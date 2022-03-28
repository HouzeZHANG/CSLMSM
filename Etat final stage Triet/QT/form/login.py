from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import psycopg2
import sys

class login(QWidget) :
    def __init__(self, parent) :
        super(QWidget, self).__init__(parent)
        self.connect()
        self.setupUI()
        
    def setupUI(self) :
        font = QFont('Arial', 16, QFont.Bold)
        label_login = QLabel('Login Form', self)
        label_login.setFont(font)
        label_login.setStyleSheet("background-color: Red;")
        label_login.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        label_login.setGeometry(400, 115, 300, 150)

        label_uname = QLabel('User name', self)
        label_uname.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label_uname.setGeometry(410, 285, 60, 20)
        self.username = QLineEdit(self)
        self.username.setPlaceholderText('Enter your user name')
        self.username.setGeometry(540, 285, 150, 20)
        splitter_password = QSplitter(Qt.Horizontal)

        label_password = QLabel('Password', self)
        label_password.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label_password.setGeometry(410, 315, 60, 20)
        self.password = QLineEdit(self)
        self.password.setPlaceholderText('Enter your password')
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setGeometry(540, 315, 150, 20)

        self.login_btn = QPushButton('Login', self)
        self.login_btn.setFont(font)
        self.login_btn.setGeometry(490, 365, 120, 40)

        

    def connect(self) :
        try :
            host = "localhost"
            username = "iventre"
            dbname = "lmsm"
            password = "lmsm"
            self.conn = psycopg2.connect(host = host, user = username, dbname = dbname, password = password)
            self.cur = self.conn.cursor()
        except psycopg2.Error as err:
            print(str(err))