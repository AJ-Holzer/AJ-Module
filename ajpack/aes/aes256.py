import os
from typing import Optional
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def derive_key_from_string(keyString: str, salt: bytes = b"") -> bytes:
    """
    Derives a 32-byte key from the provided key string using PBKDF2 with SHA256.

    :param keyString (str): The key string to derive the key from.
    :param salt (bytes): An optional salt to use for key derivation (default is an empty byte string).
    :return (bytes): A 32-byte derived key.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        iterations=100000,
        salt=salt,
        backend=default_backend()
    )
    return kdf.derive(keyString.encode('utf-8'))

def decrypt_aes256(encryptedData: bytes, key: str, iv: Optional[bytes] = None) -> str:
    """
    Decrypts the encrypted data with the provided key string.
    
    You could also use an iv, but if you don't it will take the default one. The default iv is 16 zero bytes.

    :param encryptedData (bytes): The data to decrypt (in bytes).
    :param key (str): The key string to be hashed to 32 bytes.
    :param iv (Optional[bytes]): An optional 16 bytes long initialization vector (IV).
    :return (str): Decrypted data as a string.
    """
    # Derive a 32-byte key from the key string
    keyBytes = derive_key_from_string(key)
    
    # If IV is not provided, use a default one (here it's assumed to be 16 bytes for AES)
    if iv is None:
        iv = b'\x00' * 16
    elif len(iv) != 16:
        raise ValueError("IV must be 16 bytes long.")
    
    # Create a cipher object
    cipher = Cipher(algorithms.AES(keyBytes), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Decrypt the data
    decryptedData = decryptor.update(encryptedData) + decryptor.finalize()
    
    # Unpad the decrypted data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpaddedData = unpadder.update(decryptedData) + unpadder.finalize()
    
    # Convert bytes to string and return
    return unpaddedData.decode('utf-8')

def encrypt_aes256(plaintext: str, key: str, iv: Optional[bytes] = None) -> tuple[bytes, bytes]:
    """
    Encrypts the plaintext with the provided key string.

    You could also use an iv, but if you don't, it will take the default one. The default iv value is randomly chosen.

    :param plaintext (str): The plaintext string to encrypt.
    :param key (str): The key string to be hashed to 32 bytes.
    :param iv (Optional[bytes]): An optional 16 bytes long initialization vector (IV).
    :return (tuple[bytes, bytes]): A tuple containing the IV and the encrypted data (both in bytes).
    """
    # Derive a 32-byte key from the key string
    keyBytes = derive_key_from_string(key)
    
    # If IV is not provided, generate a random 16-byte IV
    if iv is None:
        iv = os.urandom(16)
    elif len(iv) != 16:
        raise ValueError("IV must be 16 bytes long.")
    
    # Create a cipher object
    cipher = Cipher(algorithms.AES(keyBytes), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Pad the plaintext to be compatible with AES block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padderData = padder.update(plaintext.encode('utf-8')) + padder.finalize()
    
    # Encrypt the padded data
    encryptedData = encryptor.update(padderData) + encryptor.finalize()
    
    # Return the IV and the encrypted data
    return iv, encryptedData
