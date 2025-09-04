from core import database_manager as dbm
import random
import bcrypt
#import utils

class User:
    """
    Handles all user activities and attributes. It creates and stores users in a database,
    Handles session mangement for logging in.

    Methods: `sign_up`, `sign_in`.
    
    Attributes: `f_name`, `l_name`, `account_num`, `email`, `password` and `account_balance`

    Args:
        None:

    Returns:
        str: A randomly generated password string that satisfies the
             complexity rules defined in `password_valid`.
    """
    
    def __init__(self, f_name: str, l_name: str, account_num: str, email: str, password: str, account_balance: float, is_admin: bool = False):
        self.f_name = f_name
        self.l_name = l_name
        self.account_num = account_num
        self.email = email
        self.password = password
        self.account_balance = account_balance
        self.is_admin = is_admin
    
    @staticmethod
    def sign_up(f_name: str, l_name: str, email: str, password: str) -> str:
        
        """
        `sign_up` is a function that registers a new user account by collecting first name, last name, email, and password.

        It first generates an account number, then checks if the account number already exists in the
        database using `database_manager.value_exists()`. If it exists, another account number is generated and checked,
        this process continues repeatedly until a unique account number is found.

        The password is then hashed using bcrypt.

        After succesful account number generation and password hashing, the new account (first name, last name
        email, and password) is appended to the
        `data/users.db` database using `database_manager.append_to_usersdb()`.

        Args:
            f_name (str): users first name.
            l_name (str): users last name.
            email (str): users email address.
            password (str): users password.

        Returns:
            str: a string depending on the result of creation
        """
        
        while True:
            account_num = "".join([str(random.randint(0, 9)) for _ in range(10)])
            
            if dbm.value_exists(account_num, "account_number", dbm.USERS):
                continue
            else:
                break
        
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return dbm.appendto_usersdb(f_name.title(), l_name.title(), account_num, email, hashed_pw)
    
    @classmethod
    def sign_in(cls, account_number: str, pw: str) -> object|bool:
        
        """
        `sign_in` is a function that authenticates a user by verifying their account number and password.

        This function takes an account number and password as its arguments.
        It then uses `database_manger.value_exists()` to retrieve the corresponding account details from the user database.
        If no account is found, `False` is returned.

        If an account is found, the claimed password is hashed and compared with the stored hashed password of the retrieved account.
        If the passwords match, an instance of the `User` class is returned with the account details as its attributes.
        Otherwise, `False` is returned.

        Args:
            account_number: 
                the account number of the account
                
            password: 

        Returns:
            Object:
                If authentication is successful, returns an instance of the User class.
                Returns `False` if the account is not found or the password is incorrect.
        """
        
        acc_details: tuple = dbm.value_exists(account_number, "account_number", dbm.USERS)
        if acc_details:
            hashed_pw = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
            if hashed_pw == acc_details[5].encode():
                return cls(
                    acc_details[1],
                    acc_details[2],
                    acc_details[3],
                    acc_details[4],
                    acc_details[5],
                    acc_details[6],
                    acc_details[7]
            )
            else:
                print("Invalid password")
                return False
        else:
            return False