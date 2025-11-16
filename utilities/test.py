import os
import re
import random
import string
import database_manager as dbm

DATA_DIR = 'data'
ACCOUNTS_FILE = os.path.join(DATA_DIR, 'accounts.txt')
WAREHOUSE_FILES = [os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR) if f.startswith('warehouse') and f.endswith('.txt')]

i = 0
for file in WAREHOUSE_FILES:
    with open(file, 'r') as f:
        content = f.read().strip()
        if content:
            items = content.split(';')
            for item in items:
                if ':' in item:
                    name, price = item.split(':')
                    dbm.add_to_warehouse(name.strip(), price, "cosmetics")
                    i = i + 1
                    print(f"{i} {name}")