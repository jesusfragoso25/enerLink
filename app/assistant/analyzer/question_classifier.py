from app.assistant.analyzer.patterns import (
    ACTION_PATTERNS,
    DATA_PATTERNS,
    GENERAL_PATTERNS,
    INCOMPLETE_PATTERNS,
)
from app.assistant.analyzer.question_type import QuestionType


class QuestionClassifier:

    @staticmethod
    def classify(question: str) -> QuestionType:

        question = question.lower().strip()

        # -----------------------------
        # Frases incompletas
        # -----------------------------

        if question in INCOMPLETE_PATTERNS:

            return QuestionType.INCOMPLETE

        # -----------------------------
        # Acciones
        # -----------------------------

        for keyword in ACTION_PATTERNS:

            if keyword in question:

                return QuestionType.ACTION

        # -----------------------------
        # Consultas de datos
        # -----------------------------

        data_score = 0

        for keyword in DATA_PATTERNS:

            if keyword in question:

                data_score += 1

        if data_score > 0:

            return QuestionType.DATA_QUERY

        # -----------------------------
        # Conversación general
        # -----------------------------

        for keyword in GENERAL_PATTERNS:

            if keyword in question:

                return QuestionType.GENERAL

        # -----------------------------
        # No reconocida
        # -----------------------------

        return QuestionType.UNSUPPORTED