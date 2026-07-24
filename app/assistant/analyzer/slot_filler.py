from app.assistant.conversation.slot import Slot
from app.assistant.conversation.slot_type import SlotType


class SlotFiller:

    @staticmethod
    def has_slot(
        slots: list[Slot],
        slot_type: SlotType,
    ) -> bool:

        return any(
            slot.type == slot_type
            for slot in slots
        )

    @staticmethod
    def add_slot(
        slots: list[Slot],
        slot_type: SlotType,
        required: bool = True,
    ):

        if SlotFiller.has_slot(slots, slot_type):
            return

        slots.append(
            Slot(
                type=slot_type,
                required=required,
            )
        )

    @staticmethod
    def get_slot(
        slots: list[Slot],
        slot_type: SlotType,
    ) -> Slot | None:

        for slot in slots:

            if slot.type == slot_type:

                return slot

        return None

    @staticmethod
    def fill_slot(
        slots: list[Slot],
        slot_type: SlotType,
        value,
    ):

        slot = SlotFiller.get_slot(
            slots,
            slot_type,
        )

        if slot is None:
            return

        slot.value = value
        slot.completed = True

    @staticmethod
    def next_missing_slot(
        slots: list[Slot],
    ) -> Slot | None:

        for slot in slots:

            if slot.required and not slot.completed:

                return slot

        return None