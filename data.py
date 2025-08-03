from utils import ACCOUNTS_FILE, WAREHOUSE_FILES
from state import inventory

def load_inventory():
    """
    `load_inventory` is a function that loads inventory items and their prices from predefined warehouse files into a global inventory dictionary.

    This function first clears any existing items in the global `inventory` dictionary.
    It then iterates through a list of `WAREHOUSE_FILES` (expected to be global).
    For each file, it reads the content, which is expected to be a semicolon-separated
    string of "item_name:price" pairs. It parses these pairs and populates the
    `inventory` dictionary with item names as keys and their float prices as values.
    Empty lines or malformed entries are gracefully skipped.

    Args:
        None: This function uses the global `inventory` dictionary and `WAREHOUSE_FILES` list.

    Returns:
        None: This function modifies the global `inventory` dictionary in place.
    """
    inventory.clear()
    for file in WAREHOUSE_FILES:
        with open(file, 'r') as f:
            content = f.read().strip()
            if content:
                items = content.split(';')
                for item in items:
                    if ':' in item:
                        name, price = item.split(':')
                        inventory[name.strip()] = float(price.strip())

def load_accounts() -> list:
    """
    `load_accounts` is a function that loads user account data from the accounts file into a list of lists.

    This function reads each line from the `ACCOUNTS_FILE` (expected to be a global path).
    Each non-empty line is treated as a comma-separated string representing a user's
    account details (e.g., username, password, account_number, balance). These
    details are split by commas and appended as a sublist to a main `accounts` list.

    Args:
        None: This function uses the global `ACCOUNTS_FILE` path.

    Returns:
        list: A list of lists, where each inner list represents a user's account
              details (e.g., `[['user1', 'pass1', '123', '1000.0'], ...]`).
              Returns an empty list if the file is empty or does not exist.
    """
    accounts = []
    with open(ACCOUNTS_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                accounts.append(line.split(','))
    return accounts

def save_accounts(accounts: list) -> None:
    """
    `save_accounts` is a function that saves user account data from a list of lists back to the accounts file.

    This function takes a list of `accounts`, where each inner list represents
    a user's account details. It writes these details back to the `ACCOUNTS_FILE`
    (expected to be a global path), with each account on a new line and its
    details joined by commas. This effectively overwrites the existing content
    of the accounts file with the current state of the `accounts` list.

    Args:
        accounts (list): A list of lists, where each inner list contains
                         the comma-separated account details for a user.

    Returns:
        None: This function writes data to a file and does not return any value.
    """
    with open(ACCOUNTS_FILE, 'w') as f:
        for acc in accounts:
            f.write(','.join(acc) + '\n')

def find_user(identifier:str) -> list | None:
    """
    `find_user` is a function that searches for a user account by either username or email.

    This function iterates through all accounts loaded from the accounts file
    (by calling `load_accounts()`). It attempts to find a user whose username
    (index 0) or email (index 1) matches the provided `identifier`.

    Args:
        identifier (str): The username or email to search for.

    Returns:
        list or None: Returns the list representing the found user's account
                      details if a match is found. Returns `None` if no user
                      with the given identifier is found.
    """
    for acc in load_accounts():
        if acc[0] == identifier or acc[1] == identifier:
            return acc
    return None
