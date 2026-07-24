from sqlalchemy import text

from app.database import SessionLocal


class NodeRepository:

    @staticmethod
    def get_by_gateway(
        id_gateway: int,
    ) -> list[dict]:

        sql = text("""
            SELECT
                id_nodo,
                nombre
            FROM nodos
            WHERE id_gateway = :id_gateway
            ORDER BY nombre;
        """)

        with SessionLocal() as db:

            result = db.execute(
                sql,
                {
                    "id_gateway": id_gateway,
                },
            )

            return [
                dict(row._mapping)
                for row in result
            ]