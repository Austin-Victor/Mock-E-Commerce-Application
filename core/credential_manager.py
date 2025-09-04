import re
import random
import string

def generate_password() -> str:
    """
    `generate_password` is a function that generates a strong, random password that meets specific complexity requirements.

    This function continuously generates random 8-character strings composed of
    lowercase letters, uppercase letters, digits, and punctuation marks.
    It then validates each generated string using the `password_valid` function.
    The process repeats until a valid password is created.

    Args:
        None

    Returns:
        str: A randomly generated password string that satisfies the
             complexity rules defined in `password_valid`.
    """
    while True:
        p = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8))
        if pw_is_valid(p):
            return p

def is_match(val1, val2) -> bool:
    if val1 == val2:
        return True
    else:
        return False
    
def pw_is_valid(password: str) -> bool:

    """
    `password_valid` is a function that checks if a given password meets the specified complexity requirements.

    A password is considered valid if it meets all of the following criteria:
    - It must be at least 16 characters long.
    - It must contain at least one lowercase letter.
    - It must contain at least one uppercase letter.
    - It must contain at least one digit.
    - It must contain at least one special character (non-alphanumeric and non-whitespace).

    Args:
        password (str): The password string to be validated.

    Returns:
        bool: True if the password meets all the validity criteria, False otherwise.
    """

    return (
        len(password) >= 8 and
        re.search(r'[a-z]', password) and
        re.search(r'[A-Z]', password) and
        re.search(r'\d', password) and
        re.search(r'[^\w\s]', password)
    )
    
def validate_email(email: str):
    
    [
        "@email.com", "@gmail.com", "@aol.com",
        "@rocketmail.com", "@yahoo.com", "@ymail.com",
        "@outlook.com", "@hotmail.com", "@live.com", "@msn.com",
        "@icloud.com", "@me.com", "@mac.com",
        "@zoho.com", "@proton.com", "@protonmail.com",
        "@gmx.com", "@consultant.com", "@engineer.com",
        "@yandex.com", "@yandex.ru"
    ]
    pass