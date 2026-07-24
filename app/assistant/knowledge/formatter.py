class SchemaFormatter:

    @staticmethod
    def format(schema: dict) -> str:

        lines = []

        for table_name, table in schema.items():

            lines.append(f"Tabla: {table_name}")

            lines.append("Columnas:")

            for column in table["columns"]:
                lines.append(f"  - {column}")

            if table.get("foreign_keys"):

                lines.append("Relaciones:")

                for fk in table["foreign_keys"]:

                    lines.append(
                        f"  - {fk['column']} -> "
                        f"{fk['references_table']}."
                        f"{fk['references_column']}"
                    )

            lines.append("")

        return "\n".join(lines)