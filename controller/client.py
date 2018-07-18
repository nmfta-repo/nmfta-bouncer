#!/usr/bin/python

import sys, PyQt5, requests
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMenuBar, QMainWindow
from PyQt5.uic import loadUi

QApplication.setAttribute(PyQt5.QtCore.Qt.AA_EnableHighDpiScaling, True)

api_version = "v2"
access_token = ""
server = ""
port = ""
host = ""
if len(sys.argv) > 1:
    server = sys.argv[1]
    port = sys.argv[2]
    host = "http://{}:{}".format(server, port)


app = QApplication(sys.argv)

class LoginWindow(QMainWindow):
    def __init__(self, *args):
        global server, port
        username = ""
        password = ""
        super(LoginWindow, self).__init__(*args)
        loadUi('resources/login.ui', self)
        if server is not "" and port is not "":
            self.serverInput.setText(server)
            self.portInput.setText(port)
        self.loginButton.clicked.connect(self.do_login)
        self.usernameInput.returnPressed.connect(self.do_login)
        self.passwordInput.returnPressed.connect(self.do_login)
        self.serverInput.returnPressed.connect(self.do_login)
        self.portInput.returnPressed.connect(self.do_login)

    def get_info(self):
        global server, port, host
        self.username = self.usernameInput.text()
        self.password = self.passwordInput.text()
        self.server = self.serverInput.text()
        self.port = self.portInput.text()
        server = self.server
        port = self.port
        host = "http://{}:{}".format(self.server, self.port)

    def do_login(self):
        global access_token, host
        self.get_info()
        payload = (('username', self.username), ('password', self.password), ('grant_type', 'password'))
        try:
            data = requests.post("{}/{}/login".format(host,api_version), data=payload, timeout=1).json()
            if 'access_token' in data:
                access_token = data['access_token']
                self.statusLabel.setText("Good Login")
                main.show()
                main.loadLists()
                self.close()
            else:
                self.statusLabel.setText(data['message'])
        except:
            self.statusLabel.setText("Connection Failed")

class MainWindow(QMainWindow):

    global access_token,host

    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)
        loadUi('resources/main.ui', self)
        self.addButton.clicked.connect(self.addEntry)
        self.delButton.clicked.connect(self.delEntry)
        self.wlList.itemSelectionChanged.connect(self.itemSelected)
        self.blList.itemSelectionChanged.connect(self.itemSelected)

    def itemSelected(self):
        if not self.wlList.selectedItems() and not self.blList.selectedItems():
            self.delButton.setEnabled(False)
            self.modButton.setEnabled(False)
        else:
            self.delButton.setEnabled(True)
            self.modButton.setEnabled(True)

    def addEntry(self):
        add_entry.show()

    def delEntry(self):
        if self.wlList.selectedItems():
            self.delWLEntry()
        else:
            self.delBLEntry()

    def delWLEntry(self):
        ip = self.wlList.selectedItems()[0].text()
        payload = {'IPv4':ip}
        data = requests.post("{}/{}/whitelists/delete".format(host,api_version), data=payload, headers={"Authorization":"Bearer {}".format(access_token)}).json()
        self.loadLists()
        self.statusLabel.setText(data['Result']['Message'])

    def delBLEntry(self):
        ip = self.blList.selectedItems()[0].text()
        payload = {'IPv4':ip}
        data = requests.post("{}/{}/blacklists/delete".format(host,api_version), data=payload, headers={"Authorization":"Bearer {}".format(access_token)}).json()
        self.loadLists()
        self.statusLabel.setText(data['Result']['Message'])

    def loadLists(self):
        self.wlList.clear()
        data = requests.get("{}/{}/whitelists".format(host,api_version), headers={"Authorization":"Bearer {}".format(access_token)}).json()
        self.statusLabel.setText(data['Result']['Message'])
        self.wlList.addItems(data['IPAddresses'])
        self.blList.clear()
        data = requests.get("{}/{}/blacklists".format(host,api_version), headers={"Authorization":"Bearer {}".format(access_token)}).json()
        self.statusLabel.setText(data['Result']['Message'])
        self.blList.addItems(data['IPAddresses'])


class EntryWindow(QDialog):

    global access_token, host

    def __init__(self, *args):
        super(EntryWindow, self).__init__(*args)
        loadUi('resources/add_entry.ui', self)
        self.addButton.clicked.connect(self.addEntry)

    def addEntry(self):
        ip = self.entryInput.text()
        lst = "whitelists"
        self.entryInput.setText("")
        if self.blButton.isChecked():
            lst = "blacklists"
        comments = ""
        payload = (('IPv4',ip),('Comments',comments))
        data = requests.post("{}/{}/{}/create".format(host,api_version,lst), data=payload, headers={"Authorization":"Bearer {}".format(access_token)}).json()
        main.statusLabel.setText(data['Result']['Message'])
        self.close()
        main.loadLists()


login = LoginWindow()
main = MainWindow()
add_entry = EntryWindow()
login.show()
sys.exit(app.exec_())
