import os, shutil, winshell #type:ignore
from win32com.client import Dispatch #type:ignore

def create_shortcut(
        name: str = "Shortcut",
        target_path: str = "",
        description: str | None = None,
        icon_path: str | None = None,
        arguments: str | None = None,
        shortcut_path: str = os.path.join(os.path.expanduser("~"), "Desktop")
) -> bool:
    """
    Creates a shortcut.

    :param name: The name of the shortcut.
    :param target_path: The target for the shortcut.
    :param description: The description for the shortcut.
    :param icon_path: The icon for the shortcut.
    :param arguments: The arguments for the shortcut.
    :param shortcut_path: The path where the shortcut should be created.
    :return: True if the shortcut was created successfully, False otherwise.
    """

    shortcut_path = os.path.join(shortcut_path, f"{name}.lnk")
    
    if os.path.exists(shortcut_path):
        return False

    try:
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.TargetPath = target_path
        if arguments:
            shortcut.Arguments = arguments
        if description:
            shortcut.Description = description
        if icon_path:
            shortcut.IconLocation = icon_path
        
        shortcut.save()
        return True
    except Exception as e:
        raise Exception(f"There was an unexpected error. --> {e}")
