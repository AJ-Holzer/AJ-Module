import psutil

def get_battery_status() -> dict:
    """Returns the current battery status. Works only on a device with a batterie!"""
    battery = psutil.sensors_battery()
    return {
        "percent": battery.percent,
        "seconds_left": battery.secsleft,
        "power_plugged": battery.power_plugged
    }