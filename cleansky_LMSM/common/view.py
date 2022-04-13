from abc import ABC, abstractmethod

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QTableWidgetItem, QHeaderView, QAbstractItemView
import cleansky_LMSM.ui_to_py_by_qtdesigner.Login
import cleansky_LMSM.ui_to_py_by_qtdesigner.Management
import cleansky_LMSM.ui_to_py_by_qtdesigner.Menu
import cleansky_LMSM.ui_to_py_by_qtdesigner.Items_to_be_tested
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
    def __init__(self, controller_obj=None):
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
        # logging.info('finish setup_ui()')
        self.main_window.show()

    @abstractmethod
    def get_ui(self):
        pass

    @abstractmethod
    def setup_ui(self):
        pass

    def main_window_close(self):
        self.main_window.close()

    def permission_denied(self):
        # QMessageBox.warning(self.ui.pushButton, 'Warning', 'permission denied', QMessageBox.Yes)
        pass

    @staticmethod
    def tools_setup_combobox(combobox_obj, items_init=None, func=None):
        combobox_obj.clear()
        combobox_obj.setEditable(True)
        if items_init is not None:
            combobox_obj.addItems(items_init)
        combobox_obj.setCurrentIndex(-1)
        if func is not None:
            combobox_obj.currentTextChanged.connect(func)

    @staticmethod
    def tools_setup_table(table_widget_obj, mat=None, title=None, clicked_fun=None, double_clicked_fun=None):
        """
        clicked_fun 绑定点击事件
        """
        table_widget_obj.horizontalHeader().setStretchLastSection(True)
        table_widget_obj.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_widget_obj.setSelectionBehavior(1)
        if mat is not None:
            if title is not None:
                table_widget_obj.setColumnCount(len(mat[0]))
            table_widget_obj.setRowCount(len(mat))
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    # QTableWidgetItem必须传入string类型的数据，当传入浮点型数据的时候无法显示
                    if mat[i][j] is None:
                        table_widget_obj.setItem(i, j, QTableWidgetItem(mat[i][j]))
                    elif mat[i][j] is not str:
                        table_widget_obj.setItem(i, j, QTableWidgetItem(str(mat[i][j])))
                    else:
                        table_widget_obj.setItem(i, j, QTableWidgetItem(mat[i][j]))
        else:
            table_widget_obj.clear()
            table_widget_obj.setRowCount(0)
        if clicked_fun is not None:
            table_widget_obj.cellClicked[int, int].connect(clicked_fun)
        if double_clicked_fun is not None:
            table_widget_obj.cellDoubleClicked[int, int].connect(double_clicked_fun)
        if title is not None:
            # 这俩函数必须同时使用否则无法完成初始化
            table_widget_obj.setColumnCount(len(title))
            table_widget_obj.setHorizontalHeaderLabels(title)

    @staticmethod
    def tools_add_row_to_table(table_object, lis):
        row_position = table_object.rowCount()
        table_object.insertRow(row_position)
        for x in range(len(lis)):
            table_object.setItem(row_position, x, QTableWidgetItem(lis[x]))

    @staticmethod
    def tools_setup_list(list_object, lis=None, current_row_changed_fun=None):
        list_object.clear()
        if lis is not None:
            list_object.addItems(lis)
        if current_row_changed_fun is not None:
            list_object.currentRowChanged.connect(current_row_changed_fun)

    @abstractmethod
    def refresh(self):
        pass

    @staticmethod
    def tools_op_object(opacity, obj):
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(opacity)
        obj.setGraphicsEffect(op)

    def button_clicked_db_transfer(self):
        self.get_controller().action_submit()

    def button_clicked_cancel(self):
        self.get_controller().action_roll_back()
        self.refresh()


class LoginView(View):
    def refresh(self):
        pass

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
    def refresh(self):
        pass

    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Menu.Ui_MainWindow()

    def setup_ui(self):
        self.ui.pushButton.clicked.connect(self.open_management)
        self.ui.pushButton_3.clicked.connect(self.open_items_to_be_tested)

    def open_management(self):
        self.get_controller().action_open_management()

    def open_items_to_be_tested(self):
        self.get_controller().action_open_items_to_be_tested()

    def close_window(self):
        self.main_window_close()


class ManagementView(View):
    # 这个变量是用来保存当前选中的用户的名称的
    # 修改权限的条件是：知道元素的类型，元素的id，用户的id，权限的大小
    # 在修改mean的时候，必须确保元素id查找成功
    choose_person_name = None
    choose_element_type = None
    state = None

    def refresh(self):
        self.setup_table_users()
        self.setup_table_administrator()
        self.setup_table_user_right()

        self.setup_combobox_organisation()
        self.setup_combobox_username()
        self.setup_combobox_firstname()
        self.setup_combobox_last_name()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit.clear()
        self.ui.lineEdit_3.clear()

    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Management.Ui_MainWindow()

    def setup_ui_user_management(self):
        self.setup_combobox_organisation()
        self.setup_combobox_username()
        self.setup_combobox_firstname()
        self.setup_combobox_last_name()

        self.setup_table_users()
        self.setup_table_crud_users()
        self.setup_table_user_right()
        self.setup_table_administrator()

        self.setup_button_validate()
        self.setup_button_remove()
        self.setup_button_db_transfer()
        self.setup_button_cancel()

    def setup_ui_users_allocation(self):
        self.setup_combobox_coating_name()
        self.setup_combobox_detergent_name()
        self.setup_combobox_insect()
        self.setup_combobox_test_type_means()
        self.setup_combobox_test_means_name()
        self.setup_combobox_serial_number()
        self.setup_combobox_tank()
        self.setup_combobox_sensor()
        self.setup_combobox_acqui_sys()
        self.setup_combobox_ejector()
        self.setup_combobox_camera()
        self.setup_combobox_teams()
        self.setup_combobox_test_point()
        self.setup_combobox_intrinsic_value()
        self.setup_combobox_rights()

        self.setup_table_user_right_left()
        self.setup_list_user_right()
        self.setup_button_rights_validate()

        self.setup_button_db_transfer_2()
        self.setup_button_cancel_2()

    # def setup_tab_widget(self):
    #     self.ui.tabWidget.tabBarClicked.connect(self.handle_tab_bar_clicked)

    # def handle_tab_bar_clicked(self, index):
    #     if index == 1:
    #     #     界面1的数据将会自动提交
    #
    #     else:
    #     #     界面2的数据将会自动提交

    def setup_button_db_transfer_2(self):
        self.ui.pushButton_6.clicked.connect(self.button_db_transfer_2)

    def button_db_transfer_2(self):
        self.button_clicked_db_transfer()

        self.ui.comboBox_6.setCurrentIndex(-1)
        self.ui.comboBox_7.setCurrentIndex(-1)
        self.ui.comboBox_8.setCurrentIndex(-1)
        self.ui.comboBox_9.setCurrentIndex(-1)
        self.ui.comboBox_10.setCurrentIndex(-1)
        self.ui.comboBox_11.setCurrentIndex(-1)
        self.ui.comboBox_12.setCurrentIndex(-1)
        self.ui.comboBox_13.setCurrentIndex(-1)
        self.ui.comboBox_14.setCurrentIndex(-1)
        self.ui.comboBox_15.setCurrentIndex(-1)
        self.ui.comboBox_16.setCurrentIndex(-1)
        self.ui.comboBox_17.setCurrentIndex(-1)
        self.ui.comboBox_18.setCurrentIndex(-1)
        self.ui.comboBox_19.setCurrentIndex(-1)

    def setup_button_cancel_2(self):
        self.ui.pushButton_7.clicked.connect(self.button_clicked_cancel_2)

    def button_clicked_cancel_2(self):
        self.button_clicked_cancel()

        self.ui.comboBox_6.setCurrentIndex(-1)
        self.ui.comboBox_7.setCurrentIndex(-1)
        self.ui.comboBox_8.setCurrentIndex(-1)
        self.ui.comboBox_9.setCurrentIndex(-1)
        self.ui.comboBox_10.setCurrentIndex(-1)
        self.ui.comboBox_11.setCurrentIndex(-1)
        self.ui.comboBox_12.setCurrentIndex(-1)
        self.ui.comboBox_13.setCurrentIndex(-1)
        self.ui.comboBox_14.setCurrentIndex(-1)
        self.ui.comboBox_15.setCurrentIndex(-1)
        self.ui.comboBox_16.setCurrentIndex(-1)
        self.ui.comboBox_17.setCurrentIndex(-1)
        self.ui.comboBox_18.setCurrentIndex(-1)
        self.ui.comboBox_19.setCurrentIndex(-1)

    def setup_ui(self):
        """
        1.fill the organization combobox
        2.fill list of users & administrators
        3.reset new or modified or removed users
        """
        self.setup_ui_user_management()
        self.setup_ui_users_allocation()
        # self.setup_tab_widget()
        """
    https://www.geeksforgeeks.org/pyqt5-how-to-add-multiple-items-to-the-combobox/
    """
    def setup_combobox_organisation(self):
        View.tools_setup_combobox(self.ui.comboBox,
                                  self.get_controller().action_fill_organisation(),
                                  self.edited_organisation)

    def setup_combobox_username(self):
        View.tools_setup_combobox(self.ui.comboBox_2,
                                  func=self.edited_username)

    def setup_combobox_firstname(self):
        View.tools_setup_combobox(self.ui.comboBox_3)

    def setup_combobox_last_name(self):
        View.tools_setup_combobox(self.ui.comboBox_4)

    def setup_table_users(self):
        data = self.get_controller().action_fill_user_table()
        self.tools_setup_table(self.ui.tableWidget, mat=data, title=['orga', 'uname', 'email', 'fname', 'lname', 'tel'])
        """
        https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/
        If you want a table that uses your own data model you should use QTableView rather than this class.
        """

    def setup_table_crud_users(self):
        self.tools_setup_table(self.ui.tableWidget_6, title=['username', 'state'])

    def setup_table_user_right(self):
        self.tools_setup_table(self.ui.tableWidget_3, title=['element_type', 'element_info', 'role'])

    def setup_table_administrator(self):
        data = self.get_controller().action_fill_administrator_table()
        View.tools_setup_table(self.ui.tableWidget_4, mat=data, title=['element_type', 'element_info', 'admi_name'])

    def setup_button_validate(self):
        self.ui.pushButton_2.clicked.connect(self.button_clicked_validate)

    def setup_button_remove(self):
        self.ui.pushButton_3.clicked.connect(self.button_clicked_remove)

    def setup_button_db_transfer(self):
        self.ui.pushButton_5.clicked.connect(self.button_db_transfer_clicked)

    def button_db_transfer_clicked(self):
        self.button_clicked_db_transfer()
        self.setup_table_crud_users()

    def setup_button_cancel(self):
        self.ui.pushButton_4.clicked.connect(self.button_cancel_clicked)

    def button_cancel_clicked(self):
        self.button_clicked_cancel()
        self.setup_table_crud_users()

    def setup_button_new_password(self):
        self.ui.pushButton.clicked.connect(self.button_clicked_password)

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
                                  self.edited_means_type)

    def setup_combobox_test_means_name(self):
        View.tools_setup_combobox(self.ui.comboBox_10,
                                  func=self.edited_means_name)

    def setup_combobox_serial_number(self):
        View.tools_setup_combobox(self.ui.comboBox_11,
                                  func=self.edited_serial_number)

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
        self.ui.comboBox_5.setEditable(False)

    def add_table_user_modify(self, lis):
        self.tools_add_row_to_table(self.ui.tableWidget_6, lis)

    def edited_organisation(self, txt):
        user_list = self.get_controller().action_fill_user_list(txt)

        self.ui.comboBox_2.currentTextChanged.disconnect(self.edited_username)
        self.ui.comboBox_2.clear()
        View.tools_setup_combobox(self.ui.comboBox_2, items_init=user_list)
        self.ui.comboBox_2.currentTextChanged.connect(self.edited_username)

        # clear all wait to finished
        self.ui.tableWidget_3.clear()

    def edited_username(self, txt):
        if txt != '':
            print('username : ' + txt)
            mat = self.get_controller().action_fill_user_right_table(txt)
            # print(mat)
            self.update_user_rights_table(mat)

            fname, lname = self.get_controller().action_fill_fname_lname(txt)
            self.ui.comboBox_3.clear()
            View.tools_setup_combobox(self.ui.comboBox_3, items_init=fname)

            self.ui.comboBox_4.clear()
            View.tools_setup_combobox(self.ui.comboBox_4, items_init=lname)

    def edited_coating(self, txt):
        # self.ui.comboBox_6.setCurrentIndex(-1)
        self.ui.comboBox_7.setCurrentIndex(-1)
        self.ui.comboBox_8.setCurrentIndex(-1)
        self.ui.comboBox_9.setCurrentIndex(-1)
        self.ui.comboBox_10.setCurrentIndex(-1)
        self.ui.comboBox_11.setCurrentIndex(-1)
        self.ui.comboBox_12.setCurrentIndex(-1)
        self.ui.comboBox_13.setCurrentIndex(-1)
        self.ui.comboBox_14.setCurrentIndex(-1)
        self.ui.comboBox_15.setCurrentIndex(-1)
        self.ui.comboBox_16.setCurrentIndex(-1)
        self.ui.comboBox_17.setCurrentIndex(-1)
        self.ui.comboBox_18.setCurrentIndex(-1)
        self.ui.comboBox_19.setCurrentIndex(-1)
        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(1, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 1

    def edited_detergent(self, txt):
        self.ui.comboBox_6.setCurrentIndex(-1)
        # self.ui.comboBox_7.setCurrentIndex(-1)
        self.ui.comboBox_8.setCurrentIndex(-1)
        self.ui.comboBox_9.setCurrentIndex(-1)
        self.ui.comboBox_10.setCurrentIndex(-1)
        self.ui.comboBox_11.setCurrentIndex(-1)
        self.ui.comboBox_12.setCurrentIndex(-1)
        self.ui.comboBox_13.setCurrentIndex(-1)
        self.ui.comboBox_14.setCurrentIndex(-1)
        self.ui.comboBox_15.setCurrentIndex(-1)
        self.ui.comboBox_16.setCurrentIndex(-1)
        self.ui.comboBox_17.setCurrentIndex(-1)
        self.ui.comboBox_18.setCurrentIndex(-1)
        self.ui.comboBox_19.setCurrentIndex(-1)
        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(2, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 2

    def edited_insect(self, txt):
        self.ui.comboBox_6.setCurrentIndex(-1)
        self.ui.comboBox_7.setCurrentIndex(-1)
        # self.ui.comboBox_8.setCurrentIndex(-1)
        self.ui.comboBox_9.setCurrentIndex(-1)
        self.ui.comboBox_10.setCurrentIndex(-1)
        self.ui.comboBox_11.setCurrentIndex(-1)
        self.ui.comboBox_12.setCurrentIndex(-1)
        self.ui.comboBox_13.setCurrentIndex(-1)
        self.ui.comboBox_14.setCurrentIndex(-1)
        self.ui.comboBox_15.setCurrentIndex(-1)
        self.ui.comboBox_16.setCurrentIndex(-1)
        self.ui.comboBox_17.setCurrentIndex(-1)
        self.ui.comboBox_18.setCurrentIndex(-1)
        self.ui.comboBox_19.setCurrentIndex(-1)
        if txt != '':
            if txt == 'YES':
                txt = True
            if txt == 'NO':
                txt = False
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(10, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 10

    def edited_means_type(self, txt):
        self.ui.comboBox_6.setCurrentIndex(-1)
        self.ui.comboBox_7.setCurrentIndex(-1)
        self.ui.comboBox_8.setCurrentIndex(-1)
        # self.ui.comboBox_9.setCurrentIndex(-1)
        # self.ui.comboBox_10.setCurrentIndex(-1)
        # self.ui.comboBox_11.setCurrentIndex(-1)
        self.ui.comboBox_12.setCurrentIndex(-1)
        self.ui.comboBox_13.setCurrentIndex(-1)
        self.ui.comboBox_14.setCurrentIndex(-1)
        self.ui.comboBox_15.setCurrentIndex(-1)
        self.ui.comboBox_16.setCurrentIndex(-1)
        self.ui.comboBox_17.setCurrentIndex(-1)
        self.ui.comboBox_18.setCurrentIndex(-1)
        self.ui.comboBox_19.setCurrentIndex(-1)
        means_type = self.get_controller().action_fill_combobox_test_mean(txt)
        self.ui.comboBox_10.currentTextChanged.disconnect(self.edited_means_name)
        self.ui.comboBox_10.clear()
        View.tools_setup_combobox(self.ui.comboBox_10, items_init=means_type)
        self.ui.comboBox_10.currentTextChanged.connect(self.edited_means_name)
        self.choose_element_type = 0

        self.ui.comboBox_11.clear()

        self.tools_setup_table(self.ui.tableWidget_2, title=['username', 'role'])
        self.tools_setup_list(self.ui.listWidget)

    def edited_means_name(self, txt):
        self.ui.comboBox_6.setCurrentIndex(-1)
        self.ui.comboBox_7.setCurrentIndex(-1)
        self.ui.comboBox_8.setCurrentIndex(-1)
        # self.ui.comboBox_9.setCurrentIndex(-1)
        # self.ui.comboBox_10.setCurrentIndex(-1)
        # self.ui.comboBox_11.setCurrentIndex(-1)
        self.ui.comboBox_12.setCurrentIndex(-1)
        self.ui.comboBox_13.setCurrentIndex(-1)
        self.ui.comboBox_14.setCurrentIndex(-1)
        self.ui.comboBox_15.setCurrentIndex(-1)
        self.ui.comboBox_16.setCurrentIndex(-1)
        self.ui.comboBox_17.setCurrentIndex(-1)
        self.ui.comboBox_18.setCurrentIndex(-1)
        self.ui.comboBox_19.setCurrentIndex(-1)
        mean_type = self.ui.comboBox_9.currentText()
        means_serial = self.get_controller().action_fill_serial(mean_type, txt)
        self.ui.comboBox_11.currentTextChanged.disconnect(self.edited_serial_number)
        self.ui.comboBox_11.clear()
        View.tools_setup_combobox(self.ui.comboBox_11, items_init=means_serial, func=self.edited_serial_number)
        self.choose_element_type = 0

        self.tools_setup_table(self.ui.tableWidget_2, title=['username', 'role'])
        self.tools_setup_list(self.ui.listWidget)

    def edited_serial_number(self, txt):
        self.ui.comboBox_6.setCurrentIndex(-1)
        self.ui.comboBox_7.setCurrentIndex(-1)
        self.ui.comboBox_8.setCurrentIndex(-1)
        # self.ui.comboBox_9.setCurrentIndex(-1)
        # self.ui.comboBox_10.setCurrentIndex(-1)
        # self.ui.comboBox_11.setCurrentIndex(-1)
        self.ui.comboBox_12.setCurrentIndex(-1)
        self.ui.comboBox_13.setCurrentIndex(-1)
        self.ui.comboBox_14.setCurrentIndex(-1)
        self.ui.comboBox_15.setCurrentIndex(-1)
        self.ui.comboBox_16.setCurrentIndex(-1)
        self.ui.comboBox_17.setCurrentIndex(-1)
        self.ui.comboBox_18.setCurrentIndex(-1)
        self.ui.comboBox_19.setCurrentIndex(-1)
        test_mean_type = self.ui.comboBox_9.currentText()
        test_mean_name = self.ui.comboBox_10.currentText()
        if test_mean_type != '' and test_mean_name != '':
            print(test_mean_type + ' ' + test_mean_name + ' ' + txt)
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(0, (test_mean_type, test_mean_name, txt))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 0

    def edited_tank(self, txt):
        self.ui.comboBox_6.setCurrentIndex(-1)
        self.ui.comboBox_7.setCurrentIndex(-1)
        self.ui.comboBox_8.setCurrentIndex(-1)
        self.ui.comboBox_9.setCurrentIndex(-1)
        self.ui.comboBox_10.setCurrentIndex(-1)
        self.ui.comboBox_11.setCurrentIndex(-1)
        # self.ui.comboBox_12.setCurrentIndex(-1)
        self.ui.comboBox_13.setCurrentIndex(-1)
        self.ui.comboBox_14.setCurrentIndex(-1)
        self.ui.comboBox_15.setCurrentIndex(-1)
        self.ui.comboBox_16.setCurrentIndex(-1)
        self.ui.comboBox_17.setCurrentIndex(-1)
        self.ui.comboBox_18.setCurrentIndex(-1)
        self.ui.comboBox_19.setCurrentIndex(-1)
        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(3, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 3

    def edited_sensor(self, txt):
        self.ui.comboBox_6.setCurrentIndex(-1)
        self.ui.comboBox_7.setCurrentIndex(-1)
        self.ui.comboBox_8.setCurrentIndex(-1)
        self.ui.comboBox_9.setCurrentIndex(-1)
        self.ui.comboBox_10.setCurrentIndex(-1)
        self.ui.comboBox_11.setCurrentIndex(-1)
        self.ui.comboBox_12.setCurrentIndex(-1)
        # self.ui.comboBox_13.setCurrentIndex(-1)
        self.ui.comboBox_14.setCurrentIndex(-1)
        self.ui.comboBox_15.setCurrentIndex(-1)
        self.ui.comboBox_16.setCurrentIndex(-1)
        self.ui.comboBox_17.setCurrentIndex(-1)
        self.ui.comboBox_18.setCurrentIndex(-1)
        self.ui.comboBox_19.setCurrentIndex(-1)
        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(4, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 4

    def edited_acqui(self, txt):
        self.ui.comboBox_6.setCurrentIndex(-1)
        self.ui.comboBox_7.setCurrentIndex(-1)
        self.ui.comboBox_8.setCurrentIndex(-1)
        self.ui.comboBox_9.setCurrentIndex(-1)
        self.ui.comboBox_10.setCurrentIndex(-1)
        self.ui.comboBox_11.setCurrentIndex(-1)
        self.ui.comboBox_12.setCurrentIndex(-1)
        self.ui.comboBox_13.setCurrentIndex(-1)
        self.ui.comboBox_14.setCurrentIndex(-1)
        self.ui.comboBox_15.setCurrentIndex(-1)
        # self.ui.comboBox_16.setCurrentIndex(-1)
        self.ui.comboBox_17.setCurrentIndex(-1)
        self.ui.comboBox_18.setCurrentIndex(-1)
        self.ui.comboBox_19.setCurrentIndex(-1)
        if txt != '':
            if txt == 'YES':
                txt = True
            if txt == 'NO':
                txt = False
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(11, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 11

    def edited_ejector(self, txt):
        self.ui.comboBox_6.setCurrentIndex(-1)
        self.ui.comboBox_7.setCurrentIndex(-1)
        self.ui.comboBox_8.setCurrentIndex(-1)
        self.ui.comboBox_9.setCurrentIndex(-1)
        self.ui.comboBox_10.setCurrentIndex(-1)
        self.ui.comboBox_11.setCurrentIndex(-1)
        self.ui.comboBox_12.setCurrentIndex(-1)
        self.ui.comboBox_13.setCurrentIndex(-1)
        # self.ui.comboBox_14.setCurrentIndex(-1)
        self.ui.comboBox_15.setCurrentIndex(-1)
        self.ui.comboBox_16.setCurrentIndex(-1)
        self.ui.comboBox_17.setCurrentIndex(-1)
        self.ui.comboBox_18.setCurrentIndex(-1)
        self.ui.comboBox_19.setCurrentIndex(-1)
        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(5, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 5

    def edited_camera(self, txt):
        self.ui.comboBox_6.setCurrentIndex(-1)
        self.ui.comboBox_7.setCurrentIndex(-1)
        self.ui.comboBox_8.setCurrentIndex(-1)
        self.ui.comboBox_9.setCurrentIndex(-1)
        self.ui.comboBox_10.setCurrentIndex(-1)
        self.ui.comboBox_11.setCurrentIndex(-1)
        self.ui.comboBox_12.setCurrentIndex(-1)
        self.ui.comboBox_13.setCurrentIndex(-1)
        self.ui.comboBox_14.setCurrentIndex(-1)
        self.ui.comboBox_15.setCurrentIndex(-1)
        self.ui.comboBox_16.setCurrentIndex(-1)
        # self.ui.comboBox_17.setCurrentIndex(-1)
        self.ui.comboBox_18.setCurrentIndex(-1)
        self.ui.comboBox_19.setCurrentIndex(-1)
        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(6, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 6

    def edited_teams(self, txt):
        # self.ui.comboBox_6.setCurrentIndex(-1)
        self.ui.comboBox_7.setCurrentIndex(-1)
        self.ui.comboBox_8.setCurrentIndex(-1)
        self.ui.comboBox_9.setCurrentIndex(-1)
        self.ui.comboBox_10.setCurrentIndex(-1)
        self.ui.comboBox_11.setCurrentIndex(-1)
        self.ui.comboBox_12.setCurrentIndex(-1)
        self.ui.comboBox_13.setCurrentIndex(-1)
        self.ui.comboBox_14.setCurrentIndex(-1)
        self.ui.comboBox_15.setCurrentIndex(-1)
        self.ui.comboBox_16.setCurrentIndex(-1)
        self.ui.comboBox_17.setCurrentIndex(-1)
        self.ui.comboBox_18.setCurrentIndex(-1)
        self.ui.comboBox_19.setCurrentIndex(-1)
        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(9, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 9

    def edited_points(self, txt):
        self.ui.comboBox_6.setCurrentIndex(-1)
        self.ui.comboBox_7.setCurrentIndex(-1)
        self.ui.comboBox_8.setCurrentIndex(-1)
        self.ui.comboBox_9.setCurrentIndex(-1)
        self.ui.comboBox_10.setCurrentIndex(-1)
        self.ui.comboBox_11.setCurrentIndex(-1)
        self.ui.comboBox_12.setCurrentIndex(-1)
        self.ui.comboBox_13.setCurrentIndex(-1)
        self.ui.comboBox_14.setCurrentIndex(-1)
        self.ui.comboBox_15.setCurrentIndex(-1)
        self.ui.comboBox_16.setCurrentIndex(-1)
        self.ui.comboBox_17.setCurrentIndex(-1)
        # self.ui.comboBox_18.setCurrentIndex(-1)
        self.ui.comboBox_19.setCurrentIndex(-1)
        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(7, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 7

    def edited_intrinsic(self, txt):
        self.ui.comboBox_6.setCurrentIndex(-1)
        self.ui.comboBox_7.setCurrentIndex(-1)
        self.ui.comboBox_8.setCurrentIndex(-1)
        self.ui.comboBox_9.setCurrentIndex(-1)
        self.ui.comboBox_10.setCurrentIndex(-1)
        self.ui.comboBox_11.setCurrentIndex(-1)
        self.ui.comboBox_12.setCurrentIndex(-1)
        self.ui.comboBox_13.setCurrentIndex(-1)
        self.ui.comboBox_14.setCurrentIndex(-1)
        self.ui.comboBox_15.setCurrentIndex(-1)
        self.ui.comboBox_16.setCurrentIndex(-1)
        self.ui.comboBox_17.setCurrentIndex(-1)
        self.ui.comboBox_18.setCurrentIndex(-1)
        # self.ui.comboBox_19.setCurrentIndex(-1)
        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(8, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 8

    def edited_rights(self, txt):
        pass

    def button_clicked_validate(self):
        # 生成能满足要求的数据格式
        lis = []
        username = self.ui.comboBox_2.currentText()
        if username != '':
            orga = self.ui.comboBox.currentText()
            mail = self.ui.lineEdit.text()
            fname = self.ui.comboBox_3.currentText()
            lname = self.ui.comboBox_4.currentText()
            tel = self.ui.lineEdit_3.text()
            new_pd = self.ui.lineEdit_2.text()
            lis = [username, orga, fname, lname, tel, mail, new_pd]
            self.get_controller().action_validate_user(lis)
            self.setup_table_users()

    def button_clicked_remove(self):
        username = self.ui.comboBox_2.currentText()
        self.get_controller().action_delete_user(username)

        # self.get_controller().action_start_transaction()

    def button_clicked_password(self):
        pass

    def update_user_rights_table(self, mat):
        View.tools_setup_table(self.ui.tableWidget_3, mat)

    def user_right_row_left_clicked(self, i, j):
        # if self.ui.tableWidget_2.item(i, 0) is not None:
        self.choose_person_name = self.ui.tableWidget_2.item(i, 0).text()
        self.state = 0

    def user_right_row_right_clicked(self, i):
        if self.ui.listWidget.currentItem() is not None:
            self.choose_person_name = self.ui.listWidget.currentItem().text()
            self.state = 1
        else:
            self.choose_person_name = None
            self.state = None

    def setup_table_user_right_left(self):
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_2, title=['username', 'role'],
                               clicked_fun=self.user_right_row_left_clicked)

    def setup_list_user_right(self):
        self.tools_setup_list(list_object=self.ui.listWidget,
                              current_row_changed_fun=self.user_right_row_right_clicked)

    def setup_button_rights_validate(self):
        self.ui.pushButton_8.clicked.connect(self.setup_button_rights_validate_clicked)

    def setup_button_rights_validate_clicked(self):
        # 收集用户姓名，收集权限编号，收集元素类型，收集元素信息
        # 收集元素信息

        if self.choose_element_type is None or self.choose_person_name is None:
            # 报错，需要知道元素类型
            return

        element_info = {
            # means_type
            0: (self.ui.comboBox_9.currentText(), self.ui.comboBox_10.currentText(), self.ui.comboBox_11.currentText()),
            1: (self.ui.comboBox_6.currentText(),),
            2: (self.ui.comboBox_7.currentText(),),
            3: (self.ui.comboBox_6.currentText(),),
            4: (self.ui.comboBox_13.currentText(),),
            5: (self.ui.comboBox_14.currentText(),),
            6: (self.ui.comboBox_15.currentText(),),
            7: (self.ui.comboBox_18.currentText(),),
            8: (self.ui.comboBox_19.currentText(),),
            9: (self.ui.comboBox_17.currentText(),),
            10: (self.ui.comboBox_8.currentText(),),
            11: (self.ui.comboBox_16.currentText(),)
        }[self.choose_element_type]

        role_str = self.ui.comboBox_5.currentText()
        if role_str == '':
            return

        self.get_controller().action_change_role(self.choose_element_type, ref_tup=element_info,
                                                 person_name=self.choose_person_name,
                                                 role_str=role_str, state=self.state)

        owner_mat, other_list = self.get_controller().action_fill_user_right_list(self.choose_element_type,
                                                                                  element_info)
        self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
        self.tools_setup_list(self.ui.listWidget, other_list)


class ItemsToBeTestedView(View):
    coating_validate_token = None

    def __init__(self, controller_obj=None):
        super().__init__(controller_obj)
        self.message = QMessageBox()
        self.message.setText("Validate or not?")
        self.message.setWindowTitle("Warning!")
        self.message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # self.message.buttonClicked.connect(self.ans)


    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Items_to_be_tested.Ui_MainWindow()

    def setup_ui(self):
        self.setup_tab_coating()
        self.setup_tab_detergents()
        self.setup_tab_insects()
        self.disable_modify_coating()

    def setup_tab_coating(self):
        self.setup_combobox_coating()
        self.setup_combobox_position()
        self.setup_button_search()
        self.setup_button_create_coating()

        self.setup_table_coating()
        self.setup_db_transfer_coating()

    def setup_tab_detergents(self):
        pass

    def setup_tab_insects(self):
        pass

    def refresh(self):
        pass

    def setup_button_search(self):
        self.ui.pushButton_14.clicked.connect(self.button_clicked_search_coating)

    def setup_db_transfer_coating(self):
        self.ui.pushButton_12.clicked.connect(self.button_clicked_db_transfer)

    def setup_button_create_coating(self):
        self.ui.pushButton_15.clicked.connect(self.button_clicked_create_coating)

    def setup_table_coating(self):
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_4, title=['attribute', 'value', 'unity'],
                               clicked_fun=self.clicked_row_coating, double_clicked_fun=self.double_clicked_row_coating)

    def change_table_coating(self, mat):
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_4, mat=mat)

    def clicked_row_coating(self, i, j):
        """
        点击表格的某一行，将数据填入attribute，value和unity
        """
        attribute_name = self.ui.tableWidget_4.item(i, 0).text()
        value = self.ui.tableWidget_4.item(i, 1).text()
        unity = self.ui.tableWidget_4.item(i, 2).text()
        self.ui.comboBox_14.setCurrentText(attribute_name)
        self.ui.comboBox_13.setCurrentText(unity)
        self.ui.lineEdit_8.setText(value)

    def double_clicked_row_coating(self, i, j):
        coating_name = self.ui.comboBox_11.currentText()
        coating_number = self.ui.comboBox_12.currentText()
        attribute_name = self.ui.tableWidget_4.item(i, 0).text()
        value = self.ui.tableWidget_4.item(i, 1).text()
        unity = self.ui.tableWidget_4.item(i, 2).text()
        self.get_controller().action_delete_coating_attribute(coating_name, coating_number,
                                                              attribute_name, value, unity)

    # def button_clicked_search(self):
    #     if self.flag is 0:
    #         print("wait to be changed")
    #         op_0 = QtWidgets.QGraphicsOpacityEffect()
    #         op_0.setOpacity(0)
    #         self.ui.pushButton_15.setGraphicsEffect(op_0)
    #         print("changed")
    #         self.flag = 1
    #         print(self.flag)
    #     else:
    #         print("wait to be changed")
    #         op_05 = QtWidgets.QGraphicsOpacityEffect()
    #         op_05.setOpacity(0.5)
    #         self.ui.pushButton_15.setGraphicsEffect(op_05)
    #         print("changed")
    #         self.flag = 0
    #         print(self.flag)

    def setup_combobox_coating(self):
        data = self.get_controller().action_get_coatings()
        self.tools_setup_combobox(self.ui.comboBox_11, items_init=data, func=self.edited_combobox_coating)
        self.ui.comboBox_11.setEditable(False)

    def setup_combobox_position(self, items=None):
        self.tools_setup_combobox(self.ui.comboBox_12, func=self.edited_combobox_position, items_init=items)

    def setup_combobox_coating_chara(self):
        self.tools_setup_combobox(self.ui.comboBox_14, func=self.edited_combobox_coating_chara)

    def setup_combobox_coating_unity(self, items=None):
        self.tools_setup_combobox(self.ui.comboBox_13, func=self.edited_combobox_coating_unity, items_init=items)

    def setup_edit_line_coating_value(self):
        self.ui.lineEdit_8.clear()

    def edited_combobox_coating(self, txt):
        if txt != '':
            data = self.get_controller().action_get_coating_position(coating_type=txt)
            # print(data)
            self.ui.comboBox_12.currentTextChanged.disconnect(self.edited_combobox_position)
            self.ui.comboBox_12.clear()
            View.tools_setup_combobox(self.ui.comboBox_12, items_init=data)
            self.ui.comboBox_12.currentTextChanged.connect(self.edited_combobox_position)

    def edited_combobox_position(self, txt):
        if txt != '':
            coating_name = self.ui.comboBox_11.currentText()
            coating_number = txt
            chara, unity, mat = self.get_controller().action_configue_by_type_number(coating_name, coating_number)
            self.tools_setup_combobox(self.ui.comboBox_14, items_init=chara)
            self.tools_setup_combobox(self.ui.comboBox_13, items_init=unity)
            self.tools_setup_table(self.ui.tableWidget_4, mat=mat, title=['attribute', 'value', 'unity'])

    def edited_combobox_coating_chara(self, txt):
        pass

    def edited_combobox_coating_unity(self, txt):
        pass

    def edited_combobox_coating_value(self, txt):
        pass

    def button_clicked_search_coating(self):
        pass

    def button_clicked_create_coating(self):
        coating_name = self.ui.comboBox_11.currentText()
        coating_number = self.ui.comboBox_12.currentText()
        attribute_name = self.ui.comboBox_14.currentText()
        unity = self.ui.comboBox_13.currentText()
        value = self.ui.lineEdit_8.text()

        self.get_controller().action_create_coating(coating_name, coating_number, attribute_name, unity, value)
        # mat = self.get_controller().action_get_coating_table(coating_name, coating_number)
        # self.tools_setup_table(self.ui.tableWidget_4, mat=mat, title=['attribute', 'value', 'unity'])
        #
        # data = self.get_controller().action_get_coating_position(coating_type=coating_name)
        # self.ui.comboBox_12.currentTextChanged.disconnect(self.edited_combobox_position)
        # self.ui.comboBox_12.clear()
        # View.tools_setup_combobox(self.ui.comboBox_12, items_init=data)
        # self.ui.comboBox_12.currentTextChanged.connect(self.edited_combobox_position)

    def button_clicked_db_transfer_coating(self):
        pass

    def disable_modify_coating(self):
        self.tools_op_object(obj=self.ui.pushButton_14, opacity=0.5)
        self.ui.pushButton_14.clicked.disconnect()
        self.tools_op_object(obj=self.ui.pushButton_15, opacity=0.5)
        self.ui.pushButton_15.clicked.disconnect()
        self.tools_op_object(obj=self.ui.pushButton_12, opacity=0.5)
        self.ui.pushButton_12.clicked.disconnect()

    def enable_modify_coating(self):
        self.tools_op_object(obj=self.ui.pushButton_14, opacity=1)
        self.tools_op_object(obj=self.ui.pushButton_15, opacity=1)
        self.tools_op_object(obj=self.ui.pushButton_12, opacity=1)

        # self.ui.pushButton_14.clicked.disconnect()
        # self.ui.pushButton_15.clicked.disconnect()
        # self.ui.pushButton_12.clicked.disconnect()
        self.ui.pushButton_14.clicked.connect(self.button_clicked_search_coating)
        self.ui.pushButton_15.clicked.connect(self.button_clicked_create_coating)
        self.ui.pushButton_12.clicked.connect(self.button_clicked_db_transfer)

    def one_click_coating(self):
        self.coating_validate_token = False

    def question_for_validate_coating(self):
        self.coating_validate_token = True

    # def ans(self, i):
    #     print(i)

    def button_clicked_db_transfer(self):
        if self.coating_validate_token:
            res = self.message.exec_()
            print(res)
            if res == 1024:
                coating_name = self.ui.comboBox_11.currentText()
                coating_number = self.ui.comboBox_12.currentText()
                self.get_controller().action_validate_coating(coating_name, coating_number)
        self.get_controller().action_submit()
