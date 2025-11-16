# theme.py
from PySide6.QtGui import QPalette, QColor

def set_dark_theme(app):
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(18, 18, 20))
    palette.setColor(QPalette.WindowText, QColor(230, 230, 230))
    palette.setColor(QPalette.Base, QColor(25, 25, 28))
    palette.setColor(QPalette.AlternateBase, QColor(30, 30, 33))
    palette.setColor(QPalette.ToolTipBase, QColor(230, 230, 230))
    palette.setColor(QPalette.ToolTipText, QColor(230, 230, 230))
    palette.setColor(QPalette.Text, QColor(230, 230, 230))
    palette.setColor(QPalette.Button, QColor(40, 40, 44))
    palette.setColor(QPalette.ButtonText, QColor(230, 230, 230))
    palette.setColor(QPalette.Highlight, QColor(0, 120, 215))
    palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
    app.setPalette(palette)

# Common sizes/colors
PRIMARY_BG = "#121214"
CARD_BG = "#1E1E22"
ACCENT = "#0A84FF"   # nice blue accent
DIM_TEXT = "#A8A8A8"
TEXT = "#EAEAEA"