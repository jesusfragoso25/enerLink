from app.assistant.analyzer.intent_type import IntentType
from app.assistant.conversation.conversation_context import ConversationContext
from app.assistant.flows.consumption_flow import ConsumptionFlow
from app.assistant.flows.EventsFlow import EventsFlow
from app.assistant.flows.RecommendationFlow import RecommendationFlow
from app.assistant.conversation.conversation_resolver import ConversationResolver
from app.assistant.conversation.conversation_manager import ConversationManager

class ConversationFlow:

    @staticmethod
    def continue_flow(
        conversation,
        question,
        current_user,
    ):
        ConversationResolver.resolve(
            conversation=conversation,
            answer=question,
            current_user=current_user,
        )
        flow = ConversationFlow._resolve_flow(
        conversation.intent,
    )

        response = flow.continue_flow(
            conversation,
            current_user,
        )

        ConversationManager.save(
            conversation,
        )

        return response

    @staticmethod
    def start(
        conversation: ConversationContext,
        current_user,
    ) -> str:

        flow = ConversationFlow._resolve_flow(
            conversation.intent
        )

        return flow.start(
            conversation=conversation,
            current_user=current_user,
        )

    @staticmethod
    def _resolve_flow(
        intent: IntentType,
    ):

        if intent == IntentType.CONSUMPTION:
            return ConsumptionFlow()

        if intent == IntentType.EVENTS:
            return EventsFlow()


        raise ValueError(
            f"No existe un Flow para la intención {intent}"
        )