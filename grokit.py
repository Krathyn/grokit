import sys

from pyngrok import conf,ngrok

from PyQt5 import QtGui
from PyQt5.QtWidgets import (
  QApplication,
  QLabel,
  QHBoxLayout,
  QMainWindow,
  QWidget,
  QPushButton,
  QLineEdit,
  QVBoxLayout,
  QGridLayout
)

def open_tunnel(port, ip_address):

    connect_to = ""
    if len(ip_address) == 0:
        connect_to = port
    else:
        connect_to = ip_address + ":" + port

    ngrok_tunnel = ngrok.connect(connect_to)

    return ngrok_tunnel


def close_tunnel(tunnel):
    ngrok.disconnect(tunnel)


def get_tunnel(ngrok_tunnel):

    tunnel_url = ngrok_tunnel.public_url

    return tunnel_url


def set_token_default(authtoken):

    conf.get_default().auth_token = authtoken

    return

class Window(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Grok it: v0.3")
        self.resize(400,100)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QGridLayout()
        self.centralWidget.setLayout(self.layout)
        self.setupUI()
        self.setTokenButton.clicked.connect(self.tokenButtonFunction)
        self.connectButton.clicked.connect(self.connectButtonFunction)
        self.disconnectButton.clicked.connect(self.disconnectButtonFunction)
        self.ngrok_tunnel = None

    def tokenButtonFunction(self):
        set_token_default(self.authTokenField.text())
        return

    def connectButtonFunction(self):
        self.ngrok_tunnel = open_tunnel(self.portField.text(),self.ip_addressField.text())
        self.tunnelName.setText(self.ngrok_tunnel.public_url)

    def disconnectButtonFunction(self):
        tunnelname = get_tunnel(self.ngrok_tunnel)
        close_tunnel(tunnelname)
        self.tunnelName.setText("")

    def setupUI(self):


        layout = QGridLayout()
        self.portLabel = QLabel("Port")
        self.ip_addressLabel = QLabel("IP Address")
        self.authTokenLabel = QLabel("AuthToken")
        self.tunnelNameLabel = QLabel("Public Address")
        self.tunnelName = QLineEdit("")
        self.tunnelName.setReadOnly(True)
        self.portField = QLineEdit()
        self.ip_addressField = QLineEdit()
        self.authTokenField = QLineEdit()
        self.connectButton = QPushButton("Connect")
        self.setTokenButton = QPushButton("Set Auth Token")
        self.disconnectButton = QPushButton("Disconnect")

        self.layout.addWidget(self.ip_addressLabel,0,0)
        self.layout.addWidget(self.ip_addressField,1,0)
        
        self.layout.addWidget(self.portLabel,0,1)
        self.layout.addWidget(self.portField,1,1)

        self.layout.addWidget(self.connectButton,2,0)

        self.layout.addWidget(self.disconnectButton,2,1)
                
        self.layout.addWidget(self.authTokenLabel,0,3)
        self.layout.addWidget(self.authTokenField,1,3)
        self.layout.addWidget(self.setTokenButton,2,3)
        self.layout.addWidget(self.tunnelNameLabel,3,0,1,3)
        self.layout.addWidget(self.tunnelName,4,0,1,3)
        return

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
