# deposit_withdraw.py
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFrame
)
from PySide6.QtCore import Qt
from theme import CARD_BG, ACCENT, TEXT, DIM_TEXT

class BaseMoneyWidget(QWidget):
    def __init__(self, title, back_callback):
        super().__init__()
        self.back_callback = back_callback
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(120, 80, 120, 80)
        frame = QFrame()
        frame.setStyleSheet(f"background-color: {CARD_BG}; border-radius: 12px;")
        frame.setLayout(QVBoxLayout())
        frame.layout().setContentsMargins(28, 28, 28, 28)

        lbl = QLabel(title)
        lbl.setStyleSheet(f"color: {TEXT}; font-size: 20px; font-weight: 600;")
        frame.layout().addWidget(lbl)

        self.amount = QLineEdit()
        self.amount.setPlaceholderText("Amount (e.g. 1000.00)")
        frame.layout().addWidget(self.amount)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        frame.layout().addWidget(self.password)

        self.msg = QLabel("")
        self.msg.setStyleSheet("color: #F77676;")
        frame.layout().addWidget(self.msg)

        btn = QPushButton("Submit")
        btn.setStyleSheet(f"background-color: {ACCENT}; color: white; border-radius: 8px; height: 36px;")
        btn.clicked.connect(self.submit)
        frame.layout().addWidget(btn)

        back = QPushButton("Back")
        back.setStyleSheet("background: transparent; color: #9CA3AF;")
        back.clicked.connect(self.back_callback)
        frame.layout().addWidget(back, alignment=Qt.AlignLeft)

        self.layout().addWidget(frame)

    def submit(self):
        raise NotImplementedError("Implement in subclass")


class DepositWidget(BaseMoneyWidget):
    def __init__(self, navigator, back_callback):
        super().__init__("Deposit Funds", back_callback)
        self.navigator = navigator

    def submit(self):
        amt = self.amount.text().strip()
        pw = self.password.text().strip()
        if not amt or not pw:
            self.msg.setText("Fill amount and password.")
            return
        # TODO: validate amount numeric, check password, apply logic
        self.msg.setStyleSheet("color: #22C55E;")
        self.msg.setText(f"Deposit of ${amt} accepted.")
        # after success you may want to call back to refresh dashboard; simple back for now


class WithdrawWidget(BaseMoneyWidget):
    def __init__(self, navigator, back_callback):
        super().__init__("Withdraw Funds", back_callback)
        self.navigator = navigator

    def submit(self):
        amt = self.amount.text().strip()
        pw = self.password.text().strip()
        if not amt or not pw:
            self.msg.setText("Fill amount and password.")
            return
        # TODO: validate balance, check password
        self.msg.setStyleSheet("color: #22C55E;")
        self.msg.setText(f"Withdrawal of ${amt} processed.")