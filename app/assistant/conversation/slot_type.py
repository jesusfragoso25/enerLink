from enum import Enum


class SlotType(str, Enum):

    HOUSE = "house"

    GATEWAY = "gateway"

    NODE = "node"

    DATE = "date"