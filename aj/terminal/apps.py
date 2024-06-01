import msvcrt

def wait(msg: str = "Press any key to continue...") -> None:
    """Waits for the user to press a key."""
    print(msg)
    msvcrt.getch()