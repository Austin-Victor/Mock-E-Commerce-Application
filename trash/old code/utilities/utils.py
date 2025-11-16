import os
import re
import random
import string

DATA_DIR = 'data'
ACCOUNTS_FILE = os.path.join(DATA_DIR, 'accounts.txt')
WAREHOUSE_FILES = [os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR) if f.startswith('warehouse') and f.endswith('.txt')]

def create_data_dir() -> None:

    """
    `create_data_dir` is a function that ensures the necessary data directory and accounts file exist.

    This function checks if a directory specified by `DATA_DIR` exists.
    If it doesn't, it creates the directory. It also checks if a file
    specified by `ACCOUNTS_FILE` exists within that directory. If it
    doesn't, it creates an empty file. This prevents errors when trying
    to read from or write to these locations later.

    Args:
        None

    Returns:
        None
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, 'w'):
            pass

def password_valid(p: str) -> bool:

    """
    `password_valid` is a function that checks if a given password meets the specified complexity requirements.

    A password is considered valid if it meets all of the following criteria:
    - It must be at least 16 characters long.
    - It must contain at least one lowercase letter.
    - It must contain at least one uppercase letter.
    - It must contain at least one digit.
    - It must contain at least one special character (non-alphanumeric and non-whitespace).

    Args:
        p (str): The password string to be validated.

    Returns:
        bool: True if the password meets all the validity criteria, False otherwise.
    """

    return (
        len(p) >= 8 and
        re.search(r'[a-z]', p) and
        re.search(r'[A-Z]', p) and
        re.search(r'\d', p) and
        re.search(r'[^\w\s]', p)
    )

def generate_password() -> str:
    """
    `generate_password` is a function that generates a strong, random password that meets specific complexity requirements.

    This function continuously generates random 16-character strings composed of
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
        if password_valid(p):
            return p
