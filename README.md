This project involves designing and implementing a terminal-based e-commerce application in Python. The application will have features such as:

1. User authentication (Sign-In and Sign-Up)
2. Inventory management from warehouse files
3. Wallet funding and payment logic
2. Product listing and searching
3. Shopping cart management
4. Order processing and payment
5. User account management

The application will store user data in a file named "accounts.txt" in a data directory and product data in files named "warehouse*.txt" in the same directory

High-level overview of how the system will work:

1. The user will be presented with a login menu to sign in or sign up.
2. The program will check, when a user selects sign in if the entered details are present in the accounts file and proceeds the user to the next menu
3. If the user selects sign up, the program will ask for details from the user and either generate a passowrd or allow manual entry of password from the user 
4. After successful login, the user will be taken to the main menu where they can:
    - Fund their wallet
    - Make purchases
    - Manage their account
    - Exit the program
5. The user can fund their wallet with various fixed amounts, search for products, add them to their cart, and checkout.
6. The program will handle errors and exceptions, such as insufficient balance or invalid inputs.

Some key features of the program include:

- Data persistence: User data and product data will be stored in files and loaded into the program when it starts.
- Password verification: Users will be required to enter their password to access certain features.
- Account management: Users will be able to perform various actions on their accounts such as change username, password, reset balance or delete account.
- Confirmation prompts: The program will ask for confirmation before performing certain actions, such as deleting an account or resetting a balance.

Overall, the program will provide a basic e-commerce experience for users, allowing them to browse products, make purchases, and manage their accounts.