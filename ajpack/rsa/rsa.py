from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey

def gen_private_key(key_size: int = 4096) -> RSAPrivateKey:
    """
    Generate a new RSA private key.

    Classical computer:
        - 2048-bit RSA:  Estimated at 300 trillion years.
        - 4096-bit RSA:  Roughly 6 x 10^48 years.
        - 8192-bit RSA:  Far longer than the age of the universe.
        - 16384-bit RSA: Impractical to break, estimated in a time range that defies current computational capabilities.
        - 32768-bit RSA: Effectively infinite. Unbreakable within any realistic timeframe.

    Quantum computers:
        - 2048-bit RSA:  Assumed breakable in hours to days.
        - 4096-bit RSA:  Potentially breakable in weeks to months.
        - 8192-bit RSA:  Might take years or decades.
        - 16384-bit RSA: Could require centuries.
        - 32768-bit RSA: Likely in the range of thousands of years.

    Summary:
        - If you need encryption that is secure against classical computers, this is a suitable choice.
        - For encryption that can withstand quantum computer attacks, consider an alternative.
        - Generating keys longer than 16,000 bytes can be extremely time-consuming. (I'm serious.)

    :param key_size: Size of the RSA key to generate, default is 4096 bits.
    :return: The generated RSA private key.
    """
    try:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )
        return private_key
    except Exception as e:
        raise ValueError(f"Failed to generate private key: {e}")

def gen_public_key(private_key: RSAPrivateKey) -> RSAPublicKey:
    """
    Generate the corresponding public key from a private key.

    :param private_key: The RSA private key.
    :return: The corresponding RSA public key.
    """
    if not isinstance(private_key, RSAPrivateKey):
        raise ValueError("Invalid private key")
    public_key = private_key.public_key()
    return public_key

def encrypt_rsa(public_key: RSAPublicKey, private_key: RSAPrivateKey, plaintext: str) -> bytes:
    """
    Encrypt a message using the RSA public key and sign it with the private key.

    :param public_key: The RSA public key to use for encryption.
    :param private_key: The RSA private key to use for signing.
    :param plaintext: The plaintext message to encrypt.
    :return: The encrypted and signed ciphertext.
    """
    if not isinstance(public_key, RSAPublicKey):
        raise ValueError("Invalid public key")
    if not isinstance(private_key, RSAPrivateKey):
        raise ValueError("Invalid private key")
    try:
        plaintext_bytes = plaintext.encode()
        ciphertext = public_key.encrypt(
            plaintext_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        signature = private_key.sign(
            ciphertext,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return ciphertext + signature
    except Exception as e:
        raise ValueError(f"Failed to encrypt: {e}")

def decrypt_rsa(public_key: RSAPublicKey, private_key: RSAPrivateKey, ciphertext: bytes) -> str:
    """
    Decrypt a message using the RSA private key and verify the signature.

    :param public_key: The RSA public key to use for verification.
    :param private_key: The RSA private key to use for decryption.
    :param ciphertext: The ciphertext message to decrypt.
    :return: The decrypted plaintext.
    """
    if not isinstance(public_key, RSAPublicKey):
        raise ValueError("Invalid public key")
    if not isinstance(private_key, RSAPrivateKey):
        raise ValueError("Invalid private key")
    try:
        signature_length = 256  # Assuming 2048-bit RSA key with SHA-256 hash
        ciphertext_length = len(ciphertext) - signature_length
        encrypted_data = ciphertext[:ciphertext_length]
        signature = ciphertext[ciphertext_length:]
        public_key.verify(
            signature,
            encrypted_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        plaintext = private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext.decode()
    except Exception as e:
        raise ValueError(f"Failed to decrypt: {e}")