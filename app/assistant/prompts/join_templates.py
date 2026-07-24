JOIN_TEMPLATES = """
RELACIONES ENTRE TABLAS

Para consultar mediciones utiliza SIEMPRE:

usuarios.id_usuario = viviendas.id_usuario

viviendas.id_vivienda = gateways.id_vivienda

gateways.id_gateway = nodos.id_gateway

nodos.id_nodo = mediciones.id_nodo


Para consultar eventos utiliza SIEMPRE:

usuarios.id_usuario = viviendas.id_usuario

viviendas.id_vivienda = gateways.id_vivienda

gateways.id_gateway = nodos.id_gateway

nodos.id_nodo = eventos.id_nodo


REGLAS

- Nunca inventes JOIN.
- Nunca cambies las columnas de las relaciones.
- Utiliza exclusivamente las relaciones anteriores.
"""