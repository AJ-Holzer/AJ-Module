import psutil #type:ignore
from typing import Any

def get_disk_info() -> dict[str, Any]:
    """
    :return: Informations about all disk partitions.
    """
    partitions = psutil.disk_partitions()
    disk_info = {}
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)._asdict()
            disk_info[partition.device] = {
                "mountpoint": partition.mountpoint,
                "fstype": partition.fstype,
                "usage": usage
            }
        except Exception:
            pass
    return disk_info
