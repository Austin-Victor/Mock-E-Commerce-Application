from data import load_accounts, save_accounts

def fund_wallet(user: list) -> None:
    """
    `fund_wallet` is a function that funds a user's wallet with a selected amount.

    This function presents the user with a list of predefined amounts to
    add to their wallet. Upon selection, the chosen amount is added to
    the user's current balance, and the updated balance is saved to the
    accounts data.

    Args:
        user (list): A list representing the user's account information.
                     It is expected to be in the format:
                     [username, password, account_number, balance, ...]
                     where index 3 holds the current balance as a string.

    Returns:
        None: This function modifies the user's balance in place and
              saves the updated accounts data. It does not return any value.
    """
    print("\nSelect amount to fund:")
    options = [10000, 20000, 50000, 100000]
    for i, amount in enumerate(options, 1):
        print(f"{i}. NGN {amount}")
    choice = int(input("Choice: "))
    if 1 <= choice <= len(options):
        user[3] = str(float(user[3]) + options[choice - 1])
        accounts = load_accounts()
        for acc in accounts:
            if acc[0] == user[0]:
                acc[3] = user[3]
        save_accounts(accounts)
        print("Wallet funded successfully!")
