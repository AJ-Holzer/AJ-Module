import subprocess

def run_on_vm() -> bool:
    """Returns if the current script is running on a vm."""
    blacklist = [
    "vm",
    "black",
    "box",
    "vbox",
    ]
    output = str(subprocess.check_output("wmic bios")).lower()

    for item in blacklist:
        if item.lower() in output:
            return True
        
    return False