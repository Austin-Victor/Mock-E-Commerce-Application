import sqlite3  
 
USERS = "databases/users.db"
INVENTORY = "databases/inventory.db"
WAREHOUSE = "databases/warehouse.db"

def create_users_db():
    
    """
    Create the users database table if it does not already exist.

    This function connects to the SQLite database defined by the global
    constant `USERS`, and creates a table named `users` with the following schema:

        - id (INTEGER, PRIMARY KEY, AUTOINCREMENT): Unique identifier for each user.
        - f_name (TEXT, NOT NULL): First name of the user.
        - l_name (TEXT, NOT NULL): Last name of the user.
        - account_number (TEXT, UNIQUE, NOT NULL): Unique account number.
        - email (TEXT, UNIQUE, NOT NULL): User's email address.
        - password (TEXT, NOT NULL): User's password (should be stored as a hash).
        - account_bal (REAL, DEFAULT 0): User's account balance.
        - is_admin (BOOLEAN, DEFAULT 0): Flag indicating whether the user is an administrator.

    If the table already exists, this function does nothing. Changes are committed
    to the database, and the connection is closed before returning.

    Returns:
        None
    """

    users_conn = sqlite3.connect(USERS)
    
    cursor = users_conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            f_name TEXT NOT NULL,
            l_name TEXT NOT NULL,
            account_number TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            account_bal REAL DEFAULT 0,
            is_admin BOOLEAN DEFAULT 0
        )
    ''')
    
def create_warehouse_db():
    
    """
    Create the warehouse database table if it does not already exist.

    This function connects to the SQLite database defined by the global
    constant `WAREHOUSE`, and creates a table named `warehouse` with the
    following schema:

        - id (INTEGER, PRIMARY KEY, AUTOINCREMENT): Unique identifier for each product.
        - product_name (TEXT, NOT NULL): Name of the product.
        - price (REAL, NOT NULL): Price of the product.
        - category (TEXT, DEFAULT NULL): Optional category the product belongs to.

    If the table already exists, this function does nothing. Changes are committed
    to the database, and the connection is closed before returning.

    Returns:
        None
    """

    
    users_conn = sqlite3.connect(WAREHOUSE)
    
    cursor = users_conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS warehouse (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT DEFAULT NULL
        )
    ''')
    
    users_conn.commit()
    users_conn.close()

def appendto_usersdb(f_name: str, l_name: str, account_num: str, email: str, password: str, account_balance: float = 0, is_admin: bool = False) -> str:

    """
    Insert a new user into the users database.

    Connects to the SQLite database defined by the global constant `USERS`
    and attempts to add a new record into the `users` table with the provided
    details. The function uses parameterized queries to prevent SQL injection.

    Args:
        f_name (str): First name of the user.
        l_name (str): Last name of the user.
        account_num (str): Unique account number for the user.
        email (str): Unique email address for the user.
        password (str): User's password (should be stored as a hashed value).
        account_balance (float, optional): Initial account balance. Defaults to 0.
        is_admin (bool, optional): Whether the user is an administrator.
            Defaults to False.

    Returns:
        str: 
            - On success: A string in the format
              `"True,<f_name>,<l_name>,<email>,<account_num>"`.
            - On failure: An error message extracted from the exception
              (e.g., `"UNIQUE constraint failed"` if account number or email
              already exists).

    Raises:
        None explicitly. Exceptions are caught and returned as strings.
    """

    
    conn = sqlite3.connect(f"{USERS}")
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO users (f_name, l_name, account_number, email, password, account_bal, is_admin)
        VALUES (?, ?, ?, ?, ?, ?, ?)              
        ''', (f"{f_name}",f"{l_name}", f"{account_num}", f"{email}", f"{password}", account_balance, is_admin))
    except sqlite3.IntegrityError as e:
        return e.args[0].split(":")[1].strip()
    except Exception as e:
        return e.args[0].split(":")[1].strip()
    else:
        conn.commit()
        conn.close()
        return f"{True},{f_name},{l_name},{email},{account_num}"
    
def update_row(id, column, db_path):
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
def delete_user(account_num: str):
    
    """
    Delete a user from the users database by account number.

    Connects to the SQLite database defined by the global constant `USERS`
    and attempts to delete the record in the `users` table that matches the
    given account number.

    Args:
        account_num (str): The account number of the user to delete.

    Returns:
        bool | str:
            - True if the operation succeeds.
            - Error message string if an exception occurs.

    Raises:
        None explicitly. Any exception encountered during execution is caught
        and returned as a string.
    """

    conn = sqlite3.connect(f"{USERS}")
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "DELETE FROM users WHERE account_number = ?",
            (account_num,)
            )
    except Exception as e:
        return e.args[0].split(":")[1].strip()
    else:
        conn.commit()
        conn.close()
        return True

def add_to_warehouse(prod_name: str, prod_price: float, prod_category = "NULL") -> str:
    
    """
    Add a new product to the warehouse database.

    Connects to the SQLite database defined by the global constant `WAREHOUSE`
    and inserts a new record into the `warehouse` table.

    Args:
        prod_name (str): The name of the product.
        prod_price (float): The price of the product.
        prod_category (str, optional): The category of the product.
            Defaults to "NULL".

    Returns:
        str:
            - "Sucessful" (typo, should be "Successful") if the product was inserted.
            - An error message string if a database integrity error occurs
              (e.g., UNIQUE constraint failed).

    Raises:
        None explicitly. Integrity errors are caught and returned as strings.
    """
    
    conn = sqlite3.connect(f"{WAREHOUSE}")
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO warehouse (product_name, price, category)
        VALUES (?, ?, ?)              
        ''', (f"{prod_name}",f"{prod_price}", f"{prod_category}"))
    except sqlite3.IntegrityError as e:
        return e.args[0].split(":")[1].strip()
        
    conn.commit()
    conn.close()
    return "Sucessful"
        
def read_db(db_path: str) -> list|bool:
    
    """
    Read all rows from a database table.

    Connects to the SQLite database specified by `db_path`, infers the table
    name from the filename, and selects all rows from that table.

    Args:
        db_path (str): Path to the SQLite database file.
            Example: "databases/users.db"

    Returns:
        list | bool:
            - list: A list of tuples representing the rows if the query succeeds.
            - False: If an error occurs during query execution.

    Raises:
        None explicitly. Any exception is caught, printed, and False is returned.
    """
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute(f"SELECT * FROM {db_path.replace("databases/", "").replace(".db", "")}")
        rows = cursor.fetchall()
    except Exception as e:
        print(f"{e}")
        return False
    
    for row in rows:
        print(row)
    conn.close()
    return rows

def value_exists(value, column, db_path):
    
    """
    Check if a value exists in a given column of a database table.

    Connects to the SQLite database specified by `db_path`, infers the table
    name from the file name, and queries for the first row where `column`
    matches the given `value`.

    Args:
        value (Any): The value to search for in the column.
        column (str): The column name to search within.
        db_path (str): Path to the SQLite database file.
            Example: "databases/users.db"

    Returns:
        tuple | None:
            - tuple: The first row found where the column matches the value.
            - None: If no row matches.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM {db_path.replace("databases/", "").replace(".db", "")} WHERE {column} = ?", (value,))
    result = cursor.fetchone()
    return result

# create_warehouse_db()
#print(appendto_usersdb("Victor", "Austine", "0000000000", "joyaustie454@gmail.com", "0000000", 50000))
# print(type(value_exists("0000000000", "account_number", USERS)))
# add_to_warehouse("Fish", 8)
# delete_user("7756308072")
# read_db(USERS)
