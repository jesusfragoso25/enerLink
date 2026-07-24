from dataclasses import dataclass

from app.assistant.conversation.slot_type import SlotType


@dataclass
class Slot:

    type: SlotType

    value: object | None = None

    required: bool = True

    completed: bool = False