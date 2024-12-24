import win32api #type:ignore

def drives() -> list[str]:
    """
    :return: All letters of the drivers available.
    """
    return win32api.GetLogicalDriveStrings().split('\000')[:-1]
