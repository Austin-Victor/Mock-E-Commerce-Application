import utils
import data
import bcrypt

def sign_up() -> None:
    """
    `sign_up` is a function that registers a new user account by collecting username, email, and password.

    This function prompts the user to enter a desired username and email.
    It first checks if the entered username or email already exists in the
    system using `find_user()`. If either exists, an error message is displayed,
    and the sign-up process is aborted.

    The user then has the option to either have a strong password automatically
    generated using `generate_password()` or to manually enter a password.
    If a manual password is chosen, it is validated against complexity rules
    using `password_valid()` until a valid one is provided.

    Upon successful collection of valid credentials, the new account (username,
    email, password, and an initial balance of 0.00) is appended to the
    `data/accounts.txt` file.

    Args:
        None: This function interacts directly with the user via input/print
              and writes to a file.

    Returns:
        None: This function does not return any value. It either creates an
              account or prints an error message.
    """
    username = input("Enter username: ").title()
    email = input("Enter email: ")
    if data.find_user(username) or data.find_user(email):
        print("Username or Email already exists.")
        return

    choice = input("Generate password? (y/n): ").lower()
    if choice == 'y':
        password = utils.generate_password()
        print(f"Generated Password: {password}")
    else:
        password = input("Enter password: ")
        while not utils.password_valid(password):
            print("Invalid password format. Try again.")
            password = input("Enter password: ")
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    with open('data/accounts.txt', 'a') as f:
        f.write(f"{username},{email},{hashed_pw.decode()},0.00\n")
    print("Account created successfully!")

def sign_in() -> list | None:
    """
    `sign_in` is a function that authenticates a user by verifying their username/email and password.

    This function prompts the user to enter either their username or email.
    It then uses `find_user()` to retrieve the corresponding account details.
    If no account is found, an error message is displayed.

    If an account is found, the user is prompted for their password. The entered
    password is compared against the stored password for the retrieved account.
    If the passwords match, a welcome message is displayed, and the user's
    account data is returned. Otherwise, an incorrect password message is shown.

    Args:
        None: This function interacts directly with the user via input/print.
              It assumes `find_user` is available to retrieve account data.

    Returns:
        list or None: If authentication is successful, returns a list containing
                      the user's account details (e.g., `[username, email, password, balance]`).
                      Returns `None` if the account is not found or the password is incorrect.
    """
    identifier = input("Enter username or email: ").title()
    acc = data.find_user(identifier)
    if not acc:
        print("Account not found.")
        return None
    i = 0
    while i < 3:
        i = i + 1
        password = input("Enter password: ")
        if not bcrypt.checkpw(password.encode(), acc[2].encode()):
            print(f"Incorrect password. {3-i} more tries available")
            if i == 3:
                return None
            continue
        break
    print(f"Welcome, {acc[0]}!")
    return acc
