import socket

def has_internet() -> bool:
    """Checks if the computer ist connected to the internet."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect(("8.8.8.8", 53))
        return True
    except Exception as e:
        return False
    finally:
        sock.close()