import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import PyQt5
QApplication.setAttribute(PyQt5.QtCore.Qt.AA_EnableHighDpiScaling, True)


class LoginWindow(QDialog):
    def __init__(self, *args):
        super(LoginWindow, self).__init__(*args)
        loadUi('login.ui', self)

app = QApplication(sys.argv)
widget = LoginWindow()
widget.show()
sys.exit(app.exec_())
