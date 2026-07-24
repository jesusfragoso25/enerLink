from app.assistant.analyzer.intent_analyzer import IntentAnalyzer
from app.assistant.analyzer.intent_type import IntentType
from app.assistant.analyzer.question_analyzer import QuestionAnalyzer
from app.assistant.analyzer.question_type import QuestionType
from app.assistant.context.user_context import UserContext
from app.assistant.conversation.conversation_manager import ConversationManager
from app.assistant.conversation.conversation_state import ConversationState
from app.assistant.flows.consumption_flow import ConsumptionFlow
from app.assistant.flows.conversation_flow import ConversationFlow
from app.assistant.knowledge.schema_selector import SchemaSelector
from app.assistant.llm.response_generator import ResponseGenerator
from app.assistant.ollama_service import OllamaService
from app.assistant.sql.executor import SQLExecutionError, SQLExecutor
from app.assistant.sql.generator import SQLGenerator
from app.assistant.sql.post_processor import SQLPostProcessor
from app.assistant.sql.validator import SQLValidationError, SQLValidator


class AssistantService:

    @staticmethod
    def chat(
        question: str,
        current_user: UserContext,
    ) -> str:

        conversation = ConversationManager.get(
            current_user.id_usuario
        )

        # ---------------------------------------------------------
        # Si existe una conversación en curso, continuar el flujo.
        # ---------------------------------------------------------
        if conversation.state != ConversationState.IDLE:

            return ConversationFlow.continue_flow(
                conversation=conversation,
                question=question,
                current_user=current_user,
            )

        # ---------------------------------------------------------
        # Analizar la pregunta.
        # ---------------------------------------------------------
        question_type = QuestionAnalyzer.analyze(question)

        # ---------------------------------------------------------
        # Conversación general.
        # ---------------------------------------------------------
        if question_type == QuestionType.GENERAL:

            prompt = f"""
            Eres EnerLink AI.

            Responde de forma clara, amable y profesional.

            Pregunta:

            {question}
            """

            return OllamaService.ask(prompt).strip()

        # ---------------------------------------------------------
        # Operaciones no soportadas.
        # ---------------------------------------------------------
        if question_type == QuestionType.ACTION:

            return ResponseGenerator.unsupported_operation(
                question
            )

        # ---------------------------------------------------------
        # Detectar intención.
        # ---------------------------------------------------------
        intent = IntentAnalyzer.analyze(question)


        conversation.intent = intent
        conversation.original_question = question

        ConversationManager.save(
            conversation
        )

        # ---------------------------------------------------------
        # Iniciar el flujo correspondiente.
        # ---------------------------------------------------------
        flow_response = ConversationFlow.start(
            conversation=conversation,
            current_user=current_user,
        )
        

        # Si el Flow todavía está solicitando información,
        # devolver la pregunta al usuario.
        print("FLOW RESPONSE:", repr(flow_response))

        if flow_response is not None:
            return flow_response

        # ---------------------------------------------------------
        # Cuando el Flow complete todos los Slots continuará aquí.
        # ---------------------------------------------------------
        schema = SchemaSelector.select(question)

        sql = SQLGenerator.generate(
            question=conversation.original_question,
            schema=schema,
            current_user=current_user,
        )

        sql = SQLPostProcessor.process(sql)

        try:

            SQLValidator.validate(sql)

        except SQLValidationError:

            return ResponseGenerator.unsupported_operation(
                question
            )

        try:

            data = SQLExecutor.execute(sql)

        except SQLExecutionError:

            return (
                "No fue posible realizar la consulta con la "
                "información disponible."
            )

        return ResponseGenerator.generate(
            question=conversation.original_question,
            data=data,
        )