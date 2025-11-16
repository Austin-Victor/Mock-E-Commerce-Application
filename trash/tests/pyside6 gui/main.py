# main.py
import sys
from PySide6.QtWidgets import QApplication, QStackedWidget, QWidget
from PySide6.QtCore import Qt

from theme import set_dark_theme
from onboarding import OnboardingWidget
from dashboard import DashboardWidget
from deposit_withdraw import DepositWidget, WithdrawWidget

class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("E-Commerce — App")
        self.resize(1100, 720)
        self.center_on_screen()

        # Pages (create but don't add dashboard until login)
        self.onboarding = OnboardingWidget(self)
        self.addWidget(self.onboarding)
        self.setCurrentWidget(self.onboarding)

        # references for later
        self.dashboard = None
        self.deposit = None
        self.withdraw = None

    def center_on_screen(self):
        self.setWindowFlag(Qt.Window)
        screen = QApplication.primaryScreen()
        size = screen.size()
        w, h = 1100, 720
        x = (size.width() - w) // 2
        y = (size.height() - h) // 2
        self.setGeometry(x, y, w, h)

    # call after successful login/signup
    def login_success(self, user_obj: dict):
        # create dashboard if not created
        if not self.dashboard:
            self.dashboard = DashboardWidget(self, user_obj, navigator=self)
            self.addWidget(self.dashboard)
        else:
            self.dashboard.update_user(user_obj)

        # create deposit & withdraw pages
        if not self.deposit:
            self.deposit = DepositWidget(self, back_callback=lambda: self.animate_to(self.dashboard))
            self.addWidget(self.deposit)
        if not self.withdraw:
            self.withdraw = WithdrawWidget(self, back_callback=lambda: self.animate_to(self.dashboard))
            self.addWidget(self.withdraw)

        self.animate_to(self.dashboard)

    def animate_to(self, widget: QWidget):
        """Slide animation between current widget and target widget."""
        # Simple slide-left animation
        current = self.currentWidget()
        if current is widget:
            return
        # add widget to stack if not present
        if self.indexOf(widget) == -1:
            self.addWidget(widget)

        # position target to the right initially
        w_geo = self.geometry()
        widget.setGeometry(w_geo.x() + w_geo.width(), w_geo.y(), w_geo.width(), w_geo.height())
        widget.show()

        # animate current out to left and target in from right
        from PySide6.QtCore import QPropertyAnimation, QPoint
        anim_out = QPropertyAnimation(current, b"pos", self)
        anim_out.setDuration(350)
        anim_out.setStartValue(current.pos())
        anim_out.setEndValue(current.pos() - QPoint(w_geo.width(), 0))

        anim_in = QPropertyAnimation(widget, b"pos", self)
        anim_in.setDuration(350)
        anim_in.setStartValue(widget.pos())
        anim_in.setEndValue(current.pos())

        def on_done():
            self.setCurrentWidget(widget)
            # reset positions to not break layout managers
            widget.move(w_geo.x(), w_geo.y())
        # run both
        anim_out.finished.connect(on_done)
        anim_out.start()
        anim_in.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    set_dark_theme(app)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())