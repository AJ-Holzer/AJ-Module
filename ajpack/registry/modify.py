import winreg

def write_to_registry(regPath: str, regKey: str, value: str) -> None:
    """
    Writes a value to the Windows registry.

    
    :param regPath (str): The path to the registry key (e.g. "Software\\MyApp")
    :param regKey (str): The name of the registry key to write to
    :param (str): The value to write to the registry key
    :return (None):
    """
    try:
        # Split the registry path into the root key and the subkey
        root_key, subkey = regPath.split('\\', 1)

        # Convert the root key to a winreg constant
        root_key_const = getattr(winreg, f'HKEY_{root_key.upper()}')

        # Create the key if it doesn't exist
        key = winreg.CreateKeyEx(root_key_const, subkey, 0, winreg.KEY_WRITE)

        # Write the value to the registry key
        winreg.SetValueEx(key, regKey, 0, winreg.REG_SZ, value)

        # Close the registry key
        winreg.CloseKey(key)

    except WindowsError as e:
        raise WindowsError(f"Error writing to registry: {e}")
