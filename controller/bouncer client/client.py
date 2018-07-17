import sys, PyQt5, requests
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

QApplication.setAttribute(PyQt5.QtCore.Qt.AA_EnableHighDpiScaling, True)

api_version = "v2"
access_token = ""

class LoginWindow(QDialog):
    def __init__(self, *args):
        username = ""
        password = ""
        server = ""
        server = ""
        super(LoginWindow, self).__init__(*args)
        loadUi('login.ui', self)
        self.loginButton.clicked.connect(self.do_login)

    def get_info(self):
        self.username = self.usernameInput.text()
        self.password = self.passwordInput.text()
        self.server = self.serverInput.text()
        self.port = self.portInput.text()

    def do_login(self):
        global access_token
        self.get_info()
        host = "http://{}:{}".format(self.server, self.port)
        payload = (('username', self.username), ('password', self.password), ('grant_type', 'password'))
        try:
            data = requests.post("{}/{}/login".format(host,api_version), data=payload).json()
            if 'access_token' in data:
                access_token = data['access_token']
                self.statusLabel.setText("Good Login")
            else:
                self.statusLabel.setText(data['message'])
        except:
            self.statusLabel.setText("Connection Failed")

app = QApplication(sys.argv)
widget = LoginWindow()
widget.show()
sys.exit(app.exec_())
