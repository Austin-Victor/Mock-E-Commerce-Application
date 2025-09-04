import sqlite3  
 
USERS = "databases/users.db"
INVENTORY = "databases/inventory.db"
WAREHOUSE = "databases/warehouse.db"

def create_users_db():
        
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
    
def delete_user(account_num: str):
    
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
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM {db_path.replace("databases/", "").replace(".db", "")} WHERE {column} = ?", (value,))
    result = cursor.fetchone()
    return result

# create_warehouse_db()
#print(appendto_usersdb("Victor", "Austine", "0000000000", "joyaustie454@gmail.com", "0000000", 50000))
# print(type(value_exists("0000000000", "account_number", USERS)))
# add_to_warehouse("Fish", 8)
delete_user("8960075810")
read_db(USERS)
