from typing import Any
from ..settings import settings

def _print(txt: Any, nl: bool) -> None:
    """
    Helper function for printing a text without a line breaking at the end.
    
    :param nl: If line breaking should be used.
    """
    print(txt, end="", flush=True) if nl else print(txt)

def printl(txt: Any) -> None:
    """
    Prints a text without line breaking at the end.
    
    :param txt: The message to print.
    """
    _print(txt, True)

def printst(txt: Any) -> None:
    """
    Prints a message when the task starts.
    Automaticly adds '... '.
    
    Should be used with printet().

    :param txt: The message for the task to print.
    """
    _print(txt + "... ", True)

def printet_ok() -> None:
    """
    Should be called after the printst().

    Prints an 'OK' after the start task function.
    """
    green: str = settings.GREEN
    white: str = settings.WHITE
    _print(green + "OK" + white, False)

def printet_err() -> None:
    """
    Should be called after the printst().

    Prints an 'ERR' after the start task function.
    """
    red: str = settings.RED
    white: str = settings.WHITE
    _print(red + "ERR" + white, False)