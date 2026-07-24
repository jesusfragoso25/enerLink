from enum import Enum


class ConversationState(str, Enum):

    IDLE = "idle"

    WAITING_SLOT = "waiting_slot"

    READY = "ready"

    FINISHED = "finished"