import time
from typing import Callable, Any

def try_loop(
        func: Callable[..., Any|None],
        delay: float = 1,
        loops: int=1,
        **kwargs
) -> Any:
    """
    Attempts to execute a function multiple times with a delay between attempts.

    :param loops (int): The number of times to attempt to execute the function.
    :param delay (float): The time to wait between attempts in seconds.
    :param func (Callable[..., Any|None]): The function to execute.
    :param **kwargs: Keyword arguments to pass to the function.

    :return (Any): The result of the function execution, or None if all attempts fail.
    """
    for _ in range(loops):
        try:
            return func(**kwargs)
        except Exception:
            pass

        time.sleep(delay)
    
    return None