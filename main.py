import sys

from PyQt5.QtWidgets import QApplication
from core.ui.window import window


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = window()
    window.show()
    sys.exit(app.exec_())