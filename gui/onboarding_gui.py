import customtkinter as ctk
from tkinter import messagebox
from logic import credential_manager as cm
from logic.user import User

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()

app_width = 600
app_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (app_width/2))
y = int((screen_height/2) - (app_height/2))

root.title("E-commerce App")
root.geometry(f"{app_width}x{app_height}+{x}+{y}")
root.resizable(False, False)

tabview = ctk.CTkTabview(root, width=550, height=450, corner_radius=15)
tabview.pack(pady=30, padx=30, fill="both", expand=True)

sign_in_tab = tabview.add("Sign In")
sign_up_tab = tabview.add("Register")

signup_frame =ctk.CTkFrame(sign_up_tab, corner_radius=10)
signup_frame.pack(pady=20, padx=20, fill="both", expand=True)

signin_frame =ctk.CTkFrame(sign_in_tab, corner_radius=10)
signin_frame.pack(pady=20, padx=20, fill="both", expand=True)

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
            signup_label.configure(text=f"Problem with {response.split(".")[1]}", text_color="red", font=("Arial", 15))

def submit_signin():
    
    account_num = entry_claimed_id.get()
    pw = signin_password.get()
    
    if not account_num or not pw:
        signin_label.configure(text = "All fields are required", text_color="red", font=("Arial", 15))
        return
        
    response = User.sign_in(account_num, pw)
    if response == False:
        signin_label.configure(text=f"Account does not exist", text_color="red", font=("Arial", 15))
    elif response == "Invalid password":
        signin_label.configure(text=f"{response}", text_color="red", font=("Arial", 15))
    elif response == True:
        current_user = User.get_current_user()
        messagebox.showinfo("", f"Login successful! \nWelcome {current_user.f_name} {current_user.l_name}")
    else:
        messagebox.showerror("", response)

signup_label = ctk.CTkLabel(signup_frame, text="Create Account", font=("Arial", 20, "bold"))
signup_label.pack(pady=10)

entry_firstname = ctk.CTkEntry(signup_frame, width=300, height= 40, placeholder_text = "First name")
entry_firstname.pack(pady = 10)

entry_lastname = ctk.CTkEntry(signup_frame, width=300, height= 40, placeholder_text = "Last name")
entry_lastname.pack(pady = 10)

entry_email = ctk.CTkEntry(signup_frame, width=300, height= 40, placeholder_text = "Email address")
entry_email.pack(pady = 10)

entry_password = ctk.CTkEntry(signup_frame, width=300, height= 40, placeholder_text = "Password", show = "*")
entry_password.pack(pady = 10)

entry_confirm_pw = ctk.CTkEntry(signup_frame, width=300, height= 40, placeholder_text = "Confirm Password", show = "*")
entry_confirm_pw.pack(pady = 10)

signup_btn = ctk.CTkButton(signup_frame, text = "Sign up", width=200, height=40, corner_radius=12, command = sumbit_signup)
signup_btn.pack(pady = 15)

signin_label = ctk.CTkLabel(signin_frame, text="Welcome Back!", font=("Arial", 20, "bold"))
signin_label.pack(pady=20)

entry_claimed_id = ctk.CTkEntry(signin_frame, width=300, height= 40, placeholder_text="Account number or Email")
entry_claimed_id.pack(pady=10)

signin_password = ctk.CTkEntry(signin_frame, width=300, height= 40, placeholder_text="Password", show="*")
signin_password.pack(pady=10)

remember_me = ctk.CTkCheckBox(signin_frame, text="Remember Me")
remember_me.pack(pady=5)

signin_button = ctk.CTkButton(signin_frame, text="Sign In", width=200, height=40, corner_radius=12, command=submit_signin)
signin_button.pack(pady=20)

root.mainloop()