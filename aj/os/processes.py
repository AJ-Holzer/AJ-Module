import psutil

def list_processes() -> list[str] | tuple[str, ...]:
    """
    Return a list of all running process names\n
    names: list[str]\n
    processes: tuple[str, ...]
    """
    names: list[str] = [p.name() for p in psutil.process_iter()]
    processes: tuple[str, ...] = [proc.info for proc in psutil.process_iter(['pid', 'name'])]

    return names, processes