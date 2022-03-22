from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit
import cleansky_LMSM.ui_to_py_by_qtdesigner.Login
import cleansky_LMSM.ui_to_py_by_qtdesigner.Management
import cleansky_LMSM.ui_to_py_by_qtdesigner.Menu


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
        QMessageBox.warning(self.ui.pushButton, 'Warning', 'permission denied', QMessageBox.Yes)


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
        # self.setup_combobox_organisation()
        # self.setup_table_users()
        # self.setup_table_administrator()
        pass

    def setup_combobox_organisation(self):
        self.ui.comboBox.setEditable(True)
        self.ui.comboBox.addItems(self.get_controller().action_fill_orga())
        self.ui.comboBox.setCurrentIndex(-1)
        self.ui.comboBox.currentTextChanged.connect(self.edited_orga)

    def setup_table_users(self):
        pass

    def setup_table_administrator(self):
        pass

    def edited_orga(self, txt):
        pass
