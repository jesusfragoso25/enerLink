from sqlalchemy import text

from app.database import SessionLocal


class SQLExecutionError(Exception):
    pass


class SQLExecutor:

    @staticmethod
    def execute(sql: str) -> list[dict]:

        db = SessionLocal()

        try:

            result = db.execute(
                text(sql)
            )

            return [
                dict(row)
                for row in result.mappings()
            ]

        except Exception as e:

            raise SQLExecutionError(
                f"No fue posible ejecutar la consulta: {e}"
            )

        finally:

            db.close()