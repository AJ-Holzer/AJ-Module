import msvcrt

def wait(msg: str = "Press any key to continue...") -> None:
    """Wait for the user to press Enter."""
    print(msg)
    msvcrt.getch()