import threading
from typing import Callable, Any

def schedule_task(time: float, func: Callable[[Any], Any], **kwargs) -> None:
    """
    Schedules a task to run at a specified time in the future.

    :param time (float): The time to wait, before running the task.
    :param func (Callable[[], Any]): The function to run.
    :param kwargs: Any additional keyword arguments to pass to the function.
    """
    def wrapper():
        func(**kwargs)
    threading.Timer(time, wrapper).start()
