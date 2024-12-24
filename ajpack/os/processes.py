import psutil  #type:ignore[import-untyped]

def list_processes() -> tuple[list[str] , list[dict[str, str|int]]]:
    """
    :return: A list of all running process names.
    """
    names: list[str] = [p.name() for p in psutil.process_iter()]
    processes: list[dict[str, str|int]] = [proc.info for proc in psutil.process_iter(['pid', 'name'])]

    return names, processes
