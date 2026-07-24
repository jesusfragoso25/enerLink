from app.assistant.context.user_context import UserContext
from app.assistant.intent.intent import Intent


class TemplateSQL:

    @staticmethod
    def build(
        intent: Intent,
        current_user: UserContext,
    ) -> str | None:

        if intent == Intent.MY_TOTAL_CONSUMPTION:

            return f"""
SELECT
    SUM(m.energia_kwh) AS total_energia_kwh
FROM usuarios u
JOIN viviendas v
    ON v.id_usuario = u.id_usuario
JOIN gateways g
    ON g.id_vivienda = v.id_vivienda
JOIN nodos n
    ON n.id_gateway = g.id_gateway
JOIN mediciones m
    ON m.id_nodo = n.id_nodo
WHERE u.id_usuario = {current_user.id_usuario};
"""

        if intent == Intent.MY_TODAY_CONSUMPTION:

            return f"""
SELECT
    SUM(m.energia_kwh) AS total_energia_kwh
FROM usuarios u
JOIN viviendas v
    ON v.id_usuario = u.id_usuario
JOIN gateways g
    ON g.id_vivienda = v.id_vivienda
JOIN nodos n
    ON n.id_gateway = g.id_gateway
JOIN mediciones m
    ON m.id_nodo = n.id_nodo
WHERE
    u.id_usuario = {current_user.id_usuario}
    AND m.fecha_hora >= CURRENT_DATE
    AND m.fecha_hora < CURRENT_DATE + INTERVAL '1 day';
"""

        if intent == Intent.MY_MONTH_CONSUMPTION:

            return f"""
SELECT
    SUM(m.energia_kwh) AS total_energia_kwh
FROM usuarios u
JOIN viviendas v
    ON v.id_usuario = u.id_usuario
JOIN gateways g
    ON g.id_vivienda = v.id_vivienda
JOIN nodos n
    ON n.id_gateway = g.id_gateway
JOIN mediciones m
    ON m.id_nodo = n.id_nodo
WHERE
    u.id_usuario = {current_user.id_usuario}
    AND DATE_TRUNC('month', m.fecha_hora) = DATE_TRUNC('month', CURRENT_DATE);
"""

        if intent == Intent.MY_DEVICES:

            return f"""
SELECT
    COUNT(*) AS total_dispositivos
FROM usuarios u
JOIN viviendas v
    ON v.id_usuario = u.id_usuario
JOIN gateways g
    ON g.id_vivienda = v.id_vivienda
JOIN nodos n
    ON n.id_gateway = g.id_gateway
WHERE u.id_usuario = {current_user.id_usuario};
"""

        if intent == Intent.MY_GATEWAYS:

            return f"""
SELECT
    COUNT(*) AS total_gateways
FROM usuarios u
JOIN viviendas v
    ON v.id_usuario = u.id_usuario
JOIN gateways g
    ON g.id_vivienda = v.id_vivienda
WHERE u.id_usuario = {current_user.id_usuario};
"""

        if intent == Intent.MY_EVENTS:

            return f"""
SELECT
    COUNT(*) AS total_eventos
FROM usuarios u
JOIN viviendas v
    ON v.id_usuario = u.id_usuario
JOIN gateways g
    ON g.id_vivienda = v.id_vivienda
JOIN nodos n
    ON n.id_gateway = g.id_gateway
JOIN eventos e
    ON e.id_nodo = n.id_nodo
WHERE u.id_usuario = {current_user.id_usuario};
"""

        return None