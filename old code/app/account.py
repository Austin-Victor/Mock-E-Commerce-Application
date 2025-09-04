import bcrypt
from app import data
from utilities.utils import password_valid

def delete_account(user:list) -> bool:
    """
    `delete_account` is a function that handles the process of deleting a user's account.

    This function prompts the user for confirmation before proceeding with account deletion.
    If the user confirms, it loads all existing accounts, filters out the current user's
    account based on their username, and then saves the updated list of accounts back
    to the accounts file. A success message is printed, and True is returned.
    If the user cancels, a cancellation message is printed, and False is returned.

    Args:
        user (list): A list representing the currently logged-in user's account information,
                     where `user[0]` is the username.

    Returns:
        bool: True if the account was successfully deleted, False otherwise (if cancelled).
    """
    confirm = input("Are you sure you want to delete your account? (y/n): ").lower()
    if confirm == 'y':
        accounts = data.load_accounts()
        accounts = [acc for acc in accounts if acc[0] != user[0]]
        data.save_accounts(accounts)
        print("Account deleted successfully.")
        return True
    print("Account deletion cancelled.")
    return False

def change_password(user:list) -> None:
    """
    `change_password` is a function that allows a logged-in user to change their account password.

    This function prompts the user to enter their current password for verification.
    It uses `bcrypt.checkpw` to securely compare the entered password with the
    hashed password stored in the `user` object. If the current password is
    incorrect, an error message is displayed, and the function exits.

    If the current password is correct, the user is prompted to enter a new password.
    This new password is then validated using `password_valid()` to ensure it meets
    the required complexity. The process loops until a valid new password is provided.

    The new password is then hashed using `bcrypt.hashpw` and `bcrypt.gensalt`,
    and the user's account in the loaded `accounts` list is updated with this new hash.
    Finally, the updated `accounts` list is saved back to storage.

    Args:
        user (list): A list representing the currently logged-in user's account information,
                     where `user[0]` is the username and `user[2]` is the hashed password.

    Returns:
        None: This function modifies the user's password in the stored accounts data
              and prints status messages. It does not return any value.
    """
    old_password = input("Enter current password: ")
    if not bcrypt.checkpw(old_password.encode('utf-8'), user[2].encode('utf-8')):
        print("Incorrect current password.")
        return

    new_password = input("Enter new password: ")
    while not password_valid(new_password):
        print("Invalid password format. Try again.")
        new_password = input("Enter new password: ")

    hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    accounts = data.load_accounts()
    for acc in accounts:
        if acc[0] == user[0]:
            acc[2] = hashed
    data.save_accounts(accounts)
    print("Password changed successfully.")
