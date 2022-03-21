"""
一般在app运行的时候就对数据库建立连接，详见数据库连接池原理
"""
from cleansky_LMSM.common.program import Program
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QLineEdit
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    p = Program()
    p.run_login()
    sys.exit(app.exec_())
