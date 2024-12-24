def conv_sec(seconds: int) -> str:
    """
    Convert an integer representing seconds to a string formatted as hh:mm:ss.

    :param seconds: The total number of seconds.
    :return: A string representing the time in the format hh:mm:ss.
    """
    # Calculate hours, minutes, and remaining seconds
    hours: int = seconds // 3600
    minutes: int = (seconds % 3600) // 60
    remaining_seconds: int = seconds % 3600 % 60
    
    # Format as hh:mm:ss
    return f"{hours:02}:{minutes:02}:{remaining_seconds:02}"
