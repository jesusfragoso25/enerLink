from app.assistant.analyzer.question_type import QuestionType
from app.assistant.analyzer.patterns import GENERAL_PATTERNS, DATA_PATTERNS,ACTION_PATTERNS
import re


class QuestionAnalyzer:

    @staticmethod
    def analyze(question: str) -> QuestionType:

        question = question.lower().strip()

        for pattern in GENERAL_PATTERNS:

            if re.search(pattern, question):

                return QuestionType.GENERAL

        for pattern in DATA_PATTERNS:

            if re.search(pattern, question):

                return QuestionType.DATA_QUERY

        for pattern in ACTION_PATTERNS:

            if re.search(pattern, question):

                return QuestionType.ACTION

        return QuestionType.GENERAL