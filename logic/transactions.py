import database_manager as dbm
from user import User

def add_funds(account_num, fund_ammount):
    try:
        if fund_ammount < 5 or fund_ammount > 5000000:
            dbm.update_row(account_num, "account_bal", dbm.USERS)
            return False
    except Exception as e:
        return e.args
    

def withdraw_funds(account_num, withdraw_amount):
    try:
        if withdraw_amount < 5 or withdraw_amount > 5000000:
            dbm.update_row(account_num, "account_bal", dbm.USERS)
            return False
    except Exception as e:
        return e.args

def purchase_item():
    pass