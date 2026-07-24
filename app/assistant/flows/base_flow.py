from abc import ABC, abstractmethod

from app.assistant.conversation.conversation_context import ConversationContext
from app.assistant.conversation.conversation_state import ConversationState
from app.assistant.conversation.slot_filler import SlotFiller
from app.assistant.conversation.slot_type import SlotType


class BaseFlow(ABC):

    @property
    @abstractmethod
    def required_slots(self) -> list[SlotType]:
        pass

    @abstractmethod
    def execute(
        self,
        conversation: ConversationContext,
        current_user,
    ) -> str:
        pass

    @abstractmethod
    def ask_for_slot(
        self,
        slot: SlotType,
        conversation: ConversationContext,
        current_user,
    ) -> str:
        pass

    def start(
        self,
        conversation: ConversationContext,
        current_user,
    ) -> str:

        self._initialize_slots(conversation)

        missing = SlotFiller.next_missing_slot(
            conversation.slots,
        )

        if missing:

            conversation.current_slot = missing.type
            conversation.state = ConversationState.WAITING_SLOT

            return self.ask_for_slot(
                missing.type,
                conversation,
                current_user,
            )

        conversation.current_slot = None
        conversation.state = ConversationState.READY

        return self.execute(
            conversation,
            current_user,
        )

    def continue_flow(
        self,
        conversation: ConversationContext,
        current_user,
    ) -> str:

        missing = SlotFiller.next_missing_slot(
            conversation.slots,
        )

        if missing:

            conversation.current_slot = missing.type
            conversation.state = ConversationState.WAITING_SLOT

            return self.ask_for_slot(
                missing.type,
                conversation,
                current_user,
            )

        conversation.current_slot = None
        conversation.state = ConversationState.READY

        return self.execute(
            conversation,
            current_user,
        )

    def _initialize_slots(
        self,
        conversation: ConversationContext,
    ):

        for slot_type in self.required_slots:

            SlotFiller.add_slot(
                conversation.slots,
                slot_type,
            )