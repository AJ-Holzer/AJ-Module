import time

def waiter(seconds: int | float | None = None) -> None:
    """Waits for the provided time or ininite long."""
    if seconds is None:
        while True:
            time.sleep(4e6)
    else:
        time.sleep(seconds)