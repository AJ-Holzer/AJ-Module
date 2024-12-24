import socket
import psutil  #type:ignore

def get_local_ip() -> str:
    """
    Gets the local IP on a Windows computer.

    :return ip (str): The IP. or "NOIP" if no IP found.
    """
    # Check both Ethernet and Wi-Fi interfaces
    for interface in ['Ethernet', 'WiFi']:
        ipAddresses = [addr.address for addr in psutil.net_if_addrs().get(interface, []) if addr.family == socket.AF_INET]
        if ipAddresses:
            return ipAddresses[0]
        
    return "NOIP"

# Test
if __name__ == "__main__":
    print(get_local_ip())
