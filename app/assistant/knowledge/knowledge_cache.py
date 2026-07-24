from app.assistant.knowledge.database_schema import DatabaseSchema
from app.assistant.knowledge.descriptions import TABLE_DESCRIPTIONS


class KnowledgeCache:

    _knowledge = {}

    @classmethod
    def load(cls):

        schema = DatabaseSchema.get_schema()

        knowledge = {}

        for table_name, table_data in schema.items():

            knowledge[table_name] = {

                "description": TABLE_DESCRIPTIONS.get(
                    table_name,
                    "Sin descripción."
                ),

                "columns": table_data["columns"],

                "foreign_keys": table_data.get(
                    "foreign_keys",
                    []
                ),
            }

        cls._knowledge = knowledge

    @classmethod
    def get(cls):

        return cls._knowledge