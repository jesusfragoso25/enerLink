from app.assistant.context.user_context import UserContext


class QueryContextBuilder:

    @staticmethod
    def build(
        question: str,
        current_user: UserContext,
    ) -> str:

        return f"""
USUARIO AUTENTICADO

ID Usuario: {current_user.id_usuario}

Nombre: {current_user.nombre_completo}

Correo: {current_user.correo}

Teléfono: {current_user.telefono}

REGLAS

- Si la pregunta hace referencia a:
    - mi
    - mis
    - yo
    - conmigo

Debes filtrar utilizando:

u.id_usuario = {current_user.id_usuario}

Nunca filtres utilizando:

- nombre
- apellido
- correo
- teléfono
"""