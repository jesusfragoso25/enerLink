from app.assistant.knowledge.knowledge_cache import KnowledgeCache


class SchemaSelector:

    TABLE_KEYWORDS = {

        "usuarios": [
            "usuario",
            "usuarios",
            "perfil",
            "cuenta",
        ],

        "viviendas": [
            "vivienda",
            "casa",
            "hogar",
        ],

        "gateways": [
            "gateway",
            "gateways",
        ],

        "nodos": [
            "nodo",
            "nodos",
            "dispositivo",
            "dispositivos",
            "sensor",
            "sensores",
        ],

        "mediciones": [
            "consumo",
            "energia",
            "energía",
            "kwh",
            "kw",
            "voltaje",
            "corriente",
            "potencia",
            "medicion",
            "medición",
            "historial",
        ],

        "eventos": [
            "evento",
            "eventos",
            "alarma",
            "alerta",
        ],
    }

    @classmethod
    def select(cls, question: str) -> dict:

        question = question.lower()

        knowledge = KnowledgeCache.get()

        selected = {}

        for table, keywords in cls.TABLE_KEYWORDS.items():

            if any(keyword in question for keyword in keywords):

                if table in knowledge:
                    selected[table] = knowledge[table]

        if not selected:
            return knowledge

        return selected