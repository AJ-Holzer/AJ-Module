import socket, os

def has_internet(host: str = "8.8.8.8", port: int = 53, timeout: int = 3) -> bool:
    """Checks if the internet connection is available."""
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False

def ping(target_ip: str) -> str:
    """Pings a target IP address and returns the result."""
    response: str = str(os.system("ping " + target_ip))
    return response

def check_open_port(host_ip: str, port: int, timeout: float = 5) -> bool:
    """Checks if a specific port is opened on the host ip."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((host_ip, port))
        return result == 0