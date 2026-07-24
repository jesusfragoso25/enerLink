from app.assistant.analyzer.intent_type import IntentType


INTENT_KEYWORDS = {

    IntentType.CONSUMPTION: [

        "consumo",
        "consumí",
        "consumi",
        "energía",
        "energia",
        "kwh",
        "kw",
        "voltaje",
        "voltios",
        "volt",
        "corriente",
        "amperaje",
        "amp",
        "potencia",
        "watts",
        "w",
        "factor de potencia",
        "frecuencia",
        "hz",
        "medición",
        "mediciones",
        "gasto",
        "gasté",
        "gaste",

    ],

    IntentType.EVENTS: [

        "evento",
        "eventos",
        "alarma",
        "alarmas",
        "alerta",
        "alertas",
        "falla",
        "fallas",
        "desconectado",
        "apagón",
        "apagon",

    ],

    IntentType.RECOMMENDATION: [

        "recomendación",
        "recomendacion",
        "recomienda",
        "aconseja",
        "mejorar",
        "optimizar",
        "ahorrar",
        "ahorro",
        "eficiencia",

    ],

}