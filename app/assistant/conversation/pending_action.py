from enum import Enum


class PendingAction(str, Enum):

    NONE = "none"

    SELECT_HOUSE = "select_house"

    SELECT_GATEWAY = "select_gateway"