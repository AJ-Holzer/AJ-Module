from .get_drives import drives
from .processes import list_processes
from .kill import kill_process
from .ressources import get_system_resources
from .disk import get_disk_info
from .batt import get_battery_status
from .base_path import get_base_path
from .folders import get_paths, parent_folder
from .win import get_terminal_output
from .network import get_local_ip
from .uptime import get_system_uptime
from .widget import show_status_icon
from .volume import Volume

__all__: list[str] = [
    "drives",
    "list_processes",
    "kill_process",
    "get_system_resources",
    "get_disk_info",
    "get_battery_status",
    "get_base_path",
    "get_paths",
    "parent_folder",
    "get_terminal_output",
    "get_local_ip",
    "get_system_uptime",
    "show_status_icon",
    "Volume",
]