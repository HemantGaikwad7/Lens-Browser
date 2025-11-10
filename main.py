from PyQt5.QtWidgets import QApplication
from browser_ui import LensBrowser
import sys

def load_stylesheet(app):
    with open("assets/style.qss", "r") as f:
        style = f.read()
    app.setStyleSheet(style)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_stylesheet(app)
    window = LensBrowser()
    sys.exit(app.exec_())