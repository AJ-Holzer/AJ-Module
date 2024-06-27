import msvcrt, os, platform

def wait(msg: str = "Press any key to continue...") -> bytes:
    """Waits for the user to press a key. Returns the pressed key as bytes."""
    print(msg)

    return msvcrt.getch()

def size_calc(unit: str, file: str, decimal_place: int = 1) -> float:
    """
    Calculates the size and returns it as specific unit.\n
    Supported units: b, kb, mb, gb, tb, pb, eb
    """
    possible_sizes: dict = {
        "b": 1,           # bytes
        "kb": 1024,       # kilobytes
        "mb": 1024 ** 2,  # megabyte
        "gb": 1024 ** 3,  # gigabytes
        "tb": 1024 ** 4,  # terabytes
        "pb": 1024 ** 5,  # petabytes
        "eb": 1024 ** 6   # exabytes
    }

    if not unit in possible_sizes.keys():
        raise ValueError(f"Invalid unit: {unit}.")

    size: int = os.path.getsize(file)
    formatted_size: float = round(size / possible_sizes[unit], decimal_place)

    return formatted_size

def cls() -> None:
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def colored_text(text: str, color: str) -> str:
    """
    Returns the colored text.\n
    Supported colors: red, green, yellow, blue, magenta, cyan, white, gray
    """
    colors: dict[str, str] = {
        "gray":    "\033[90m",
        "red":     "\033[91m",
        "green":   "\033[92m",
        "yellow":  "\033[93m",
        "blue":    "\033[94m",
        "magenta": "\033[95m",
        "cyan":    "\033[96m",
        "white":   "\033[97m"
    }

    if color not in colors.keys():
        raise ValueError(f"Invalid color: {color}.")
    
    return f"{colors[color]}{text}{colors["white"]}"

def formatted_text(text: str, format: str) -> str:
    """
    Returns text string formatted as bold, italic or underlined.\n
    Supports: bold, italic, underline, underline_double, invisible, cross_out
    """
    formats: dict[str, str] = {
        "bold":             "\033[1m",
        "italic":           "\033[3m",
        "underline":        "\033[4m",
        "invisible":        "\033[8m",
        "cross_out":        "\033[9m",
        "underline_double": "\033[21m"
    }

    if not format in formats.keys():
        raise ValueError(f"Invalid format: {format}.")

    return f"{formats[format]}{text}\033[0m"

def get_sys_info() -> dict[str, str]:
    """
    Returns a dictionary containing system information.\n
    Supported infos:\n
        -> System\n
        -> Mode Name\n
        -> Release\n
        -> Version\n
        -> Machine\n
        -> Processor\n
        -> Architecture\n
        -> Win32 Edition\n
        -> Win32 Version
    """
    info: dict[str, str] = {
        "System":        str({platform.system()}),
        "Mode Name":     str({platform.node()}),
        "Release":       str({platform.release()}),
        "Version":       str({platform.version()}),
        "Machine":       str({platform.machine()}),
        "Processor":     str({platform.processor()}),
        "Architecture":  str({platform.architecture()}),
        "Win32 Edition": str({platform.win32_edition()}),
        "Win32 Version": str({platform.win32_ver()})
    }

    return info