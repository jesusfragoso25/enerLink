import sqlglot
from sqlglot import exp


class SQLValidationError(Exception):
    pass


class SQLValidator:

    @classmethod
    def validate(cls, sql: str) -> None:

        if not sql:
            raise SQLValidationError(
                "La consulta SQL está vacía."
            )

        if sql.strip().upper() == "INVALID_QUERY":
            raise SQLValidationError(
                "No fue posible generar una consulta válida."
            )

        try:

            tree = sqlglot.parse_one(
                sql,
                read="postgres",
            )

        except Exception as e:

            raise SQLValidationError(
                f"SQL inválido: {e}"
            )

        cls._validate_select(tree)

    @staticmethod
    def _validate_select(tree):

        if not isinstance(tree, exp.Select):

            raise SQLValidationError(
                "Solo se permiten consultas SELECT."
            )

        forbidden = (
            exp.Delete,
            exp.Insert,
            exp.Update,
            exp.Drop,
            exp.Create,
            exp.Alter,
        )

        for node in tree.walk():

            if isinstance(node, forbidden):

                raise SQLValidationError(
                    "La consulta contiene operaciones no permitidas."
                )