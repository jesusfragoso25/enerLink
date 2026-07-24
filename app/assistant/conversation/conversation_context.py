from dataclasses import dataclass, field

from app.assistant.analyzer.intent_type import IntentType
from app.assistant.conversation.conversation_state import ConversationState
from app.assistant.conversation.slot import Slot
from app.assistant.conversation.slot_type import SlotType


@dataclass
class ConversationContext:

    user_id: int

    state: ConversationState = ConversationState.IDLE

    intent: IntentType = IntentType.UNKNOWN

    original_question: str = ""

    slots: list[Slot] = field(default_factory=list)

    current_slot: SlotType | None = None

    finished: bool = False