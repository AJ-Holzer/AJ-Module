import sys
from pystray import Icon, Menu, MenuItem  #type:ignore
from PIL import Image
from typing import Callable, Any

def show_status_icon(
        iconPath: str,
        title: str,
        funcArgs: tuple,
        customExitFunction: Callable|None = None,
        exit: bool = False,
        addMenuItems: list[MenuItem] = [],
        useDefault: bool = True
    ) -> None:
    """
    Show a status icon in the system tray.

    :param iconPath (str): The image path to use as icon.
    :param title (str): The title of the icon.
    :param funcArgs (tuple): Arguments to pass to the custom exit function if provided.
    :param customExitFunction (Callable|None): A custom function to call on exit; if None, the default exit behavior is used.
    :param exit (bool): A flag indicating whether to exit the application.
    :param addMenuItems (list[pystray.MenuItem]): A list of additional menu items to add to the default list.
    :param useDefault (bool): Whether to use the default menu items or not. (addMenuItems won't be removed)
    """
    # Load the icon image
    image = Image.open(iconPath)

    # Create the icon
    icon = Icon(title, image, title, Menu())

    # Create a menu
    def exit_icon():
        icon.stop()

        if customExitFunction:
            customExitFunction(*funcArgs)

    if useDefault:
        menuItems = addMenuItems + [
            MenuItem("EXIT", exit_icon)
        ]
    else:
        menuItems = addMenuItems

    icon.menu = Menu(*menuItems)

    # Run the icon in the background
    icon.run()

    if exit:
        sys.exit(0)
