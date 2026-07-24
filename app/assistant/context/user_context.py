from dataclasses import dataclass


@dataclass
class UserContext:

    id_usuario: int

    nombre_completo: str

    correo: str

    telefono: str