from app.assistant.conversation.conversation_context import ConversationContext


class ConversationManager:

    _sessions: dict[int, ConversationContext] = {}

    @classmethod
    def get(cls, user_id: int) -> ConversationContext:

        if user_id not in cls._sessions:

            cls._sessions[user_id] = ConversationContext(
                user_id=user_id
            )

        return cls._sessions[user_id]

    @classmethod
    def save(cls, context: ConversationContext):

        cls._sessions[context.user_id] = context

    @classmethod
    def clear(cls, user_id: int):

        if user_id in cls._sessions:

            del cls._sessions[user_id]