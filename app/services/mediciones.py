from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException
from datetime import datetime, date, timedelta
from app.models.mediciones import Mediciones
from app.models.nodos import Nodos
from app.models.gateways import Gateways
from app.models.viviendas import Viviendas


#VALIDA QUE EL NODO PERTENEZCA AL USUARIO AUTENTICADO (MISMO PATRON QUE EN NODOS)
def _validar_nodo_de_usuario(db: Session, id_nodo: int, id_usuario: int):
    nodo = (
        db.query(Nodos)
        .join(Gateways, Nodos.id_gateway == Gateways.id_gateway)
        .join(Viviendas, Gateways.id_vivienda == Viviendas.id_vivienda)
        .filter(Nodos.id_nodo == id_nodo, Viviendas.id_usuario == id_usuario)
        .first()
    )
    if not nodo:
        raise HTTPException(status_code=404, detail="Nodo no encontrado")
    return nodo


#CONSUMO DEL DIA ACTUAL PARA UN NODO
def consumo_diario_por_nodo(db: Session, id_nodo: int, id_usuario: int):
    _validar_nodo_de_usuario(db, id_nodo, id_usuario)

    hoy = date.today()
    inicio = datetime.combine(hoy, datetime.min.time())
    fin = inicio + timedelta(days=1)

    total = (
        db.query(func.coalesce(func.sum(Mediciones.energia_kwh), 0))
        .filter(
            Mediciones.id_nodo == id_nodo,
            Mediciones.fecha_hora >= inicio,
            Mediciones.fecha_hora < fin
        )
        .scalar()
    )

    return {
        "id_nodo": id_nodo,
        "consumo_total_kwh": float(total),
        "periodo_inicio": inicio,
        "periodo_fin": fin
    }


#CONSUMO DEL MES ACTUAL PARA UN NODO
def consumo_mensual_por_nodo(db: Session, id_nodo: int, id_usuario: int):
    _validar_nodo_de_usuario(db, id_nodo, id_usuario)

    ahora = datetime.now()
    inicio = datetime(ahora.year, ahora.month, 1)

    if ahora.month == 12:
        fin = datetime(ahora.year + 1, 1, 1)
    else:
        fin = datetime(ahora.year, ahora.month + 1, 1)

    total = (
        db.query(func.coalesce(func.sum(Mediciones.energia_kwh), 0))
        .filter(
            Mediciones.id_nodo == id_nodo,
            Mediciones.fecha_hora >= inicio,
            Mediciones.fecha_hora < fin
        )
        .scalar()
    )

    return {
        "id_nodo": id_nodo,
        "consumo_total_kwh": float(total),
        "periodo_inicio": inicio,
        "periodo_fin": fin
    }

#CONSUMO AGRUPADO POR DIA, DE LA SEMANA ACTUAL (LUNES A DOMINGO)
def consumo_semanal_por_nodo(db: Session, id_nodo: int, id_usuario: int):
    _validar_nodo_de_usuario(db, id_nodo, id_usuario)

    hoy = date.today()
    inicio_semana = hoy - timedelta(days=hoy.weekday())  # weekday(): lunes=0
    inicio = datetime.combine(inicio_semana, datetime.min.time())
    fin = inicio + timedelta(days=7)

    resultados = (
        db.query(
            func.date(Mediciones.fecha_hora).label("fecha"),
            func.coalesce(func.sum(Mediciones.energia_kwh), 0).label("consumo")
        )
        .filter(
            Mediciones.id_nodo == id_nodo,
            Mediciones.fecha_hora >= inicio,
            Mediciones.fecha_hora < fin
        )
        .group_by(func.date(Mediciones.fecha_hora))
        .all()
    )

    #MAPA DE RESULTADOS EXISTENTES, PARA RELLENAR LOS DIAS SIN MEDICIONES CON 0
    mapa_consumo = {r.fecha: float(r.consumo) for r in resultados}

    datos = []
    for i in range(7):
        dia = inicio_semana + timedelta(days=i)
        datos.append({
            "fecha": dia,
            "consumo_kwh": mapa_consumo.get(dia, 0.0)
        })

    return {
        "id_nodo": id_nodo,
        "periodo_inicio": inicio,
        "periodo_fin": fin,
        "datos": datos
    }

