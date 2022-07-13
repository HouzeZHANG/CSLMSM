# from Exploitation_of_tests import *
# from Management import *
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from Login import *

# from Test_execution import *
# from Exploitation_of_tests import *
# from User_Query import *
# from List_of_configuration import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
