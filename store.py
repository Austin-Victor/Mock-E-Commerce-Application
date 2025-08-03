import re
from utils import load_accounts, save_accounts

def search_inventory(query: str, inventory: dict) -> list:
    """
    `search_inventory` is a function that searches the inventory for items matching all terms in a given query.

    This function takes a search query string, splits it into individual terms,
    and then compiles regular expressions for each term to perform case-insensitive
    matching. It iterates through the inventory items and returns a list of
    items that contain all the search terms. The results are sorted alphabetically.

    Args:
        query (str): The search string, which can contain multiple terms
                     separated by spaces.
        inventory (dict): A dictionary where keys are item names (strings)
                          and values are their prices.

    Returns:
        list: A sorted list of strings, where each string is an item name
              from the inventory that matches all search terms.
              Returns an empty list if no matches are found.
    """
    terms = query.split()
    patterns = [re.compile(re.escape(term), re.IGNORECASE) for term in terms]
    results = []
    for item in inventory:
        if all(p.search(item) for p in patterns):
            results.append(item)
    results.sort()  # Alphabetically sorted results
    return results

def purchase(user: list, inventory: dict) -> None:
    """
    `purchase` is a function that manages the user's shopping experience, including searching, viewing the cart, and checkout.

    This function provides an interactive interface for a user to browse and purchase items
    from an inventory. It allows users to:
     Search for items using keywords.
     Add selected items to a shopping cart.
     View the current contents of their cart.
     Proceed to checkout, where the total cost is calculated and deducted from the
       user's balance if sufficient funds are available.
     Exit the purchasing interface.

    Upon successful checkout, the user's balance is updated in their account data
    and saved.

    Args:
        user (list): A list representing the user's account information.
                     It is expected to be in the format:
                     [username, password, account_number, balance, ...]
                     where index 3 holds the current balance as a string.
        inventory (dict): A dictionary where keys are item names (strings)
                          and values are their prices (numeric).

    Returns:
        None: This function primarily interacts with the user and modifies
              the user's balance in place within the `user` list. It also
              calls `load_accounts()` and `save_accounts()` (assumed to be
              defined elsewhere) to persist changes to the user's account.
    """
    cart = []
    while True:
        print("\n1. Search\n2. View Cart\n3. Checkout\n4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            query = input("Search: ")
            results = search_inventory(query, inventory)
            if results:
                for i, item in enumerate(results, 1):
                    print(f"{i}. {item} - NGN {inventory[item]}")
                add = input("Add item number to cart (or press Enter to skip): ")
                if add:
                    try:
                        index = int(add) - 1
                        if 0 <= index < len(results):
                            cart.append(results[index])
                        else:
                            print("Invalid selection.")
                    except:
                        print("Invalid selection.")
            else:
                print("No items found.")

        elif choice == '2':
            print("\nCart:")
            if not cart:
                print("Your cart is empty.")
            for item in cart:
                print(f"- {item} - NGN {inventory[item]}")

        elif choice == '3':
            if not cart:
                print("Cart is empty.")
                continue
            total = sum(inventory[item] for item in cart)
            print(f"Total: NGN {total}")
            if float(user[3]) >= total:
                user[3] = str(float(user[3]) - total)
                print("Purchase successful!")
                cart.clear()
                accounts = load_accounts()
                for acc in accounts:
                    if acc[0] == user[0]:
                        acc[3] = user[3]
                save_accounts(accounts)
            else:
                print("Insufficient balance.")

        elif choice == '4':
            break
        else:
            print("Invalid choice.")
