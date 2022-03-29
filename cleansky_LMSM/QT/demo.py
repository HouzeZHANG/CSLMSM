from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import psycopg2
import sys

class widget1(QWidget) :
    def __init__(self, parent) :
        super(widget1, self).__init__(parent)
        self.line = QLineEdit(self)
        self.line.setGeometry(0,0,60,20)
        self.button = QPushButton('next', self)
        self.button.setGeometry(0,30,60,20)
        self.label = QLabel('widget 1', self)
        self.label.setGeometry(0,50,60,20)

    
class widget2(QWidget) :
    def __init__(self, parent) :
        super(widget2, self).__init__(parent)
        self.line = QLineEdit(self)
        self.line.setGeometry(0,0,60,20)
        self.button = QPushButton('back', self)
        self.button.setGeometry(0,30,60,20)
        self.label = QLabel('widget 2', self)
        self.label.setGeometry(0,50,60,20)

    
class App(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setGeometry(100, 200, 300, 200)
        self.startWidget1()
    
    def startWidget1(self) :
        self.widget1 = widget1(self)
        self.setWindowTitle('widget 1')
        self.setCentralWidget(self.widget1)
        self.widget1.button.installEventFilter(self)
        self.show()
    
    def startWidget2(self) :
        self.widget2 = widget2(self)
        self.setWindowTitle('widget 2')
        self.setCentralWidget(self.widget2)
        self.widget2.button.installEventFilter(self)
        self.show()

    def eventFilter(self, obj, event) :
        if obj == self.widget1.button :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                if self.widget1.line.text() == 'next' :
                    self.startWidget2()
                    print('to widget 2')
                else :
                    print('try again')
                return True
            return False
        if obj == self.widget2.button :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                if self.widget2.line.text() == 'back' :
                    self.startWidget1()
                    print('to widget 1')
                else :
                    print('try again')
                return True
            return False 
        return False

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())