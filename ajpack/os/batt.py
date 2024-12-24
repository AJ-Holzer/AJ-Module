import psutil #type:ignore
from psutil import _common

def get_battery_status() -> dict[str, str]|None:
    """
    Gets the battery status.

    Including:
        - percent
        - seconds_left
        - power_plugged

    :return (dict[str, str] | None): The current battery status. Returns None, if no battery found.
    """
    battery: _common.sbattery = psutil.sensors_battery()

    return {
        "percent":       str(battery.percent),
        "seconds_left":  str(battery.secsleft),
        "power_plugged": str(battery.power_plugged),
    } if battery else None
