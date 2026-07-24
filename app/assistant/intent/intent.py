from enum import Enum


class Intent(str, Enum):

    MY_TOTAL_CONSUMPTION = "my_total_consumption"

    MY_TODAY_CONSUMPTION = "my_today_consumption"

    MY_MONTH_CONSUMPTION = "my_month_consumption"

    MY_DEVICES = "my_devices"

    MY_GATEWAYS = "my_gateways"

    MY_EVENTS = "my_events"

    DYNAMIC = "dynamic"