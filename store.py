import re
import data as d
import time

cart = []

def purchase(user: list) -> None:
    """
    `purcahse` is a function that manages the user's shopping experience, allowing them to search, add to cart, and checkout.
    It presents a menu with options to:
    `search`, `view Cart`, `checkout`, and `exit`

    Args:
        user (list): A list representing the authenticated user's account data.
                     It is expected to contain the user's balance at index `3`
                     (e.g., `user[3] = "150000.0"`). The username is expected
                     at index `0` (e.g., `user[0] = "john_doe"`).

    Returns:
        None: This function primarily interacts with the user via print statements
              and input prompts. It modifies the `user` list in place to update
              the balance and implicitly relies on `load_accounts` and
              `save_accounts` to persist these changes.
    """
    while True:
        print("\n1. Search\n2. View Cart\n3. Checkout\n4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            query = input("Search: ")
            results = search_inventory(query)
            if results:
                for i, item in enumerate(results, 1):
                    print(f"\t{i}. {item} - NGN {d.inventory[item]}")
                    time.sleep(0.1)
                time.sleep(0.6)
                add_to_cart(results)
            else:
                print("No items found.")

        elif choice == '2':
            view_cart()
        elif choice == '3':
            checkout(user)
        elif choice == '4':
            break
        else:
            print("Invalid Selection")


def search_inventory(query: str) -> list:
    """
    `search_inventory` is a function that searches the global inventory for items matching all terms in a given query.

    This function processes a search query, breaking it into individual terms.
    It then uses these terms to find items in the `inventory` (expected to be
    a globally accessible dictionary or passed implicitly). An item matches
    if its name contains all the search terms, irrespective of case. The
    results are returned without specific sorting in this version.

    Args:
        query (str): The search string, which can contain multiple terms
                     separated by spaces (e.g., "dell laptop").

    Returns:
        list: A list of strings, where each string is an item name from
              the inventory that contains all the search terms. Returns
              an empty list if no matches are found.
    """
    terms = query.split()
    patterns = [re.compile(re.escape(term), re.IGNORECASE) for term in terms]
    results = []
    for item in d.inventory:
        if all(p.search(item) for p in patterns):
            results.append(item)
    return results
            
def add_to_cart(results: list):
    """
    
    add items from inventory to `cart`
    Args:
        results (list): A list representing all search results for an item.

    Returns:
        None: 
    """
    
    while True:
        add = input("Add item number to cart (or press Enter to skip): ")
        if add:
            try:
                index = int(add) - 1
                cart.append(results[index])
            except:
                print("Invalid selection.")
            continue
        break

def view_cart():
    """
    View Cart: Display all items currently in the shopping cart and their prices.
    Args:
        None:

    Returns:
        None:
    """
    print("\nCart:")
    for item in cart:
        print(f"- {item} - NGN {d.inventory[item]}")
    print(f"Total: {sum(d.inventory[item] for item in cart):,}")

def checkout(user: list):
    
    """
    Checkout: Calculate the total cost of items in the cart. If the user
    has sufficient funds in their account balance, the total is deducted,
    the purchase is confirmed, the cart is cleared, and the user's updated
        balance is saved to the accounts data (via `load_accounts` and
        `save_accounts`, which are assumed to be externally defined). If funds
        are insufficient, a message is displayed.
        
    Args:
        user (list): A list representing the authenticated user's account data.
                    It is expected to contain the user's balance at index `3`
                    (e.g., `user[3] = "150000.0"`). The username is expected
                     at index `0` (e.g., `user[0] = "john_doe"`).
    Returns:
            None:
    """
    total = sum(d.inventory[item] for item in cart)
    print(f"Total: NGN {total}")
    
    if float(user[3]) >= total:
        user[3] = str(float(user[3]) - total)
        print("Purchase successful!")
        print(f"Updated Balance: {user[3]:,}")
        cart.clear()
        
        accounts = d.load_accounts()
        for acc in accounts:
            if acc[0] == user[0]:
                acc[3] = user[3]
        d.save_accounts(accounts)
    else:
        print("Insufficient balance.")