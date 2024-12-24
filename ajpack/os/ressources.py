import psutil #type:ignore

def get_system_resources() -> dict[str, str]:
    """
    :return (dict[str, str]): System resource usage statistics.
    """
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "virtual_memory": psutil.virtual_memory()._asdict(),
        "swap_memory": psutil.swap_memory()._asdict(),
        "disk_usage": psutil.disk_usage('/')._asdict(),
    }
