import customtkinter as ctk
from gui.theme import init_theme
from gui.onboarding_gui import OnboardingFrame
from gui.dashboard_gui import DashboardFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        init_theme()

        self.title("E-Commerce App")
        self.geometry("900x600")
        self.resizable(False, False)
        self.center_window()

        self.current_frame = None
        self.show_onboarding()

    def center_window(self):
        self.update_idletasks()
        width, height = 900, 600
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def switch_frame(self, new_frame):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(expand=True, fill="both")

    def show_onboarding(self):
        self.switch_frame(OnboardingFrame(self, self.show_dashboard))

    def show_dashboard(self, user_name, account_number, balance):
        self.switch_frame(DashboardFrame(self, user_name, account_number, balance))

if __name__ == "__main__":
    app = App()
    app.mainloop()