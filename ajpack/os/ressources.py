import psutil

def get_system_resources() -> dict:
    """Returns system resource usage statistics."""
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "virtual_memory": psutil.virtual_memory()._asdict(),
        "swap_memory": psutil.swap_memory()._asdict(),
        "disk_usage": psutil.disk_usage('/')._asdict(),
    }