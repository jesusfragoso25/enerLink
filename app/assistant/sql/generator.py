from app.assistant.context.query_context_builder import QueryContextBuilder
from app.assistant.context.user_context import UserContext
from app.assistant.knowledge.formatter import SchemaFormatter
from app.assistant.ollama_service import OllamaService
from app.assistant.prompts.sql_prompt import SQLPromptBuilder


class SQLGenerator:

    @staticmethod
    def generate(
        question: str,
        schema: str,
        current_user: UserContext,
        conversation=None,
    ) -> str:

        formatted_schema = SchemaFormatter.format(schema)

        query_context = QueryContextBuilder.build(
            question=question,
            current_user=current_user,
        )

        prompt = SQLPromptBuilder.build(
            user_context=query_context,
            schema=formatted_schema,
            question=question,
        )

        return OllamaService.ask(prompt).strip()