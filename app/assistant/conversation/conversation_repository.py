from sqlalchemy import text

from app.database import SessionLocal


class ConversationRepository:

    @staticmethod
    def get_user_houses(id_usuario: int) -> list[dict]:

        db = SessionLocal()

        try:

            result = db.execute(

                text("""
                    SELECT
                        id_vivienda,
                        nombre
                    FROM viviendas
                    WHERE id_usuario = :id_usuario
                    ORDER BY id_vivienda
                """),

                {
                    "id_usuario": id_usuario
                }

            )

            return [
                dict(row)
                for row in result.mappings()
            ]

        finally:

            db.close()

    @staticmethod
    def get_house_gateways(id_vivienda: int) -> list[dict]:

        db = SessionLocal()

        try:

            result = db.execute(

                text("""
                    SELECT
                        id_gateway,
                        nombre
                    FROM gateways
                    WHERE id_vivienda = :id_vivienda
                    ORDER BY id_gateway
                """),

                {
                    "id_vivienda": id_vivienda
                }

            )

            return [
                dict(row)
                for row in result.mappings()
            ]

        finally:

            db.close()

    @staticmethod
    def house_names(id_usuario: int) -> list[str]:

        return [

        house["nombre"]

        for house in ConversationRepository.get_user_houses(
            id_usuario
        )

    ]
    @staticmethod
    def gateway_names(id_vivienda: int) -> list[str]:

        return [

        gateway["nombre"]

        for gateway in ConversationRepository.get_house_gateways(
            id_vivienda
        )

    ]