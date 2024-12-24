import time

def waiter(seconds: int | float | None = None) -> None:
    """
    Waits for the provided time or infinite long if seconds = None.
    
    :param seconds: The delay to wait in seconds.
    """
    if seconds is None:
        while True:
            time.sleep(4e6)
    else:
        time.sleep(seconds)
