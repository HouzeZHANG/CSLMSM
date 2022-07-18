"""
1. fixer le bug: user allocation
2. test execution: cherche les coatings, mettre position
3. 3小时飞行的数据怎么导入数据库
4. creation sur coating clicker plusieur fois validate or not ensuite
"""

from cleansky_LMSM.common import ProgramRunning
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication([])
    p = ProgramRunning()
    sys.exit(app.exec_())
