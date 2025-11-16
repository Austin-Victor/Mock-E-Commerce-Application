import customtkinter as ctk
from gui.theme import PRIMARY_COLOR, ACCENT_COLOR, TEXT_COLOR, SECONDARY_TEXT

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master, user_name, account_number, balance, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=PRIMARY_COLOR)

        self.user_name = user_name
        self.account_number = account_number
        self.balance = balance
        self.show_balance = True

        self.build_ui()

    def build_ui(self):
        
        # Header
        header_frame = ctk.CTkFrame(self, height=100, corner_radius=20)
        header_frame.pack(fill="x", pady=10, padx = 10)
        header_frame.pack_propagate(False)
        
        acc_name = ctk.CTkLabel(header_frame, text=f"{self.user_name}",
                     font=("SF Pro Display", 20, "bold"), text_color=TEXT_COLOR)
        acc_name.grid(row=0, column=0, sticky="w", padx=(20, 0), pady=(10, 0))
        
        acc_num = ctk.CTkLabel(header_frame, text=f"{self.account_number}",
                     font=("SF Pro Display", 12), text_color=SECONDARY_TEXT)
        acc_num.grid(row=1, column=0, sticky="w", padx=(20, 30), pady=(0,0))

        # Balance frame
        balance_frame = ctk.CTkFrame(header_frame, corner_radius=12, height=50, fg_color=PRIMARY_COLOR)
        balance_frame.pack(padx=5, pady=0, side="right")
        balance_frame.pack_propagate(False)

        self.balance_label = ctk.CTkLabel(balance_frame, 
                                          text=f"${self.balance:,.2f}", 
                                          font=("SF Pro Display", 16, "bold"), 
                                          text_color=TEXT_COLOR)
        self.balance_label.pack(side="left", padx=(30,0))

        self.eye_button = ctk.CTkButton(balance_frame, text="👁", width=40,
                                        fg_color="transparent", text_color=ACCENT_COLOR,
                                        command=self.toggle_balance)
        self.eye_button.pack(side="right", padx=(0,20))

        #Mid frame
        middle_frame = ctk.CTkFrame(self, height=100, corner_radius=20)
        middle_frame.pack(fill="x", pady=10, padx = 10)
        middle_frame.pack_propagate(False)
        
        # Action buttons
        actions_frame = ctk.CTkFrame(middle_frame, fg_color=None)
        actions_frame.pack(expand=True)

        ctk.CTkButton(actions_frame, text="➕ Deposit", fg_color=ACCENT_COLOR, width=120, height=40, corner_radius=12).pack(side="left", pady=10, padx = 10)
        ctk.CTkButton(actions_frame, text="➖ Withdraw", fg_color=ACCENT_COLOR, width=120, height=40, corner_radius=12).pack(side="left", pady=10, padx = 10)
        ctk.CTkButton(actions_frame, text="🔍 Search", fg_color=ACCENT_COLOR, width=120, height=40, corner_radius=12).pack(side="left", pady=10, padx = 10)

    def toggle_balance(self):
        self.show_balance = not self.show_balance
        if self.show_balance:
            self.balance_label.configure(text=f"${self.balance:,.2f}")
            self.eye_button.configure(text="👁")
        else:
            self.balance_label.configure(text="    ******")
            self.eye_button.configure(text="🚫")