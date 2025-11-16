import customtkinter as ctk
from tkinter import messagebox
from logic import credential_manager as cm
from logic.user import User
from gui.theme import PRIMARY_COLOR, ACCENT_COLOR, TEXT_COLOR, SECONDARY_TEXT

class OnboardingFrame(ctk.CTkFrame):
    def __init__(self, master, switch_to_dashboard, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=PRIMARY_COLOR)

        self.switch_to_dashboard = switch_to_dashboard

        # Tabview (Sign In / Sign Up)
        self.tabs = ctk.CTkTabview(self, corner_radius=20)
        self.tabs.pack(expand=True, fill="both", padx=40, pady=40)

        self.signin_tab = self.tabs.add("Sign In")
        self.signup_tab = self.tabs.add("Sign Up")

        self.build_signin()
        self.build_signup()

    def build_signin(self):
        signin_label = ctk.CTkLabel(self.signin_tab, text="Welcome Back", 
                     font=("SF Pro Display", 20, "bold"), text_color=TEXT_COLOR)
        signin_label.pack(pady=20)

        self.signin_id = ctk.CTkEntry(self.signin_tab, width=300, height= 40, placeholder_text="Account number or Email")
        self.signin_id.pack(pady=10, padx=60, fill="x")

        self.signin_password = ctk.CTkEntry(self.signin_tab, width=300, height= 40, placeholder_text="Password", show="*")
        self.signin_password.pack(pady=10, padx=60, fill="x")
        
        self.remember_me = ctk.CTkCheckBox(self.signin_tab, text="Remember Me")
        self.remember_me.pack(pady=5)

        ctk.CTkButton(self.signin_tab, text="Sign In", width=200, height=40, corner_radius=12,
                      fg_color=ACCENT_COLOR, command=self.handle_signin).pack(pady=30)

    def build_signup(self):
        ctk.CTkLabel(self.signup_tab, text="Create Account", 
                     font=("SF Pro Display", 20, "bold"), text_color=TEXT_COLOR).pack(pady=10)

        self.signup_firstname = ctk.CTkEntry(self.signup_tab, width=300, height= 40, placeholder_text = "First name")
        self.signup_firstname.pack(pady=10, padx=60, fill="x")
        
        self.signup_lastname = ctk.CTkEntry(self.signup_tab, width=300, height= 40, placeholder_text = "Last name")
        self.signup_lastname.pack(pady=10, padx=60, fill="x")

        self.signup_email = ctk.CTkEntry(self.signup_tab, width=300, height= 40, placeholder_text="Email")
        self.signup_email.pack(pady=10, padx=60, fill="x")

        self.signup_password = ctk.CTkEntry(self.signup_tab, width=300, height= 40, placeholder_text="Password", show="*")
        self.signup_password.pack(pady=10, padx=60, fill="x")
        
        self.signup_confirm_password = ctk.CTkEntry(self.signup_tab, width=300, height= 40, placeholder_text="Confirm Password", show="*")
        self.signup_confirm_password.pack(pady=10, padx=60, fill="x")

        ctk.CTkButton(self.signup_tab, text="Sign Up", width=200, height=40, corner_radius=12,
                      fg_color=ACCENT_COLOR, command=self.handle_signup).pack(pady=10)

    def handle_signin(self):
        id = self.signin_id.get().strip()
        pw = self.signin_password.get()

        if not id or not pw:
            messagebox.showerror("Error", "All fields are required")
            return
        
        response = User.sign_in(id, pw)
        if response == False:
            messagebox.showerror("Error", "Account does not exist")
        elif response == "Invalid password":
            messagebox.showerror("Error", f"{response}")
        elif response == True:
            current_user = User.get_current_user()
            self.switch_to_dashboard(f"{current_user.f_name} {current_user.l_name}", current_user.account_num, current_user.account_balance)
        else:
            messagebox.showerror("", response)

    def handle_signup(self):
        
        f_name = self.signup_firstname.get().strip()
        l_name = self.signup_lastname.get().strip()
        email = self.signup_email.get().strip()
        password = self.signup_password.get()
        cnfrm = self.signup_confirm_password.get()
        
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
            else:
                messagebox.showerror("Error", f"Problem with {response.split(".")[1]}")