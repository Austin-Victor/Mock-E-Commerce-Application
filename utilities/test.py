import bcrypt
import utils
import core.database_manager as dbm



dbm.delete_user("1174873895")

# for file in utils.WAREHOUSE_FILES:
#         with open(file, 'r') as f:
#             content = f.read().strip()
#             if content:
#                 items = content.split(';')
#                 for item in items:
#                     if ':' in item:
#                         name, price = item.split(':')
#                         dbm.add_to_warehouse(name, price)