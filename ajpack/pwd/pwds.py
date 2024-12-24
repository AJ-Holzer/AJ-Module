import secrets

def gen_pwd(length: int, possibleDigits: str) -> str:
    """
    Generates a pwd with the length and the digits provided.
    
    :param length (int): The length of the password.
    :param possibleDigits (str): The possible digits to use in the password.
    :return (str): A password of the specified length with the possible digits.
    """

    if possibleDigits == "":
        raise ValueError("There are no possible digits defined!")
    elif length < 0:
        raise ValueError("The length of the digits in your password must be grater than 0!")
    
    return "".join(secrets.choice(possibleDigits) for _ in range(length))
