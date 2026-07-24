from sqlalchemy import inspect

from app.database import Base, engine


class DatabaseSchema:

    @staticmethod
    def get_schema() -> dict:

        inspector = inspect(engine)

        schema = {}

        for mapper in Base.registry.mappers:

            table = mapper.local_table

            table_name = table.name

            columns = [
                column.name
                for column in table.columns
            ]

            foreign_keys = []

            for fk in inspector.get_foreign_keys(table_name):

                if fk["referred_table"] is None:
                    continue

                foreign_keys.append({
                    "column": fk["constrained_columns"][0],
                    "references_table": fk["referred_table"],
                    "references_column": fk["referred_columns"][0],
                })

            schema[table_name] = {
                "columns": columns,
                "foreign_keys": foreign_keys,
            }

        return schema