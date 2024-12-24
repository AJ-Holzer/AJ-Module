import subprocess

from ..useful.convert import remove_duplicates

def run_on_vm(additionalBlacklist: list[str] = []) -> bool:
    """
    Checks if current script is running on a vm.
    
    :param additionalBlacklist (list[str]): Some additionional keywords for a vm from you side.
    :return (bool): If running on vm
    """
    blacklist: list[str] = [
    "vm",
    "black",
    "box",
    "vbox",
    "sand",
    ] + additionalBlacklist

    return any(str(item).lower() in str(subprocess.check_output("wmic bios")).lower() for item in remove_duplicates(blacklist))
