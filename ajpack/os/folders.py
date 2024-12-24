import os

def get_paths() -> dict[str, str]:
    """
    Get all important paths. Returns a dict with the name as keys and the paths as their values.

    names included:
    AppData, Cache, Contacts, Desktop, Documents, Downloads, Drivers, Favorites, Fonts, Help, IME, Inf, InputMethod, Installer, L2Schemas, Links, Local, LocalLow, Logs, Microsoft, Music, Network, OneDrive, PLA, PLA Files, Performance, Pictures, Prefetch, Printers, Program Files, Program Files (x86), ProgramData, Public, Recent, Resources, Roaming, Saved Games, Searches, SendTo, ShellNew, SoftwareDistribution, Speech, Start Menu, Startup, SysWOW64, System32, SystemApps, SystemResources, Tasks, Temp, Users, Videos, Vss, Web, WinSAT, WinSxS, Windows, Windows Defender, Windows Security, WindowsPowerShell, Autostart
    """
    paths: dict[str, str] = {
        "AppData": os.getenv('APPDATA', ''),
        "Cache": os.path.join(os.getenv('LOCALAPPDATA', ''), 'Microsoft', 'Windows', 'INetCache'),
        "Contacts": os.path.join(os.getenv('USERPROFILE', ''), 'Contacts'),
        "Desktop": os.path.join(os.getenv('USERPROFILE', ''), 'Desktop'),
        "Documents": os.path.join(os.getenv('USERPROFILE', ''), 'Documents'),
        "Downloads": os.path.join(os.getenv('USERPROFILE', ''), 'Downloads'),
        "Drivers": os.path.join(os.getenv('SystemRoot', ''), 'System32', 'drivers'),
        "Favorites": os.path.join(os.getenv('USERPROFILE', ''), 'Favorites'),
        "Fonts": os.path.join(os.getenv('SystemRoot', ''), 'Fonts'),
        "Help": os.path.join(os.getenv('SystemRoot', ''), 'Help'),
        "IME": os.path.join(os.getenv('SystemRoot', ''), 'IME'),
        "Inf": os.path.join(os.getenv('SystemRoot', ''), 'Inf'),
        "InputMethod": os.path.join(os.getenv('SystemRoot', ''), 'IME'),
        "Installer": os.path.join(os.getenv('SystemRoot', ''), 'Installer'),
        "L2Schemas": os.path.join(os.getenv('SystemRoot', ''), 'L2Schemas'),
        "Links": os.path.join(os.getenv('USERPROFILE', ''), 'Links'),
        "Local": os.getenv('LOCALAPPDATA', ''),
        "LocalLow": os.path.join(os.getenv('USERPROFILE', ''), 'AppData', 'LocalLow'),
        "Logs": os.path.join(os.getenv('SystemRoot', ''), 'System32', 'LogFiles'),
        "Microsoft": os.path.join(os.getenv('ProgramFiles', ''), 'Microsoft'),
        "Music": os.path.join(os.getenv('USERPROFILE', ''), 'Music'),
        "OneDrive": os.path.join(os.getenv('USERPROFILE', ''), 'OneDrive'),
        "PLA": os.path.join(os.getenv('SystemRoot', ''), 'PLA'),
        "PLA Files": os.path.join(os.getenv('ProgramData', ''), 'Microsoft', 'PLA Files'),
        "Performance": os.path.join(os.getenv('SystemRoot', ''), 'Performance'),
        "Pictures": os.path.join(os.getenv('USERPROFILE', ''), 'Pictures'),
        "Prefetch": os.path.join(os.getenv('SystemRoot', ''), 'Prefetch'),
        "Printers": os.path.join(os.getenv('SystemRoot', ''), 'System32', 'spool', 'PRINTERS'),
        "Program Files": os.getenv('ProgramFiles', ''),
        "Program Files (x86)": os.getenv('ProgramFiles(x86)', ''),
        "ProgramData": os.getenv('ProgramData', ''),
        "Public": os.path.join(os.getenv('PUBLIC', '')),
        "Recent": os.path.join(os.getenv('APPDATA', ''), 'Microsoft', 'Windows', 'Recent'),
        "Resources": os.path.join(os.getenv('SystemRoot', ''), 'Resources'),
        "Roaming": os.path.join(os.getenv('APPDATA', '')),
        "Saved Games": os.path.join(os.getenv('USERPROFILE', ''), 'Saved Games'),
        "Searches": os.path.join(os.getenv('USERPROFILE', ''), 'Searches'),
        "SendTo": os.path.join(os.getenv('APPDATA', ''), 'Microsoft', 'Windows', 'SendTo'),
        "ShellNew": os.path.join(os.getenv('SystemRoot', ''), 'ShellNew'),
        "SoftwareDistribution": os.path.join(os.getenv('SystemRoot', ''), 'SoftwareDistribution'),
        "Speech": os.path.join(os.getenv('ProgramFiles', ''), 'Common Files', 'Microsoft Shared', 'Speech'),
        "Start Menu": os.path.join(os.getenv('APPDATA', ''), 'Microsoft', 'Windows', 'Start Menu'),
        "Startup": os.path.join(os.getenv('APPDATA', ''), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup'),
        "SysWOW64": os.path.join(os.getenv('SystemRoot', ''), 'SysWOW64'),
        "System32": os.path.join(os.getenv('SystemRoot', ''), 'System32'),
        "SystemApps": os.path.join(os.getenv('SystemRoot', ''), 'SystemApps'),
        "SystemResources": os.path.join(os.getenv('SystemRoot', ''), 'Resources'),
        "Tasks": os.path.join(os.getenv('SystemRoot', ''), 'Tasks'),
        "Temp": os.getenv('TEMP', ''),
        "Users": os.path.join(os.getenv('SystemDrive', ''), 'Users'),
        "Videos": os.path.join(os.getenv('USERPROFILE', ''), 'Videos'),
        "Vss": os.path.join(os.getenv('SystemRoot', ''), 'Vss'),
        "Web": os.path.join(os.getenv('SystemRoot', ''), 'Web'),
        "WinSAT": os.path.join(os.getenv('SystemRoot', ''), 'System32', 'WinSAT'),
        "WinSxS": os.path.join(os.getenv('SystemRoot', ''), 'WinSxS'),
        "Windows": os.getenv('SystemRoot', ''),
        "Windows Defender": os.path.join(os.getenv('ProgramFiles', ''), 'Windows Defender'),
        "Windows Security": os.path.join(os.getenv('ProgramFiles', ''), 'Windows Security'),
        "WindowsPowerShell": os.path.join(os.getenv('SystemRoot', ''), 'System32', 'WindowsPowerShell'),
        "Autostart": os.path.join(os.getenv('APPDATA', ''), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    }

    return paths

def parent_folder(file: str = __file__) -> str:
    """
    Gets the parent folder of a specific file.

    :param file: The file. Default is the current file, which is running the script.
    :return: The parent folder.
    """
    return os.path.basename(os.path.dirname(os.path.abspath(file)))
