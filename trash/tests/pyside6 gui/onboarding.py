# onboarding.py
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QTabWidget, QSpacerItem, QSizePolicy, QFrame
)
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt

from theme import CARD_BG, ACCENT, TEXT, DIM_TEXT

class OnboardingWidget(QWidget):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator  # MainWindow instance
        self.setContentsMargins(0,0,0,0)

        root = QHBoxLayout(self)
        root.setContentsMargins(40, 40, 40, 40)

        # left: branding / illustration (image placeholder)
        brand_frame = QFrame()
        brand_layout = QVBoxLayout(brand_frame)
        brand_layout.setAlignment(Qt.AlignCenter)

        logo = QLabel()
        logo.setFixedSize(220, 220)
        logo.setStyleSheet(f"background-color: {CARD_BG}; border-radius: 12px;")
        # drop your app logo here: logo.setPixmap(QPixmap('assets/logo.png').scaled(200,200,Qt.KeepAspectRatio, Qt.SmoothTransformation))
        brand_layout.addWidget(logo)

        title = QLabel("Welcome to\nMyShop")
        title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        title.setStyleSheet(f"color: {TEXT};")
        title.setAlignment(Qt.AlignCenter)
        brand_layout.addWidget(title)

        subtitle = QLabel("A modern shopping experience")
        subtitle.setStyleSheet(f"color: {DIM_TEXT};")
        subtitle.setAlignment(Qt.AlignCenter)
        brand_layout.addWidget(subtitle)

        root.addWidget(brand_frame, 1)

        # right: form area
        form_frame = QFrame()
        form_frame.setStyleSheet(f"background-color: {CARD_BG}; border-radius: 12px;")
        form_layout = QVBoxLayout(form_frame)
        form_layout.setContentsMargins(30, 30, 30, 30)

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setDocumentMode(True)
        tabs.setStyleSheet("""
            QTabBar::tab { height: 34px; width: 140px; }
            QTabBar::tab:selected { background: transparent; color: white; border-bottom: 2px solid %s; }
        """ % ACCENT)

        # Sign In tab
        signin = QWidget()
        s_layout = QVBoxLayout(signin)
        s_layout.setSpacing(8)
        self.si_user = QLineEdit()
        self.si_user.setPlaceholderText("Username or Email")
        self.si_pass = QLineEdit()
        self.si_pass.setEchoMode(QLineEdit.Password)
        self.si_pass.setPlaceholderText("Password")

        self.si_msg = QLabel("")
        self.si_msg.setStyleSheet("color: #F77676;")  # red-ish for errors

        btn_signin = QPushButton("Sign In")
        btn_signin.setFixedHeight(40)
        btn_signin.setStyleSheet(f"background-color: {ACCENT}; color: white; border-radius: 8px;")
        btn_signin.clicked.connect(self.attempt_signin)

        s_layout.addWidget(self.si_user)
        s_layout.addWidget(self.si_pass)
        s_layout.addWidget(self.si_msg)
        s_layout.addSpacing(6)
        s_layout.addWidget(btn_signin)
        s_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Sign Up tab
        signup = QWidget()
        up_layout = QVBoxLayout(signup)
        up_layout.setSpacing(8)
        self.su_name = QLineEdit()
        self.su_name.setPlaceholderText("Full name")
        self.su_email = QLineEdit()
        self.su_email.setPlaceholderText("Email")
        self.su_pass = QLineEdit()
        self.su_pass.setPlaceholderText("Password")
        self.su_pass.setEchoMode(QLineEdit.Password)

        self.su_msg = QLabel("")
        self.su_msg.setStyleSheet("color: #F77676;")

        btn_signup = QPushButton("Create Account")
        btn_signup.setFixedHeight(40)
        btn_signup.setStyleSheet(f"background-color: {ACCENT}; color: white; border-radius: 8px;")
        btn_signup.clicked.connect(self.attempt_signup)

        up_layout.addWidget(self.su_name)
        up_layout.addWidget(self.su_email)
        up_layout.addWidget(self.su_pass)
        up_layout.addWidget(self.su_msg)
        up_layout.addSpacing(6)
        up_layout.addWidget(btn_signup)
        up_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        tabs.addTab(signin, "Sign In")
        tabs.addTab(signup, "Sign Up")

        form_layout.addWidget(tabs)
        form_layout.addSpacing(6)

        # small footer links area
        footer = QHBoxLayout()
        footer.addStretch()
        help_btn = QPushButton("Need help?")
        help_btn.setFlat(True)
        help_btn.setStyleSheet("color: #9CA3AF; background: transparent;")
        footer.addWidget(help_btn)
        form_layout.addLayout(footer)

        root.addWidget(form_frame, 2)

    def attempt_signin(self):
        u = self.si_user.text().strip()
        p = self.si_pass.text().strip()
        if not u or not p:
            self.si_msg.setText("Enter both username and password.")
            return
        # TODO: call real logic (bcrypt + sqlite) — for now, we fake success
        user_obj = {
            "name": u.split("@")[0] if "@" in u else u,
            "account_no": "ACC-"+u[:4].upper(),
            "balance": 4200.50,
            "email": u if "@" in u else f"{u}@example.com"
        }
        self.si_msg.setText("")
        # navigator is the MainWindow (QStackedWidget)
        self.navigator.login_success(user_obj)

    def attempt_signup(self):
        n = self.su_name.text().strip()
        e = self.su_email.text().strip()
        p = self.su_pass.text().strip()
        if not n or not e or not p:
            self.su_msg.setText("Complete all fields to sign up.")
            return
        # TODO: persist new user; validate email/password strength
        user_obj = {
            "name": n,
            "account_no": "ACCNEW-001",
            "balance": 0.00,
            "email": e
        }
        self.su_msg.setText("")
        self.navigator.login_success(user_obj)