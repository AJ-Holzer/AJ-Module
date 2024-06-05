import psutil
from typing import List, Tuple, Dict, Any

def list_processes() -> Tuple[List[str], List[Dict[str, Any]]]:
    """
    Return a list of all running process names\n
    names: list[str]\n
    processes: tuple[str, ...]
    """
    names: list[str] = [p.name() for p in psutil.process_iter()]
    processes: list[Any] = [proc.info for proc in psutil.process_iter(['pid', 'name'])]

    return names, processes