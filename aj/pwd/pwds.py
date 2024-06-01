import random

def gen_pwd(count:int, possible_digits:str) -> str:
    """Generates a pwd with the count and the digits provided."""
    
    if count > 0:
        digits = []
        pwd = ""

        for digit in possible_digits:
            digits.append(str(digit))

        for _ in range(count):
            pwd += str(random.choice(digits))

        return pwd
    else:
        raise ValueError("The count of the digits in your password must be grater than 0!")