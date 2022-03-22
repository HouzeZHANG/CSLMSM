from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QTableWidgetItem, QHeaderView
import cleansky_LMSM.ui_to_py_by_qtdesigner.Login
import cleansky_LMSM.ui_to_py_by_qtdesigner.Management
import cleansky_LMSM.ui_to_py_by_qtdesigner.Menu


# class TableModel(QtCore.QAbstractTableModel):
#     def __init__(self, data):
#         super(TableModel, self).__init__()
#         self._data = data
#
#     def data(self, index, role):
#         if role == Qt.DisplayRole:
#             # See below for the nested-list data structure.
#             # .row() indexes into the outer list,
#             # .column() indexes into the sub-list
#             return self._data[index.row()][index.column()]
#
#     def rowCount(self, index):
#         # The length of the outer list.
#         return len(self._data)
#
#     def columnCount(self, index):
#         # The following takes the first sub-list, and returns
#         # the length (only works if all rows are an equal length)
#         return len(self._data[0])


class View(ABC):
    def __init__(self, controller_obj=None) -> None:
        super().__init__()
        self.ui = self.get_ui()
        # View classes must have droit to access his controller by architecture MVC, otherwise we create a view object
        # without controller object just for doing an unittest
        self.__controller = controller_obj
        self.main_window = None

    def set_controller(self, controller_obj):
        """
        View classes must have droit to access his controller by architecture MVC
        """
        self.__controller = controller_obj

    def get_controller(self):
        return self.__controller

    def run_view(self):
        """
        template method for setup and display a GUI
        """
        self.main_window = QMainWindow()
        self.ui.setupUi(self.main_window)
        self.setup_ui()
        self.main_window.show()

    @abstractmethod
    def get_ui(self):
        """
        The configuration in the UI object plus the logical details in the setup_UI method make up the complete
        interface logic
        """
        pass

    @abstractmethod
    def setup_ui(self):
        """
        Any remaining logical details that are not implemented in QT designer will be implemented in this method
        """
        pass

    def main_window_close(self):
        self.main_window.close()

    def permission_denied(self):
        """
        未测试
        """
        # QMessageBox.warning(self.ui.pushButton, 'Warning', 'permission denied', QMessageBox.Yes)
        print("permission denied")
        pass


class LoginView(View):
    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Login.Ui_MainWindow()

    def setup_ui(self):
        self.ui.pushButton.clicked.connect(self.button_login_clicked)
        self.ui.lineEdit.setEchoMode(QLineEdit.Password)

    def button_login_clicked(self):
        self.get_controller().action_login()

    def get_username(self):
        return self.ui.lineEdit_2.text()

    def get_password(self):
        return self.ui.lineEdit.text()

    def login_fail(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        if QMessageBox.warning(self.ui.pushButton,
                               'login fail', 'wanna retry?',
                               QMessageBox.Yes | QMessageBox.No) == 65536:
            self.main_window.close()

    def login_success(self):
        self.main_window_close()


class MenuView(View):
    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Menu.Ui_MainWindow()

    def setup_ui(self):
        self.ui.pushButton.clicked.connect(self.open_management)

    def open_management(self):
        self.get_controller().action_open_management()

    def access_management_success(self):
        self.main_window_close()


class ManagementView(View):
    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Management.Ui_MainWindow()

    def setup_ui(self):
        """
        1.fill the organization combobox
        2.fill list of users & administrators
        3.reset new or modified or removed users
        """
        self.setup_combobox_organisation()
        self.setup_table_users()
        self.setup_table_crud_users()
        self.setup_table_user_right()
        self.setup_table_administrator()

    def setup_combobox_organisation(self):
        """
        https://www.geeksforgeeks.org/pyqt5-how-to-add-multiple-items-to-the-combobox/
        """
        self.ui.comboBox.setEditable(True)
        self.ui.comboBox.addItems(self.get_controller().action_fill_organisation())
        self.ui.comboBox.setCurrentIndex(-1)
        self.ui.comboBox.currentTextChanged.connect(self.edited_organisation)

    def setup_table_users(self):
        """
        """
        data = self.get_controller().action_fill_user_table()
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(len(data[0]))
        for i in range(len(data)):
            for j in range(len(data[0])):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(data[i][j]))
        self.ui.tableWidget.setHorizontalHeaderLabels(['orga', 'uname', 'email', 'fname', 'lname', 'tel'])
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        """
        https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/
        If you want a table that uses your own data model you should use QTableView rather than this class.
        """
        # model = TableModel(data=data)
        # self.ui.tableWidget.setModel(model)

    def setup_table_crud_users(self):
        self.ui.tableWidget_6.setColumnCount(8)
        self.ui.tableWidget_6.setHorizontalHeaderLabels(['orga', 'uname', 'email', 'fname',
                                                       'lname', 'tel', 'new_pd', 'state'])
        self.ui.tableWidget_6.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget_6.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def setup_table_user_right(self):
        self.ui.tableWidget_3.setColumnCount(8)
        self.ui.tableWidget_3.setHorizontalHeaderLabels(['orga', 'uname', 'email', 'fname',
                                                         'lname', 'tel', 'new_pd', 'state'])
        self.ui.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def setup_table_administrator(self):
        self.ui.tableWidget_4.setColumnCount(8)
        self.ui.tableWidget_4.setHorizontalHeaderLabels(['orga', 'uname', 'email', 'fname',
                                                       'lname', 'tel', 'new_pd', 'state'])
        self.ui.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def setup_combobox_user_name(self, organisation):
        pass

    def edited_organisation(self, txt):
        self.setup_combobox_user_name(txt)
