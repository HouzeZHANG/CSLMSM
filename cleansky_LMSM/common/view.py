import sys
from abc import ABC, abstractmethod

from PyQt5.QtWidgets import QMainWindow, QApplication

import cleansky_LMSM.ui_to_py_by_qtdesigner.Login
import cleansky_LMSM.ui_to_py_by_qtdesigner.Management


class View(ABC):
    def __init__(self, controller_obj=None) -> None:
        super().__init__()
        self.ui = self.get_ui()
        # View classes must have droit to access his controller by architecture MVC, otherwise we create a view object
        # without controller object just for doing an unittest
        self.__controller = controller_obj

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
        app = QApplication(sys.argv)
        main_window = QMainWindow()
        self.ui.setupUi(main_window)
        self.setup_ui()
        main_window.show()
        sys.exit(app.exec_())

    def run_test_view(self):
        """
        template method for GUI test
        """
        app = QApplication(sys.argv)
        main_window = QMainWindow()
        self.ui.setupUi(main_window)
        main_window.show()
        sys.exit(app.exec_())

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


class LoginView(View):
    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Login.Ui_MainWindow()

    def setup_ui(self):
        self.ui.pushButton.clicked.connect(self.button_login_clicked)

    def button_login_clicked(self):
        self.get_controller().action_login()

    def get_username(self):
        return self.ui.lineEdit.text()

    def get_password(self):
        return self.ui.lineEdit_2.text()

    def login_fail(self, error_info):
        """
        登陆失败
        """
        pass

    def login_success(self, uname, role):
        """显示登录成功，等待连接数据。。。"""
        pass


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
        self.setup_table_administrator()

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
