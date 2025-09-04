import customtkinter as ctk
from tkinter import messagebox
from core import credential_manager as cm
from core.user import User

def sumbit_signup():
    
    """
    `sign_up` is a function that registers a new user account by collecting username, email, and password.

    This function prompts the user to enter a desired username and email.
    It first checks if the entered username or email already exists in the
    system using `find_user()`. If either exists, an error message is displayed,
    and the sign-up process is aborted, going back to previous prompt.

    The user then has the option to either have a strong password automatically
    generated using `generate_password()` or to manually enter a password.
    If a manual password is chosen, it is validated against complexity rules
    using `password_valid()` until a valid one is provided. The password is then hashed using bcrypt.

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
    
    f_name = entry_firstname.get()
    l_name = entry_lastname.get()
    email = entry_email.get()
    password = entry_password.get()
    cnfrm = entry_confirm_pw.get()
    
    if not f_name or not l_name or not email or not password or not cnfrm:
        messagebox.showerror("Error", "All fields are required")
        return
    elif not cm.pw_is_valid(password):
        messagebox.showwarning("Weak password", "Password must be at least 8 in length, contain an uppercase, a lowercase, a number, and a symbol")
    elif not cm.is_match(password, cnfrm):
        messagebox.showerror("Error", "Passwords do not match")
        return
    else:
        response = User.sign_up(f_name, l_name, email, password)
        if response.__contains__(","):
            response = response.split(",")
            if response[0] == "True":
                messagebox.showinfo("Success", "Account created successfully")
                messagebox.showinfo("Account Details", f"Account Name: {response[1]} {response[2]}\n\nEmail: {response[3]}\n\nAccount Number: {response[4]}")
        else:
            messagebox.showerror("Error", f"Problem with {response.split(".")[1]}")

def submit_signin():
    account_num = entry_claimed_id.get()
    pw = entry_claimed_password.get()

        
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("E-commerce App")
root.geometry("500x500")
root.resizable(False, False)

signup_frame =ctk.CTkFrame(root, width= 400, height= 400)
signup_frame.pack(expand = True)

signin_frame =ctk.CTkFrame(root, width= 400, height= 400)
signin_frame.pack(expand = True)
    
entry_firstname = ctk.CTkEntry(signup_frame, placeholder_text = "First name", width = 360, height= 36)
entry_lastname = ctk.CTkEntry(signup_frame, placeholder_text = "Last name",  width = 360, height= 36)
entry_email = ctk.CTkEntry(signup_frame, placeholder_text = "Email address", width = 360, height= 36)
entry_password = ctk.CTkEntry(signup_frame, placeholder_text = "Password", show = "*", width = 360, height= 36)
entry_confirm_pw = ctk.CTkEntry(signup_frame, placeholder_text = "Confirm Password", show = "*", width = 360, height= 36)
submit_btn = ctk.CTkButton(signup_frame, text = "Sign up", command = sumbit_signup, width= 76)

entry_claimed_id = ctk.CTkEntry(signin_frame, placeholder_text = "Account number or Email address", width = 360, height= 36)
entry_claimed_password = ctk.CTkEntry(signin_frame, placeholder_text = "Password", show = "*", width = 360, height= 36)
submit_btn = ctk.CTkButton(signin_frame, text = "Sign in", command = submit_signin, width= 76)

entry_firstname.pack(pady = 10)
entry_lastname.pack(pady = 10)
entry_email.pack(pady = 10)
entry_password.pack(pady = 10)
entry_confirm_pw.pack(pady = 10)
submit_btn.pack(pady = 10)

entry_claimed_id.pack(pady = 10)
entry_claimed_password.pack(pady = 10)

root.mainloop()