from app.assistant.intent.intent import Intent


class IntentRouter:

    @staticmethod
    def detect(question: str) -> Intent:

        q = question.lower()

        if "consumo" in q and "hoy" in q:
            return Intent.MY_TODAY_CONSUMPTION

        if "consumo" in q and "mes" in q:
            return Intent.MY_MONTH_CONSUMPTION

        if "consumo" in q:
            return Intent.MY_TOTAL_CONSUMPTION

        if "dispositivos" in q:
            return Intent.MY_DEVICES

        if "gateways" in q:
            return Intent.MY_GATEWAYS

        if "eventos" in q:
            return Intent.MY_EVENTS

        return Intent.DYNAMIC