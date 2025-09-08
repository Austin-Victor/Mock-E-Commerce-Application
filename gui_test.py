# # dashboard_gui.py
# import customtkinter as ctk

# # Setup CTkinter
# ctk.set_appearance_mode("dark")   # "light", "dark", "system"
# ctk.set_default_color_theme("blue")

# class DashboardApp(ctk.CTk):
#     def __init__(self):
#         super().__init__()

#         # Window setup
#         self.title("E-Commerce Dashboard")
#         self.geometry("900x600")

#         # Sidebar frame
#         self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
#         self.sidebar.pack(side="left", fill="y")

#         # Sidebar buttons
#         self.logo_label = ctk.CTkLabel(self.sidebar, text="ShopEase", font=("Arial", 20, "bold"))
#         self.logo_label.pack(pady=20)

#         self.home_button = ctk.CTkButton(self.sidebar, text="🏠 Home", command=self.show_home)
#         self.home_button.pack(pady=10, fill="x")

#         self.orders_button = ctk.CTkButton(self.sidebar, text="📦 Orders", command=self.show_orders)
#         self.orders_button.pack(pady=10, fill="x")

#         self.profile_button = ctk.CTkButton(self.sidebar, text="👤 Profile", command=self.show_profile)
#         self.profile_button.pack(pady=10, fill="x")

#         self.logout_button = ctk.CTkButton(self.sidebar, text="🚪 Logout", fg_color="red", command=self.quit)
#         self.logout_button.pack(pady=10, fill="x")

#         # Main content frame
#         self.content_frame = ctk.CTkFrame(self, corner_radius=10)
#         self.content_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

#         # By default, show Home
#         self.show_home()

#     # -------------------------
#     # Page Handlers
#     # -------------------------
#     def clear_content(self):
#         for widget in self.content_frame.winfo_children():
#             widget.destroy()

#     def show_home(self):
#         self.clear_content()
#         label = ctk.CTkLabel(self.content_frame, text="📊 Dashboard Overview", font=("Arial", 18, "bold"))
#         label.pack(pady=20)

#         sales_progress = ctk.CTkProgressBar(self.content_frame, width=400)
#         sales_progress.set(0.7)
#         sales_progress.pack(pady=10)
#         ctk.CTkLabel(self.content_frame, text="Sales Target: 70% reached").pack(pady=5)

#         orders_progress = ctk.CTkProgressBar(self.content_frame, width=400, fg_color="gray", progress_color="green")
#         orders_progress.set(0.45)
#         orders_progress.pack(pady=10)
#         ctk.CTkLabel(self.content_frame, text="Orders Fulfilled: 45%").pack(pady=5)

#     def show_orders(self):
#         self.clear_content()
#         label = ctk.CTkLabel(self.content_frame, text="📦 Recent Orders", font=("Arial", 18, "bold"))
#         label.pack(pady=20)

#         scroll_frame = ctk.CTkScrollableFrame(self.content_frame, width=600, height=300)
#         scroll_frame.pack(pady=10, fill="both", expand=True)

#         for i in range(1, 16):
#             order_label = ctk.CTkLabel(scroll_frame, text=f"Order #{i} - Status: Shipped")
#             order_label.pack(anchor="w", pady=2)

#     def show_profile(self):
#         self.clear_content()
#         label = ctk.CTkLabel(self.content_frame, text="👤 User Profile", font=("Arial", 18, "bold"))
#         label.pack(pady=20)

#         ctk.CTkLabel(self.content_frame, text="Username: Victor").pack(pady=5)
#         ctk.CTkLabel(self.content_frame, text="Email: victor@mail.com").pack(pady=5)

#         update_btn = ctk.CTkButton(self.content_frame, text="Update Profile", fg_color="green")
#         update_btn.pack(pady=20)

# # Run App
# if __name__ == "__main__":
#     app = DashboardApp()
#     app.mainloop()

# onboarding_gui.py
import customtkinter as ctk
from logic.user import User   # <-- assumes your User logic is in place

# -------------------------
# CTkinter Setup
# -------------------------
ctk.set_appearance_mode("dark")         # "light", "dark", or "system"
ctk.set_default_color_theme("blue")     # "blue", "green", "dark-blue"

app = ctk.CTk()

# Window size
app_width = 600
app_height = 450

# Center the window
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = int((screen_width/2) - (app_width/2))
y = int((screen_height/2) - (app_height/2))

app.geometry(f"{app_width}x{app_height}+{x}+{y}")
app.title("E-Commerce Onboarding")

# -------------------------
# Tab View (Sign In / Sign Up)
# -------------------------
tabview = ctk.CTkTabview(app, width=550, height=400, corner_radius=15)
tabview.pack(pady=20, padx=20, fill="both", expand=True)

sign_in_tab = tabview.add("Sign In")
sign_up_tab = tabview.add("Sign Up")

# -------------------------
# Sign In Tab
# -------------------------
signin_frame = ctk.CTkFrame(sign_in_tab, corner_radius=10)
signin_frame.pack(pady=20, padx=20, fill="both", expand=True)

signin_label = ctk.CTkLabel(signin_frame, text="Welcome Back!", font=("Arial", 20, "bold"))
signin_label.pack(pady=15)

signin_username = ctk.CTkEntry(signin_frame, width=350, placeholder_text="Username")
signin_username.pack(pady=10)

signin_password = ctk.CTkEntry(signin_frame, width=350, placeholder_text="Password", show="*")
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

signin_button = ctk.CTkButton(signin_frame, text="Sign In", width=200, height=40, corner_radius=12, command=handle_sign_in)
signin_button.pack(pady=20)

message_label = ctk.CTkLabel(signin_frame, text="", font=("Arial", 12))
message_label.pack(pady=5)

# -------------------------
# Sign Up Tab
# -------------------------
signup_frame = ctk.CTkFrame(sign_up_tab, corner_radius=10)
signup_frame.pack(pady=20, padx=20, fill="both", expand=True)

signup_label = ctk.CTkLabel(signup_frame, text="Create an Account", font=("Arial", 20, "bold"))
signup_label.pack(pady=15)

signup_username = ctk.CTkEntry(signup_frame, width=350, placeholder_text="Choose a Username")
signup_username.pack(pady=10)

signup_email = ctk.CTkEntry(signup_frame, width=350, placeholder_text="Email Address")
signup_email.pack(pady=10)

signup_password = ctk.CTkEntry(signup_frame, width=350, placeholder_text="Password", show="*")
signup_password.pack(pady=10)

def handle_sign_up():
    username = signup_username.get()
    email = signup_email.get()
    password = signup_password.get()
    # Hook up your actual sign-up logic here
    message_signup.configure(text=f"✅ Account created for {username}!", text_color="green")

signup_button = ctk.CTkButton(signup_frame, text="Sign Up", width=200, height=40, corner_radius=12, fg_color="green", command=handle_sign_up)
signup_button.pack(pady=20)

message_signup = ctk.CTkLabel(signup_frame, text="", font=("Arial", 12))
message_signup.pack(pady=5)

# -------------------------
# Run App
# -------------------------
app.mainloop()