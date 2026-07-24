from app.assistant.prompts.business_rules import BUSINESS_RULES
from app.assistant.prompts.join_templates import JOIN_TEMPLATES


class SQLPromptBuilder:

    @staticmethod
    def build(
        user_context: str,
        schema: str,
        question: str,
    ) -> str:

        return f"""
{BUSINESS_RULES}

==================================================

{JOIN_TEMPLATES}

==================================================

CONTEXTO DEL USUARIO

{user_context}

==================================================

ESQUEMA DISPONIBLE

{schema}

==================================================

PREGUNTA

{question}

==================================================

Genera únicamente SQL PostgreSQL.
"""