from app.assistant.analyzer.intent_keywords import INTENT_KEYWORDS
from app.assistant.analyzer.intent_type import IntentType


class IntentAnalyzer:

    @staticmethod
    def analyze(question: str) -> IntentType:

        question = question.lower()

        print(f"Pregunta: {question}")
        print(INTENT_KEYWORDS)

        best_intent = IntentType.UNKNOWN
        best_score = 0

        for intent, keywords in INTENT_KEYWORDS.items():

            score = 0

            for keyword in keywords:

                if keyword in question:

                    print(f"Coincidencia: {keyword} -> {intent}")

                    score += 1

            if score > best_score:

                best_score = score
                best_intent = intent

        print(f"Intent detectado: {best_intent}")

        return best_intent