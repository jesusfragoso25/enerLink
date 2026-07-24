from fastapi import APIRouter, Depends

from app.assistant.context.user_context import UserContext
from app.assistant.services.assistant_service import AssistantService
from app.security import (get_current_user)
from app.schemas.assistant import (
    AssistantRequest,
    AssistantResponse,
)

router = APIRouter(
    prefix="/assistant",
    tags=["Assistant"],
)


@router.post(
    "/chat",
    response_model=AssistantResponse,
)
def chat(
    request: AssistantRequest,
    current_user=Depends(get_current_user),
):

    user_context = UserContext(

        id_usuario=current_user["id_usuario"],

        nombre_completo=f"{current_user['nombre']} {current_user['apellido']}",

        correo=current_user["correo"],

        telefono=current_user["telefono"],

    )

    answer = AssistantService.chat(
        question=request.question,
        current_user=user_context,
    )
    print("ANSWER:", repr(answer))
    return AssistantResponse(
        answer=answer
    )