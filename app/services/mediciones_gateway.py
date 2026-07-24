from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException
from datetime import datetime, date, timedelta, timezone
from app.models.mediciones_gateway import MedicionesGateway
from app.models.gateways import Gateways
from app.models.viviendas import Viviendas


#VALIDA QUE EL GATEWAY PERTENEZCA AL USUARIO AUTENTICADO
def _validar_gateway_de_usuario(db: Session, id_gateway: int, id_usuario: int):
    gateway = (
        db.query(Gateways)
        .join(Viviendas, Gateways.id_vivienda == Viviendas.id_vivienda)
        .filter(Gateways.id_gateway == id_gateway, Viviendas.id_usuario == id_usuario)
        .first()
    )
    if not gateway:
        raise HTTPException(status_code=404, detail="Gateway no encontrado")
    return gateway


#CONSUMO DEL DIA ACTUAL PARA UN GATEWAY
def consumo_diario_por_gateway(db: Session, id_gateway: int, id_usuario: int):
    _validar_gateway_de_usuario(db, id_gateway, id_usuario)

    hoy = date.today()
    inicio = datetime.combine(hoy, datetime.min.time(), tzinfo=timezone.utc)
    fin = inicio + timedelta(days=1)

    total = (
        db.query(func.coalesce(func.sum(MedicionesGateway.energia_kwh), 0))
        .filter(
            MedicionesGateway.id_gateway == id_gateway,
            MedicionesGateway.fecha_hora >= inicio,
            MedicionesGateway.fecha_hora < fin
        )
        .scalar()
    )

    return {
        "id_gateway": id_gateway,
        "consumo_total_kwh": float(total),
        "periodo_inicio": inicio,
        "periodo_fin": fin
    }


#CONSUMO DEL MES ACTUAL PARA UN GATEWAY
def consumo_mensual_por_gateway(db: Session, id_gateway: int, id_usuario: int):
    _validar_gateway_de_usuario(db, id_gateway, id_usuario)

    ahora = datetime.now(timezone.utc)
    inicio = datetime(ahora.year, ahora.month, 1, tzinfo=timezone.utc)

    if ahora.month == 12:
        fin = datetime(ahora.year + 1, 1, 1, tzinfo=timezone.utc)
    else:
        fin = datetime(ahora.year, ahora.month + 1, 1, tzinfo=timezone.utc)

    total = (
        db.query(func.coalesce(func.sum(MedicionesGateway.energia_kwh), 0))
        .filter(
            MedicionesGateway.id_gateway == id_gateway,
            MedicionesGateway.fecha_hora >= inicio,
            MedicionesGateway.fecha_hora < fin
        )
        .scalar()
    )

    return {
        "id_gateway": id_gateway,
        "consumo_total_kwh": float(total),
        "periodo_inicio": inicio,
        "periodo_fin": fin
    }


#CONSUMO AGRUPADO POR DIA, DE LA SEMANA ACTUAL (LUNES A DOMINGO)
def consumo_semanal_por_gateway(db: Session, id_gateway: int, id_usuario: int):
    _validar_gateway_de_usuario(db, id_gateway, id_usuario)

    hoy = date.today()
    inicio_semana = hoy - timedelta(days=hoy.weekday())
    inicio = datetime.combine(inicio_semana, datetime.min.time(), tzinfo=timezone.utc)
    fin = inicio + timedelta(days=7)

    resultados = (
        db.query(
            func.date(MedicionesGateway.fecha_hora).label("fecha"),
            func.coalesce(func.sum(MedicionesGateway.energia_kwh), 0).label("consumo")
        )
        .filter(
            MedicionesGateway.id_gateway == id_gateway,
            MedicionesGateway.fecha_hora >= inicio,
            MedicionesGateway.fecha_hora < fin
        )
        .group_by(func.date(MedicionesGateway.fecha_hora))
        .all()
    )

    mapa_consumo = {r.fecha: float(r.consumo) for r in resultados}

    datos = []
    for i in range(7):
        dia = inicio_semana + timedelta(days=i)
        datos.append({
            "fecha": dia,
            "consumo_kwh": mapa_consumo.get(dia, 0.0)
        })

    return {
        "id_gateway": id_gateway,
        "periodo_inicio": inicio,
        "periodo_fin": fin,
        "datos": datos
    }

#CONSUMO TOTAL DEL DIA ACTUAL, SUMANDO TODOS LOS GATEWAYS DEL USUARIO
def consumo_diario_total_usuario(db: Session, id_usuario: int):
    hoy = date.today()
    inicio = datetime.combine(hoy, datetime.min.time(), tzinfo=timezone.utc)
    fin = inicio + timedelta(days=1)

    total = (
        db.query(func.coalesce(func.sum(MedicionesGateway.energia_kwh), 0))
        .join(Gateways, MedicionesGateway.id_gateway == Gateways.id_gateway)
        .join(Viviendas, Gateways.id_vivienda == Viviendas.id_vivienda)
        .filter(
            Viviendas.id_usuario == id_usuario,
            MedicionesGateway.fecha_hora >= inicio,
            MedicionesGateway.fecha_hora < fin
        )
        .scalar()
    )

    cantidad_gateways = (
        db.query(Gateways)
        .join(Viviendas, Gateways.id_vivienda == Viviendas.id_vivienda)
        .filter(Viviendas.id_usuario == id_usuario)
        .count()
    )

    return {
        "id_usuario": id_usuario,
        "consumo_total_kwh": float(total),
        "periodo_inicio": inicio,
        "periodo_fin": fin,
        "gateways_incluidos": cantidad_gateways
    }


#CONSUMO TOTAL DEL MES ACTUAL, SUMANDO TODOS LOS GATEWAYS DEL USUARIO
def consumo_mensual_total_usuario(db: Session, id_usuario: int):
    ahora = datetime.now(timezone.utc)
    inicio = datetime(ahora.year, ahora.month, 1, tzinfo=timezone.utc)

    if ahora.month == 12:
        fin = datetime(ahora.year + 1, 1, 1, tzinfo=timezone.utc)
    else:
        fin = datetime(ahora.year, ahora.month + 1, 1, tzinfo=timezone.utc)

    total = (
        db.query(func.coalesce(func.sum(MedicionesGateway.energia_kwh), 0))
        .join(Gateways, MedicionesGateway.id_gateway == Gateways.id_gateway)
        .join(Viviendas, Gateways.id_vivienda == Viviendas.id_vivienda)
        .filter(
            Viviendas.id_usuario == id_usuario,
            MedicionesGateway.fecha_hora >= inicio,
            MedicionesGateway.fecha_hora < fin
        )
        .scalar()
    )

    cantidad_gateways = (
        db.query(Gateways)
        .join(Viviendas, Gateways.id_vivienda == Viviendas.id_vivienda)
        .filter(Viviendas.id_usuario == id_usuario)
        .count()
    )

    return {
        "id_usuario": id_usuario,
        "consumo_total_kwh": float(total),
        "periodo_inicio": inicio,
        "periodo_fin": fin,
        "gateways_incluidos": cantidad_gateways
    }


#CONSUMO TOTAL AGRUPADO POR DIA DE LA SEMANA ACTUAL, SUMANDO TODOS LOS GATEWAYS DEL USUARIO
def consumo_semanal_total_usuario(db: Session, id_usuario: int):
    hoy = date.today()
    inicio_semana = hoy - timedelta(days=hoy.weekday())
    inicio = datetime.combine(inicio_semana, datetime.min.time(), tzinfo=timezone.utc)
    fin = inicio + timedelta(days=7)

    resultados = (
        db.query(
            func.date(MedicionesGateway.fecha_hora).label("fecha"),
            func.coalesce(func.sum(MedicionesGateway.energia_kwh), 0).label("consumo")
        )
        .join(Gateways, MedicionesGateway.id_gateway == Gateways.id_gateway)
        .join(Viviendas, Gateways.id_vivienda == Viviendas.id_vivienda)
        .filter(
            Viviendas.id_usuario == id_usuario,
            MedicionesGateway.fecha_hora >= inicio,
            MedicionesGateway.fecha_hora < fin
        )
        .group_by(func.date(MedicionesGateway.fecha_hora))
        .all()
    )

    mapa_consumo = {r.fecha: float(r.consumo) for r in resultados}

    datos = []
    for i in range(7):
        dia = inicio_semana + timedelta(days=i)
        datos.append({
            "fecha": dia,
            "consumo_kwh": mapa_consumo.get(dia, 0.0)
        })

    return {
        "id_usuario": id_usuario,
        "periodo_inicio": inicio,
        "periodo_fin": fin,
        "datos": datos
    }

#CONSUMO TOTAL AGRUPADO POR MES, DEL AÑO ACTUAL, SUMANDO TODOS LOS GATEWAYS DEL USUARIO
def consumo_anual_total_usuario(db: Session, id_usuario: int):
    anio_actual = datetime.now(timezone.utc).year
    inicio = datetime(anio_actual, 1, 1, tzinfo=timezone.utc)
    fin = datetime(anio_actual + 1, 1, 1, tzinfo=timezone.utc)

    resultados = (
        db.query(
            func.extract("month", MedicionesGateway.fecha_hora).label("mes"),
            func.coalesce(func.sum(MedicionesGateway.energia_kwh), 0).label("consumo")
        )
        .join(Gateways, MedicionesGateway.id_gateway == Gateways.id_gateway)
        .join(Viviendas, Gateways.id_vivienda == Viviendas.id_vivienda)
        .filter(
            Viviendas.id_usuario == id_usuario,
            MedicionesGateway.fecha_hora >= inicio,
            MedicionesGateway.fecha_hora < fin
        )
        .group_by(func.extract("month", MedicionesGateway.fecha_hora))
        .all()
    )

    #MAPA DE RESULTADOS EXISTENTES, PARA RELLENAR LOS MESES SIN MEDICIONES CON 0
    mapa_consumo = {int(r.mes): float(r.consumo) for r in resultados}

    datos = []
    for mes in range(1, 13):
        datos.append({
            "anio": anio_actual,
            "mes": mes,
            "consumo_kwh": mapa_consumo.get(mes, 0.0)
        })

    return {
        "id_usuario": id_usuario,
        "periodo_inicio": inicio,
        "periodo_fin": fin,
        "datos": datos
    }