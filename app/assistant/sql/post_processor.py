import re


class SQLPostProcessor:

    @staticmethod
    def process(sql: str) -> str:

        replacements = {

            r"\bCURDATE\s*\(\s*\)": "CURRENT_DATE",

            r"\bNOW\s*\(\s*\)": "CURRENT_TIMESTAMP",

            r"\bIFNULL\s*\(": "COALESCE(",
        }

        for pattern, replacement in replacements.items():

            sql = re.sub(
                pattern,
                replacement,
                sql,
                flags=re.IGNORECASE,
            )

        return sql