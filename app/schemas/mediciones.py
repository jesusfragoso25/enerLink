from pydantic import BaseModel
from datetime import date, datetime
from typing import List

class ConsumoResponse(BaseModel):
    id_nodo: int
    consumo_total_kwh: float
    periodo_inicio: datetime
    periodo_fin: datetime

class ConsumoPorDia(BaseModel):
    fecha: date
    consumo_kwh: float


class ConsumoSemanalResponse(BaseModel):
    id_nodo: int
    periodo_inicio: datetime
    periodo_fin: datetime
    datos: List[ConsumoPorDia]

class ConsumoGatewayResponse(BaseModel):
    id_gateway: int
    consumo_total_kwh: float
    periodo_inicio: datetime
    periodo_fin: datetime


class ConsumoPorDiaGateway(BaseModel):
    fecha: date
    consumo_kwh: float


class ConsumoSemanalGatewayResponse(BaseModel):
    id_gateway: int
    periodo_inicio: datetime
    periodo_fin: datetime
    datos: List[ConsumoPorDiaGateway]


class ConsumoTotalResponse(BaseModel):
    id_usuario: int
    consumo_total_kwh: float
    periodo_inicio: datetime
    periodo_fin: datetime
    gateways_incluidos: int

class ConsumoPorDiaTotal(BaseModel):
    fecha: date
    consumo_kwh: float

class ConsumoSemanalTotalResponse(BaseModel):
    id_usuario: int
    periodo_inicio: datetime
    periodo_fin: datetime
    datos: List[ConsumoPorDiaTotal]

class ConsumoPorMes(BaseModel):
    anio: int
    mes: int
    consumo_kwh: float


class ConsumoAnualTotalResponse(BaseModel):
    id_usuario: int
    periodo_inicio: datetime
    periodo_fin: datetime
    datos: List[ConsumoPorMes]