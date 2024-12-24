import socket
import time
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey

# Custom functions
from ..rsa.rsa import encrypt_rsa, decrypt_rsa

endIndicatorDefault = "/end/"

def send(
        serverSocket: socket.socket,
        msg: str,
        endIndicator: str = endIndicatorDefault,
        chunkSize: int = 1000,
        delay: float = 0
) -> None:
    """
    Sends a message to the server. (no encryption)

    :param serverSocket (socket.socket): The socket object.
    :param msg (str): The message to send.
    :param endIndicator (str): The end str to be sent, to indicate that the message is done.
    :param chunkSize (int): The size of each chunk to send.
    :param delay (float): The time to wait before sending a new chunk.
    """
    try:
        # Split the message into chunks
        chunks: list[str] = [msg[i:i+chunkSize] for i in range(0, len(msg), chunkSize)]

        for chunk in chunks:
            if chunk:
                # Send chunk
                serverSocket.send(chunk.encode())
                # Wait to prevent bugs
                time.sleep(delay)
        
        # Send end indicator
        serverSocket.send(endIndicator.encode())
    except Exception as e:
        raise Exception(f"There was an unexpected error while sending the message to the server. --> {e}")

def rcv(
        serverSocket: socket.socket,
        endIndicator: str = endIndicatorDefault,
        bufSize: int = 1024
) -> str:
    """
    Receives a message of the server. (no encryption)

    :param serverSocket (socket.socket): The socket object.
    :param endIndicator (str): The end str to be received, to indicate that the message is done. (must be the same of sending)
    :param bufSize (int): The buf size of the socket object.
    :return feedback (str): The received message of the server.
    """
    try:
        feedback: str = ""

        while True:
            feedbackTmp: str = serverSocket.recv(bufSize).decode()
            if feedbackTmp:
                if feedbackTmp != endIndicator:
                    feedback += feedbackTmp
                else:
                    break
            
        return feedback
    except Exception as e:
        raise Exception(f"There was an unexpected error while receiving the data from the server. --> {e}")

def send_rsa(
        serverSocket: socket.socket,
        msg: str,
        serverPublicKey: RSAPublicKey,
        clientPrivateKey: RSAPrivateKey,
        endIndicator: str = endIndicatorDefault,
        chunkSize: int = 1000,
        delay: float = 0
) -> None:
    """
    Sends a message (encrypted with rsa) to the server.

    :param serverSocket (socket.socket): The socket object.
    :param msg (str): The message to be sent.
    :param serverPublicKey (RSAPublicKey): The server's public key.
    :param clientPrivateKey (RSAPrivateKey): The client's private key.
    :param endIndicator (str): The end str to be received, to indicate that the message is done.
    :param chunkSize (int): The chunk size of the message.
    :param delay (float): The delay between chunks.
    """
    # Split the message into chunks
    chunks: list[str] = [msg[i:i+chunkSize] for i in range(0, len(msg), chunkSize)]

    for chunk in chunks:
        if chunk:
            encryptedMsg: bytes = encrypt_rsa(serverPublicKey, clientPrivateKey, chunk)
            # Send chunk
            serverSocket.send(encryptedMsg)
            time.sleep(delay)

    # Send end indicator
    serverSocket.send(encrypt_rsa(serverPublicKey, clientPrivateKey, endIndicator))

def rcv_rsa(
        serverSocket: socket.socket,
        clientPrivateKey: RSAPrivateKey,
        serverPublicKey: RSAPublicKey,
        endIndicator: str = endIndicatorDefault,
        bufSize: int = 1024
) -> str:
    """
    Receives a message (encrypted with rsa) from the server.

    :param serverSocket (socket.socket): The socket object.
    :param clientPrivateKey (RSAPrivateKey): The client's private key.
    :param serverPublicKey (RSAPublicKey): The server's public key.
    :param endIndicator (str): The end str to be received, to indicate that the message is done.
    :param bufSize (int): The buffer size.
    :return feedback (str): The received (decrypted) message of the server.
    """
    try:
        feedback: str = ""

        while True:
            feedbackTmp: bytes = serverSocket.recv(bufSize)
            decryptedFeedbackTmp: str = decrypt_rsa(serverPublicKey, clientPrivateKey, feedbackTmp)
            if decryptedFeedbackTmp:
                if decryptedFeedbackTmp != endIndicator:
                    feedback += decryptedFeedbackTmp
                else:
                    break

        return feedback
    except Exception as e:
        raise Exception(f"There was an unexpected error while receiving the data from the server. --> {e}")
