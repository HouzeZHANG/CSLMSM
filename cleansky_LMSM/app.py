from cleansky_LMSM.common.program import Program
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication([])
    p = Program()
    sys.exit(app.exec_())
