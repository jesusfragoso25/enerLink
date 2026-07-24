from app.assistant.context.user_context import UserContext
from app.assistant.conversation.conversation_context import ConversationContext
from app.assistant.conversation.slot_filler import SlotFiller
from app.assistant.conversation.slot_type import SlotType
from app.assistant.flows.base_flow import BaseFlow
from app.assistant.repositories.gateway_repository import GatewayRepository
from app.assistant.repositories.house_repository import HouseRepository


class ConsumptionFlow(BaseFlow):

    @property
    def required_slots(self) -> list[SlotType]:

        return [
            SlotType.HOUSE,
            SlotType.GATEWAY,
        ]

    def ask_for_slot(
        self,
        slot: SlotType,
        conversation: ConversationContext,
        current_user: UserContext,
    ) -> str:

        if slot == SlotType.HOUSE:

            houses = HouseRepository.get_by_user(
                current_user.id_usuario,
            )

            if not houses:
                return "No tienes viviendas registradas."

            if len(houses) == 1:

                SlotFiller.fill_slot(
                    conversation.slots,
                    SlotType.HOUSE,
                    houses[0],
                )

                if SlotFiller.get_slot(
                    conversation.slots,
                    SlotType.HOUSE,
                ) is None:

                    return "No encontré esa vivienda. Intenta nuevamente."

                return self.continue_flow(
                    conversation,
                    current_user,
                )

            text = "¿Sobre cuál vivienda deseas realizar la consulta?\n\n"

            for i, house in enumerate(houses, start=1):
                text += f"{i}. {house['nombre']}\n"

            return text

        if slot == SlotType.GATEWAY:

            house = SlotFiller.get_slot(
                conversation.slots,
                SlotType.HOUSE,
            ).value

            gateways = GatewayRepository.get_by_house(
                house["id_vivienda"],
            )

            if not gateways:
                return "La vivienda seleccionada no tiene gateways registrados."

            if len(gateways) == 1:

                SlotFiller.fill_slot(
                    conversation.slots,
                    SlotType.GATEWAY,
                    gateways[0],
                )

                return self.continue_flow(
                    conversation,
                    current_user,
                )

            text = "¿Qué gateway deseas consultar?\n\n"

            for i, gateway in enumerate(gateways, start=1):
                text += f"{i}. {gateway['nombre']}\n"

            return text

        return "No fue posible continuar."

    def execute(
        self,
        conversation: ConversationContext,
        current_user: UserContext,
    ) -> str:

        return None