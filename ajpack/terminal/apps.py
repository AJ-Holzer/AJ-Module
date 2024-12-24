import msvcrt, os, platform
from ..settings import settings

def wait(msg: str = "Press any key to continue...") -> bytes:
    """
    Waits for the user to press a key.
    
    :param msg: The msg to show.
    :return: bytes --> Pressed key.
    """
    print(msg)

    return msvcrt.getch()

def size_calc(unit: str, file: str, decimal_place: int = 1) -> float:
    """
    Calculates the size and returns it as specific unit.\n
    Supported units: b, kb, mb, gb, tb, pb, eb

    :param unit: The converted unit.
    :param file: The file path.
    :param decimal_place: The decimal place.
    :return: The size in the specified file.
    """
    possible_sizes: dict = {
        "b": 1,           # bytes
        "kb": 1024,       # kilobytes
        "mb": 1024 ** 2,  # megabyte
        "gb": 1024 ** 3,  # gigabytes
        "tb": 1024 ** 4,  # terabytes
        "pb": 1024 ** 5,  # petabytes
        "eb": 1024 ** 6,   # exabytes
    }

    if not unit in possible_sizes.keys():
        raise ValueError(f"Invalid unit: {unit}.")

    return round(os.path.getsize(file) / possible_sizes[unit], decimal_place)

def cls() -> None:
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def colored_text(txt: str, color: str) -> str:
    """
    Returns the colored text.\n
    Supported colors: red, green, yellow, blue, magenta, cyan, white, gray

    :param txt: The txt to convert.
    :param color: The color to use.
    :return: str --> The colored txt.
    """
    colors: dict[str, str] = {
        "gray":    settings.GRAY,
        "red":     settings.RED,
        "green":   settings.GREEN,
        "yellow":  settings.YELLOW,
        "blue":    settings.BLUE,
        "magenta": settings.MAGENTA,
        "cyan":    settings.CYAN,
        "white":   settings.WHITE,
    }

    if color not in colors.keys():
        raise ValueError(f"Invalid color: {color}.")
    
    return f"{colors[color]}{txt}{colors["white"]}"

def err(err_msg: str, error: Exception, sep: str = "-->") -> None:
    """
    Prints the error message and the error itself.
    
    :param err_msg: The message to show.
    :param error: The error to show.
    :param sep: The separator between the message and the error.
    :return: The error message.
    """
    red: str = "\033[91m"
    white: str = "\033[97m"
    
    print(red + f"[ ERROR ]:    {err_msg} {sep} {error}" + white)

def suc(txt: str) -> None:
    """
    Prints the success message.
    
    :param txt: The txt to use.
    """
    green: str = "\033[92m"
    white: str = "\033[97m"

    print(green + f"[ SUCCESS ]:  {txt}" + white)

def war(warning: str, additional_msg: str = "", sep: str = "-->") -> None:
    """
    Prints the warning message.

    :param warning: The warning message to use.
    :param additional_msg: The additional message to use.
    :param sep: The separator between the message and the additional message.
    """
    yellow: str = "\033[93m"
    white: str = "\033[97m"

    if additional_msg != "": print(yellow + f"[ WARNING ]:  {warning} {sep} {additional_msg}" + white)
    else: print(yellow + f"[ WARNING ]:  {warning}" + white)

def deb(txt: str, state: bool) -> None:
    """
    Prints a debug message.
    
    :param txt: The message to print.
    :param state: Whether to print the message or not.
    """
    cyan: str = "\033[96m"
    white: str = "\033[97m"

    if state:
        print(cyan + f"[ DEBUG ]:    {txt}" + white)

def inf(txt: str) -> None:
    """
    Prints a test message.

    :param txt: The message to print.    
    """
    blue: str = "\033[94m"
    white: str = "\033[97m"

    print(blue + f"[ INFO ]:     {txt}" + white)

def formatted_text(txt: str, format: str) -> str:
    """
    Returns text string formatted as bold, italic or underlined.\n
    Supported formats: bold, italic, underline, underline_double, invisible, cross_out

    :param txtt: The text to use.
    :param format: What format should be used.
    """
    formats: dict[str, str] = {
        "bold":             settings.BOLD,
        "italic":           settings.ITALIC,
        "underline":        settings.UNDERLINE,
        "invisible":        settings.INVISIBLE,
        "cross_out":        settings.STRIKETHROUGH,
        "underline_double": settings.UNDERLINE_DOUBLE
    }

    if not format in formats.keys():
        raise ValueError(f"Invalid format: {format}.")

    return f"{formats[format]}{txt}\033[0m"

def get_sys_info() -> dict[str, str]:
    """
    Returns a dictionary containing system information.\n
    Supported infos:\n
        - System\n
        - Mode Name\n
        - Release\n
        - Version\n
        - Machine\n
        - Processor\n
        - Architecture\n
        - Win32 Edition\n
        - Win32 Version
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
