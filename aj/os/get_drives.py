import win32api

def drives() -> list[str]:
    """Gets all letters of the drivers available."""

    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]

    return drives