from app.assistant.context.user_context import UserContext
from app.assistant.conversation.conversation_context import ConversationContext
from app.assistant.conversation.slot_filler import SlotFiller
from app.assistant.conversation.slot_type import SlotType
from app.assistant.repositories.gateway_repository import GatewayRepository
from app.assistant.repositories.house_repository import HouseRepository
from app.assistant.conversation.conversation_state import ConversationState

class ConversationResolver:

    @staticmethod
    def resolve(
        conversation: ConversationContext,
        answer: str,
        current_user: UserContext,
    ) -> None:

        slot = conversation.current_slot

        if slot == SlotType.HOUSE:

            ConversationResolver._resolve_house(
                conversation,
                answer,
                current_user,
            )

        elif slot == SlotType.GATEWAY:

            ConversationResolver._resolve_gateway(
                conversation,
                answer,
            )

    @staticmethod
    def _resolve_house(
        conversation: ConversationContext,
        answer: str,
        current_user: UserContext,
    ):

        houses = HouseRepository.get_by_user(
            current_user.id_usuario
        )

        house = ConversationResolver._find_option(
            answer,
            houses,
            "nombre",
        )

        if house is None:

            conversation.state = ConversationState.WAITING_SLOT

            return

        SlotFiller.fill_slot(
            conversation.slots,
            SlotType.HOUSE,
            house,
        )

        conversation.current_slot = None

    @staticmethod
    def _resolve_gateway(
        conversation: ConversationContext,
        answer: str,
    ):

        house = SlotFiller.get_slot(
            conversation.slots,
            SlotType.HOUSE,
        ).value

        gateways = GatewayRepository.get_by_house(
            house["id_vivienda"]
        )

        gateway = ConversationResolver._find_option(
            answer,
            gateways,
            "nombre_gateway",
        )

        if house is None:

            conversation.state = ConversationState.WAITING_SLOT

            return

        SlotFiller.fill_slot(
            conversation.slots,
            SlotType.GATEWAY,
            gateway,
        )

        conversation.current_slot = None

    @staticmethod
    def _find_option(
        answer: str,
        options: list[dict],
        field: str,
    ):

        answer = answer.strip().lower()

        # Coincidencia exacta por nombre
        for option in options:

            if option[field].lower() == answer:
                return option

        # Selección por número
        if answer.isdigit():

            index = int(answer) - 1

            if 0 <= index < len(options):
                return options[index]

        return None