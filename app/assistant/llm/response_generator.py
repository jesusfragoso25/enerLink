import json
from decimal import Decimal

from app.assistant.ollama_service import OllamaService
from app.assistant.responses.system_messages import (
    NO_DATA_FOUND,
    UNSUPPORTED_OPERATION,
)

class ResponseGenerator:

    @staticmethod
    def generate(
        question: str,
        data: list[dict],
    ) -> str:

        if not data:
            return NO_DATA_FOUND

        if (
            len(data) == 1
            and all(
                value is None
                for value in data[0].values()
            )
        ):
            return NO_DATA_FOUND

        prompt = f"""
Eres EnerLink AI.

Responde únicamente utilizando la información entregada.

Reglas:

- No inventes información.
- No hagas suposiciones.
- No menciones SQL.
- No menciones bases de datos.
- No menciones tablas.
- No menciones columnas.
- Responde en español.
- Sé breve y profesional.

Pregunta:

{question}

Datos:

{json.dumps(
    data,
    ensure_ascii=False,
    indent=2,
    default=lambda x: float(x)
    if isinstance(x, Decimal)
    else str(x)
)}

Respuesta:
"""

        return OllamaService.ask(prompt).strip()

    @staticmethod
    def unsupported_operation(
        question: str,
    ) -> str:

        return UNSUPPORTED_OPERATION