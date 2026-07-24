from enum import Enum


class QuestionType(str, Enum):

    GENERAL = "general"

    DATA_QUERY = "data_query"

    ACTION = "action"

    UNSUPPORTED = "unsupported"