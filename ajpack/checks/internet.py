import socket, os

def has_internet(host: str = "8.8.8.8", port: int = 53, timeout: int = 3) -> bool:
    """
    Checks if the internet connection is available.
    
    :param host (str): The target ip.
    :param port (int): The target port.
    :param timeout (int): How long to wait if no response.
    :return (bool): If connection to the target.
    """
    try:
        with socket.create_connection((host, port), timeout):
            return True
    except socket.error:
        return False

def ping(targetIp: str) -> bool:
    """
    Pings a target IP address.
    
    :param targetIp (str): The target ip.
    :return (bool): If connection to the target.
    """
    return os.system("ping -c 1" + targetIp) == 0

def check_open_port(hostIp: str, port: int, timeout: float = 5) -> bool:
    """
    Checks if a specific port is opened on the host ip.
    
    :param hostIp (str): Target ip.
    :param port (int): Target port.
    :param timeout (int): How long to wait if no response.
    :return (bool): If port is open.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        return sock.connect_ex((hostIp, port)) == 0
