import hashlib
from typing import Any

_hashes: dict[str, Any] = {
    'md5': hashlib.md5(),
    'sha1': hashlib.sha1(),
    'sha256': hashlib.sha256(),
}

def get_file_etag(file_path: str) -> dict[str, str]:
    """
    Get the ETag of a file.
    
    :param file_path (str): The file to check.
    :return (dict[str, str]): A dictionary with the hash name and the ETag.
    """
    
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            for _, hash_func in _hashes.items():
                hash_func.update(chunk)

    return {hash_name: hash_func.hexdigest() for hash_name, hash_func in _hashes.items()}

def get_str_etag(txt: str) -> dict[str, str]:
    """
    Get the ETag of a string.

    :param txt (str): The string to check.
    :return (dict[str, str]): A dictionary with the hash name and the ETag.
    """
    # Update the hashes with the string bytes
    for _, hash_func in _hashes.items():
        hash_func.update(txt.encode('utf-8'))

    # Return a dictionary with the hash names and their corresponding ETags
    return {hash_name: hash_func.hexdigest() for hash_name, hash_func in _hashes.items()}

def get_bytes_etag(data: bytes) -> dict[str, str]:
    """
    Get the ETag of a bytes object.

    :param data (bytes): The bytes object to check.
    :return (dict[str, str]): A dictionary with the hash name and the ETag.
    """
    # Update the hashes with the bytes
    for _, hash_func in _hashes.items():
        hash_func.update(data)

    # Return a dictionary with the hash names and their corresponding ETags
    return {hash_name: hash_func.hexdigest() for hash_name, hash_func in _hashes.items()}

# Test
if __name__ == "__main__":
    print(get_bytes_etag(b"Hello")["sha256"])
