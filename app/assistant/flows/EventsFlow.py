from app.assistant.flows.base_flow import BaseFlow
from app.assistant.conversation.slot_type import SlotType

class EventsFlow(BaseFlow):

    @property
    def required_slots(self):

        return [
            SlotType.HOUSE,
            SlotType.GATEWAY,
            SlotType.DATE,
        ]