import time
from typing import Any

def log_execution_time(decimals: int = 4) -> Any:
    """Logs the execution time of a function with the specified number of decimal places."""
    def start_function(func) -> Any:
        def wrapper(*args, **kwargs) -> Any:
            start_time: float = time.time()

            # Run function
            result: Any = func(*args, **kwargs)

            print(f"Function '{func.__name__}' executed in {(time.time() - start_time):.{decimals}f} seconds")
            return result
        return wrapper
    return start_function
