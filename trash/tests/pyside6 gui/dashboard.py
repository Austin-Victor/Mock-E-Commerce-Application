# dashboard.py
from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QFrame,
    QSizePolicy, QGridLayout, QScrollArea
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QPixmap

from theme import CARD_BG, ACCENT, TEXT, DIM_TEXT

class DashboardWidget(QWidget):
    def __init__(self, main_app, user_obj, navigator):
        """
        main_app: parent (unused in this widget)
        user_obj: dict with user data
        navigator: MainWindow for navigation/animations
        """
        super().__init__()
        self.main_app = main_app
        self.user = user_obj
        self.navigator = navigator

        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)

        # Sidebar
        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(220)
        self.sidebar.setStyleSheet(f"background-color: #151517;")
        s_layout = QVBoxLayout(self.sidebar)
        s_layout.setContentsMargins(18,18,18,18)
        s_layout.setSpacing(16)

        logo = QLabel("MyShop")
        logo.setFont(QFont("Segoe UI", 18, QFont.Bold))
        logo.setStyleSheet(f"color: {ACCENT};")
        s_layout.addWidget(logo)

        # nav buttons - placeholders for icons (add QIcon with setIcon if you have assets)
        btn_spec = [
            ("Home", self.show_home),
            ("Products", self.show_products),
            ("Cart", self.show_cart),
            ("Orders", self.show_orders),
            ("Deposit", lambda: self.navigator.animate_to(self.navigator.deposit)),
            ("Withdraw", lambda: self.navigator.animate_to(self.navigator.withdraw)),
            ("Profile", self.show_profile),
            ("Logout", self.logout)
        ]
        for text, cb in btn_spec:
            b = QPushButton(text)
            b.setFixedHeight(42)
            b.setStyleSheet("text-align:left; padding-left:12px; color: #cfcfcf; background: transparent; border: none;")
            b.clicked.connect(cb)
            s_layout.addWidget(b)

        s_layout.addStretch()
        self.layout().addWidget(self.sidebar)

        # Main content area with a scrollable area
        content_area = QScrollArea()
        content_area.setWidgetResizable(True)
        main_content = QWidget()
        main_content.setStyleSheet("background-color: transparent;")
        main_content.setLayout(QVBoxLayout())
        main_content.layout().setContentsMargins(30, 28, 30, 28)
        content_area.setWidget(main_content)
        self.layout().addWidget(content_area)

        # Top: user card + actions
        top_row = QHBoxLayout()
        user_card = QFrame()
        user_card.setStyleSheet(f"background-color: {CARD_BG}; border-radius: 12px;")
        user_card.setFixedHeight(120)
        uc_layout = QHBoxLayout(user_card)
        uc_layout.setContentsMargins(18,18,18,18)

        # user image placeholder
        avatar = QLabel()
        avatar.setFixedSize(72,72)
        avatar.setStyleSheet("background-color: #2A2A2A; border-radius: 36px;")
        # to set image later: avatar.setPixmap(QPixmap('assets/user.png').scaled(72,72,Qt.KeepAspectRatio,Qt.SmoothTransformation))
        uc_layout.addWidget(avatar)

        # user info
        uinfo = QVBoxLayout()
        name = QLabel(self.user.get("name", "User"))
        name.setFont(QFont("Segoe UI", 14, QFont.Bold))
        name.setStyleSheet(f"color: {TEXT};")
        uinfo.addWidget(name)

        acct = QLabel(f"Account: {self.user.get('account_no', '')}")
        acct.setStyleSheet(f"color: {DIM_TEXT};")
        uinfo.addWidget(acct)
        uc_layout.addLayout(uinfo)

        uc_layout.addStretch()

        # balance + eye button (no emoji)
        self.balance_label = QLabel(f"${self.user.get('balance', 0):,.2f}")
        self.balance_label.setFont(QFont("Segoe UI", 18, QFont.Bold))
        self.balance_label.setStyleSheet(f"color: {TEXT};")
        uc_layout.addWidget(self.balance_label)

        eye_btn = QPushButton()
        eye_btn.setFixedSize(36,36)
        eye_btn.setStyleSheet("background-color: transparent; border-radius: 6px;")
        # set icon later: eye_btn.setIcon(QIcon('assets/eye.svg'))
        eye_btn.clicked.connect(self.toggle_balance)
        uc_layout.addWidget(eye_btn)

        top_row.addWidget(user_card, 2)

        # Right top small cards (e.g., user-related quick metrics)
        quicks = QHBoxLayout()
        for title in ("Wallet", "Orders", "Saved"):
            card = QFrame()
            card.setFixedSize(160, 90)
            card.setStyleSheet(f"background-color: {CARD_BG}; border-radius: 10px;")
            cl = QVBoxLayout(card)
            t = QLabel(title)
            t.setStyleSheet(f"color: {DIM_TEXT};")
            v = QLabel("—")
            v.setFont(QFont("Segoe UI", 14, QFont.Bold))
            v.setStyleSheet(f"color: {TEXT};")
            cl.addWidget(t)
            cl.addWidget(v)
            quicks.addWidget(card)
        top_row.addLayout(quicks, 1)

        main_content.layout().addLayout(top_row)
        main_content.layout().addSpacing(22)

        # Product grid: 2 columns
        grid_frame = QFrame()
        grid_frame.setLayout(QGridLayout())
        grid = grid_frame.layout()
        grid.setSpacing(18)

        # create placeholder product cards with image slot
        for i in range(6):
            card = QFrame()
            card.setMinimumSize(220, 260)
            card.setStyleSheet(f"background-color: {CARD_BG}; border-radius: 10px;")
            c_layout = QVBoxLayout(card)
            # image placeholder
            img = QLabel()
            img.setFixedSize(180, 140)
            img.setStyleSheet("background-color: #2A2A2A; border-radius: 6px;")
            # later: img.setPixmap(QPixmap('assets/prodX.png').scaled(180,140,Qt.KeepAspectRatio, Qt.SmoothTransformation))
            c_layout.addWidget(img, alignment=Qt.AlignCenter)
            # product title
            title = QLabel(f"Product {i+1}")
            title.setStyleSheet(f"color: {TEXT}; font-weight: 600;")
            c_layout.addWidget(title, alignment=Qt.AlignLeft)
            # price and add-to-cart
            bottom = QHBoxLayout()
            price = QLabel(f"${(20+i*5):.2f}")
            price.setStyleSheet(f"color: {DIM_TEXT};")
            bottom.addWidget(price)
            buy = QPushButton("Add")
            buy.setFixedSize(70, 28)
            buy.setStyleSheet(f"background-color: {ACCENT}; color: white; border-radius:6px;")
            bottom.addWidget(buy, alignment=Qt.AlignRight)
            c_layout.addLayout(bottom)

            row = i // 3
            col = i % 3
            grid.addWidget(card, row, col)

        main_content.layout().addWidget(grid_frame)
        main_content.layout().addStretch()

    def toggle_balance(self):
        cur = self.balance_label.text()
        if cur.startswith("$"):
            self.balance_label.setText("••••••")
        else:
            self.balance_label.setText(f"${self.user.get('balance', 0):,.2f}")

    # simple placeholders for nav actions
    def show_home(self): pass
    def show_products(self): pass
    def show_cart(self): pass
    def show_orders(self): pass
    def show_profile(self): pass
    def logout(self):
        # go back to onboarding (simple)
        self.navigator.setCurrentWidget(self.navigator.onboarding)