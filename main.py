from utils import create_data_dir
from data import load_inventory
from auth import sign_in, sign_up
from wallet import fund_wallet
from purchase import purchase
from state import user

def run(user: list) -> None:
    """
    `run` is a function that presents the main operational menu to a logged-in user and handles their choices.

    This function enters a loop that displays options for a logged-in user:
    Fund Wallet: Calls the `fund_wallet` function to allow the user to add money to their account.
    Purchase: Calls the `purchase` function to allow the user to browse and buy items.
    Exit: Breaks out of the run menu loop, returning control to the `main` function.

    Args:
        user (list): A list representing the currently logged-in user's account information.
                     This list is passed to `fund_wallet` and `purchase` functions.

    Returns:
        None: This function does not return any value. It continues to loop
              until the user chooses to exit.
    """

    while True:
        print("\nRun Menu:\n1. Fund Wallet\n2. Purchase\n3. Exit")
        choice = input("Choice: ")
        if choice == '1':
            fund_wallet(user)
        elif choice == '2':
            purchase(user)
        elif choice == '3':
            break
        else:
            print("Invalid input.")

def main() -> None:
    """
     `main` function initializes the application and manages the main user flow.

    This is the entry point of the application. It performs the following steps:
      Calls `create_data_dir()` to ensure the necessary data directory and accounts file exist.
      Calls `load_inventory()` to load the available items and their prices into memory.
      Enters a continuous loop to present the main welcome menu to the user:
        -   **Sign In:** Calls `sign_in()` to authenticate an existing user. If successful,
            it then calls `run()` to start the shopping session for that user.
        -   **Sign Up:** Calls `sign_up()` to allow a new user to create an account.
        -   **Exit:** Breaks out of the main loop, terminating the application.

    This function orchestrates the overall flow of the application, from setup
    to user interaction and session management.

    Args:
        None

    Returns:
        None: This function runs indefinitely until the user chooses to exit the application.
    """
    create_data_dir()
    load_inventory()
    while True:
        print("\nWelcome")
        print("1. Sign In")
        print("2. Sign Up")
        print("3. Exit")
        choice = input("Choice: ")
        if choice == '1':
            logged_in_user = sign_in()
            if logged_in_user:
                run(logged_in_user)
        elif choice == '2':
            sign_up()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()