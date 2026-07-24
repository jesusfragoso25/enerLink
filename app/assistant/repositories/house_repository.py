from sqlalchemy import text

from app.database import SessionLocal


class HouseRepository:

    @staticmethod
    def get_by_user(
        id_usuario: int,
    ) -> list[dict]:

        sql = text("""
            SELECT
                id_vivienda,
                nombre
            FROM viviendas
            WHERE id_usuario = :id_usuario
            ORDER BY nombre;
        """)

        with SessionLocal() as db:

            result = db.execute(
                sql,
                {
                    "id_usuario": id_usuario,
                },
            )

            return [
                dict(row._mapping)
                for row in result
            ]
        