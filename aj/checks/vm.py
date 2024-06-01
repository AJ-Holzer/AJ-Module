import subprocess

def run_on_vm(additional_blacklist: list[str]) -> bool:
    """Returns if the current script is running on a vm."""
    blacklist: list[str] = [
    "vm",
    "black",
    "box",
    "vbox",
    ]

    for item in additional_blacklist: blacklist.append(item)

    output: str = str(subprocess.check_output("wmic bios")).lower()

    for item in blacklist:
        if item.lower() in output:
            return True
        
    return False