from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt


class WithdrawPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        lbl = QLabel("Withdraw Funds")
        lbl.setStyleSheet("font-size: 22px; font-weight: bold; color: #FFFFFF;")
        layout.addWidget(lbl)

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Amount")
        layout.addWidget(self.amount_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        submit_btn = QPushButton("Submit")
        layout.addWidget(submit_btn)