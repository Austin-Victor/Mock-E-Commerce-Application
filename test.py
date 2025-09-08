# import bcrypt
# from logic import database_manager as dbm
# # import utils
# # import gui
# # pw = "victor".encode()
# # hashed_pw = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
# # print(pw)

# acc_details: tuple = dbm.value_exists("8830392407", "account_number", dbm.USERS)
# print(acc_details[5].encode())
# print(bcrypt.checkpw("@Joy1234".encode(), acc_details[5].encode()))
# # for file in utils.WAREHOUSE_FILES:
# #         with open(file, 'r') as f:
# #             content = f.read().strip()
# #             if content:
# #                 items = content.split(';')
# #                 for item in items:
# #                     if ':' in item:
# #                         name, price = item.split(':')
# #                         dbm.add_to_warehouse(name, price)


# onboarding_gui.py
import customtkinter as ctk
from logic.user import User   # <-- assumes you have your User logic like we discussed

# -------------------------
# CTkinter Setup
# -------------------------
ctk.set_appearance_mode("dark")         # "light", "dark", or "system"
ctk.set_default_color_theme("blue")     # "blue", "green", "dark-blue"

app = ctk.CTk()
app.geometry("500x500")
app.title("E-Commerce Onboarding")

# -------------------------
# Tab View (Sign In / Sign Up)
# -------------------------
tabview = ctk.CTkTabview(app, width=450, height=350, corner_radius=15)
tabview.pack(pady=20, padx=20, fill="both", expand=True)

sign_in_tab = tabview.add("Sign In")
sign_up_tab = tabview.add("Sign Up")

# -------------------------
# Sign In Tab
# -------------------------
signin_frame = ctk.CTkFrame(sign_in_tab, corner_radius=10)
signin_frame.pack(pady=20, padx=20, fill="both", expand=True)

signin_label = ctk.CTkLabel(signin_frame, text="Welcome Back!", font=("Arial", 18, "bold"))
signin_label.pack(pady=10)

signin_username = ctk.CTkEntry(signin_frame, placeholder_text="Username")
signin_username.pack(pady=10)

signin_password = ctk.CTkEntry(signin_frame, placeholder_text="Password", show="*")
signin_password.pack(pady=10)

remember_me = ctk.CTkCheckBox(signin_frame, text="Remember Me")
remember_me.pack(pady=5)

def handle_sign_in():
    username = signin_username.get()
    password = signin_password.get()
    result = User.sign_in(username, password)
    if result["status"]:
        current_user = User.get_current_user()
        message_label.configure(text=f"✅ Welcome {current_user.username}!", text_color="green")
    else:
        message_label.configure(text=f"❌ {result['message']}", text_color="red")

signin_button = ctk.CTkButton(signin_frame, text="Sign In", corner_radius=12, command=handle_sign_in)
signin_button.pack(pady=15)

message_label = ctk.CTkLabel(signin_frame, text="", font=("Arial", 12))
message_label.pack(pady=5)

# -------------------------
# Sign Up Tab
# -------------------------
signup_frame = ctk.CTkFrame(sign_up_tab, corner_radius=10)
signup_frame.pack(pady=20, padx=20, fill="both", expand=True)

signup_label = ctk.CTkLabel(signup_frame, text="Create an Account", font=("Arial", 18, "bold"))
signup_label.pack(pady=10)

signup_username = ctk.CTkEntry(signup_frame, placeholder_text="Choose a Username")
signup_username.pack(pady=10)

signup_email = ctk.CTkEntry(signup_frame, placeholder_text="Email Address")
signup_email.pack(pady=10)

signup_password = ctk.CTkEntry(signup_frame, placeholder_text="Password", show="*")
signup_password.pack(pady=10)

def handle_sign_up():
    username = signup_username.get()
    email = signup_email.get()
    password = signup_password.get()
    # You’d implement your actual User.sign_up() here
    # For demo, just fake success
    message_signup.configure(text=f"✅ Account created for {username}!", text_color="green")

signup_button = ctk.CTkButton(signup_frame, text="Sign Up", corner_radius=12, fg_color="green", command=handle_sign_up)
signup_button.pack(pady=15)

message_signup = ctk.CTkLabel(signup_frame, text="", font=("Arial", 12))
message_signup.pack(pady=5)

# -------------------------
# Run App
# -------------------------
app.mainloop()
