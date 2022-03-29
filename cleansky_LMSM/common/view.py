from abc import ABC, abstractmethod
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QTableWidgetItem, QHeaderView
import cleansky_LMSM.ui_to_py_by_qtdesigner.Login
import cleansky_LMSM.ui_to_py_by_qtdesigner.Management
import cleansky_LMSM.ui_to_py_by_qtdesigner.Menu
import logging


# class TableModel(QtCore.QAbstractTableModel):
#     """
#     https://www.pythonguis.com/tutorials/modelview-architecture/
#     """
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
        logging.info('finish setup_ui()')
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

    @staticmethod
    def tools_setup_combobox(combobox_obj, items_init=None, func=None):
        combobox_obj.setEditable(True)
        if items_init is not None:
            combobox_obj.clear()
            combobox_obj.addItems(items_init)
            combobox_obj.setCurrentIndex(-1)
        if func is not None:
            combobox_obj.currentTextChanged.connect(func)

    @staticmethod
    def tools_setup_table(table_object, list_of_field=None, items_init=None):
        if list_of_field is not None:
            table_object.setColumnCount(len(list_of_field))
            table_object.setHorizontalHeaderLabels(list_of_field)
        if items_init is not None:
            table_object.setRowCount(len(items_init))
            table_object.setColumnCount(len(items_init[0]))
            for i in range(len(items_init)):
                for j in range(len(items_init[0])):
                    table_object.setItem(i, j, QTableWidgetItem(items_init[i][j]))
        table_object.horizontalHeader().setStretchLastSection(True)
        table_object.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


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
        self.ui.button_management.clicked.connect(self.open_management)
        self.ui.button_items_to_be_tested.clicked.connect(self.open_items_to_be_tested)
        # self.ui.button_list_of_test_means.clicked.connect()

    def open_management(self):
        self.get_controller().action_open_management()

    def open_items_to_be_tested(self):
        self.get_controller().action_open_items_to_be_tested()


class ManagementView(View):
    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Management.Ui_MainWindow()

    def setup_ui_user_management(self):
        self.setup_combobox_organisation()
        self.setup_combobox_username()
        self.setup_table_users()
        self.setup_table_crud_users()
        self.setup_table_user_right()
        self.setup_table_administrator()

    def setup_ui_users_allocation(self):
        self.setup_combobox_coating_name()
        self.setup_combobox_detergent_name()
        self.setup_combobox_insect()
        self.setup_combobox_test_type_means()
        self.setup_combobox_tank()
        self.setup_combobox_sensor()
        self.setup_combobox_acqui_sys()
        self.setup_combobox_ejector()
        self.setup_combobox_camera()
        self.setup_combobox_teams()
        self.setup_combobox_test_point()
        self.setup_combobox_intrinsic_value()
        self.setup_combobox_rights()

    def setup_ui(self):
        """
        1.fill the organization combobox
        2.fill list of users & administrators
        3.reset new or modified or removed users
        ...
        """
        self.setup_ui_user_management()
        self.setup_ui_users_allocation()

    """
    https://www.geeksforgeeks.org/pyqt5-how-to-add-multiple-items-to-the-combobox/
    """

    def setup_combobox_organisation(self):
        View.tools_setup_combobox(self.ui.comboBox,
                                  self.get_controller().action_fill_organisation(),
                                  self.edited_organisation)

    def setup_combobox_username(self):
        View.tools_setup_combobox(self.ui.comboBox_2,
                                  func=self.edited_user_name)

    def setup_table_users(self):
        data = self.get_controller().action_fill_user_table()
        self.tools_setup_table(self.ui.tableWidget, items_init=data,
                               list_of_field=['orga', 'uname', 'email', 'fname', 'lname', 'tel'])
        """
        https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/
        If you want a table that uses your own data model you should use QTableView rather than this class.
        """
        # model = TableModel(data=data)
        # self.ui.tableWidget.setModel(model)

    def setup_table_crud_users(self):
        self.tools_setup_table(self.ui.tableWidget_6,
                               items_init=None,
                               list_of_field=['orga', 'uname', 'email', 'fname', 'lname', 'tel', 'new_pd', 'state'])

    def setup_table_user_right(self):
        self.tools_setup_table(self.ui.tableWidget_3, list_of_field=['elements_info', 'role_type'])

    def setup_table_administrator(self):
        data = self.get_controller().action_fill_table_admin()
        self.tools_setup_table(self.ui.tableWidget_4, items_init=data,
                               list_of_field=['elements_info', 'username'])

    def edited_organisation(self, txt):
        if txt != '':
            print(txt)
            data = self.get_controller().action_fill_username_combobox(txt)
            self.tools_setup_combobox(self.ui.comboBox_2, items_init=data)

    def edited_user_name(self, txt):
        if txt != '':
            print(txt)
            mat = self.get_controller().action_fill_user_right_table(txt)
            self.tools_setup_table(self.ui.tableWidget_3, items_init=mat)






    def setup_combobox_coating_name(self):
        View.tools_setup_combobox(self.ui.comboBox_6,
                                  self.get_controller().action_fill_coating(),
                                  self.edited_coating)

    def setup_combobox_detergent_name(self):
        View.tools_setup_combobox(self.ui.comboBox_7,
                                  self.get_controller().action_fill_detergent(),
                                  self.edited_detergent)

    def setup_combobox_insect(self):
        View.tools_setup_combobox(self.ui.comboBox_8,
                                  self.get_controller().action_fill_insect(),
                                  self.edited_insect)

    def setup_combobox_test_type_means(self):
        View.tools_setup_combobox(self.ui.comboBox_9,
                                  self.get_controller().action_fill_means(),
                                  self.edited_means)

    def setup_combobox_tank(self):
        View.tools_setup_combobox(self.ui.comboBox_12,
                                  self.get_controller().action_fill_tank(),
                                  self.edited_tank)

    def setup_combobox_sensor(self):
        View.tools_setup_combobox(self.ui.comboBox_13,
                                  self.get_controller().action_fill_sensor(),
                                  self.edited_sensor)

    def setup_combobox_acqui_sys(self):
        View.tools_setup_combobox(self.ui.comboBox_16,
                                  self.get_controller().action_fill_acqui(),
                                  self.edited_acqui)

    def setup_combobox_ejector(self):
        View.tools_setup_combobox(self.ui.comboBox_14,
                                  self.get_controller().action_fill_ejector(),
                                  self.edited_ejector)

    def setup_combobox_camera(self):
        View.tools_setup_combobox(self.ui.comboBox_15,
                                  self.get_controller().action_fill_camera(),
                                  self.edited_camera)

    def setup_combobox_teams(self):
        View.tools_setup_combobox(self.ui.comboBox_17,
                                  self.get_controller().action_fill_teams(),
                                  self.edited_teams)

    def setup_combobox_test_point(self):
        View.tools_setup_combobox(self.ui.comboBox_18,
                                  self.get_controller().action_test_points(),
                                  self.edited_points)

    def setup_combobox_intrinsic_value(self):
        View.tools_setup_combobox(self.ui.comboBox_19,
                                  self.get_controller().action_fill_intrinsic(),
                                  self.edited_intrinsic)

    def setup_combobox_rights(self):
        View.tools_setup_combobox(self.ui.comboBox_5,
                                  self.get_controller().action_fill_rights(),
                                  self.edited_rights)










    def edited_coating(self):
        pass

    def edited_detergent(self):
        pass

    def edited_insect(self):
        pass

    def edited_means(self):
        pass

    def edited_tank(self):
        pass

    def edited_sensor(self):
        pass

    def edited_acqui(self):
        pass

    def edited_ejector(self):
        pass

    def edited_camera(self):
        pass

    def edited_teams(self):
        pass

    def edited_points(self):
        pass

    def edited_intrinsic(self):
        pass

    def edited_rights(self):
        pass




class ItemsToBeTestedView(View):
    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Items_to_be_tested.Ui_MainWindow()

    def setup_ui(self):
        data = self.get_controller().action_fill_coating_name()
        self.tools_setup_combobox(self.ui.somboBox_11, data, self.edited_coating_name)

    def edited_coating_name(self):
        pass

    def edited_coating_position(self):
        pass
