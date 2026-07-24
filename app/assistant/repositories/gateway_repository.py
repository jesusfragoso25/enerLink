from sqlalchemy import text

from app.database import SessionLocal


class GatewayRepository:

    @staticmethod
    def get_by_house(
        id_vivienda: int,
    ) -> list[dict]:

        sql = text("""
            SELECT
                id_gateway,
                nombre_gateway
            FROM gateways
            WHERE id_vivienda = :id_vivienda
            ORDER BY nombre_gateway;
        """)

        with SessionLocal() as db:

            result = db.execute(
                sql,
                {
                    "id_vivienda": id_vivienda,
                },
            )

            return [
                dict(row._mapping)
                for row in result
            ]