import psutil  #type:ignore
import time

def get_system_uptime() -> float:
    """
    This function returns the system uptime in seconds.

    :return uptime (float): The uptime in seconds.
    """    
    return time.time() - psutil.boot_time()

# Test
if __name__ == "__main__":
    print(f"System uptime: {get_system_uptime()} seconds")
