from enum import Enum


class IntentType(str, Enum):

    GENERAL = "general"

    CONSUMPTION = "consumption"

    EVENTS = "events"

    RECOMMENDATION = "recommendation"

    UNKNOWN = "unknown"