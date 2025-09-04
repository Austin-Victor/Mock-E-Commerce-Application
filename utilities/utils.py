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

