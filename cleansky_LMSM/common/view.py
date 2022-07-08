from abc import ABC, abstractmethod

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QTableWidgetItem, QHeaderView, QFileDialog, QWidget, \
    QGridLayout, QPushButton, QLabel

import cleansky_LMSM.config.config as ccc

import cleansky_LMSM.tools.type_checker as tc

import cleansky_LMSM.ui_to_py_by_qtdesigner.Items_to_be_tested
import cleansky_LMSM.ui_to_py_by_qtdesigner.List_of_test_means
import cleansky_LMSM.ui_to_py_by_qtdesigner.Login
import cleansky_LMSM.ui_to_py_by_qtdesigner.Management
import cleansky_LMSM.ui_to_py_by_qtdesigner.Menu
import cleansky_LMSM.ui_to_py_by_qtdesigner.List_of_configuration
import cleansky_LMSM.ui_to_py_by_qtdesigner.Test_execution
import cleansky_LMSM.ui_to_py_by_qtdesigner.Exploitation_of_tests


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

class MyMainWindow(QMainWindow):
    def __init__(self, my_view):
        super().__init__()
        self.view = my_view

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.view.get_controller().action_close_window()


class View(ABC):
    """
    MVC架构的一部分，负责在qt层和controller层之间通讯
    View类负责实现所有视图层类的通用接口，负责标准化view对象创建的流程
    """

    def __init__(self, controller_obj=None):
        super().__init__()

        # validate box object
        self.vali_box = None

        self.ui = self.get_ui()
        # View classes must have droit to access his controller by architecture MVC, otherwise we create a view object
        # without controller object just for doing an unittest
        self.__controller = controller_obj
        self.main_window = None

        self.input_file_path = r'.\file_input'
        self.output_file_path = r'.\file_output'

    def set_controller(self, controller_obj):
        """View classes must have droit to access his controller by architecture MVC"""
        self.__controller = controller_obj

    def get_controller(self):
        return self.__controller

    def run_view(self):
        """
        template method for setup and display a GUI
        模板方法
        """
        self.main_window = MyMainWindow(self)
        self.ui.setupUi(self.main_window)
        self.setup_ui()
        self.main_window.show()

    @abstractmethod
    def get_ui(self):
        """从指定目录下调取ui对象的方法，该方法在View的构造器中被定义"""
        pass

    @abstractmethod
    def setup_ui(self):
        pass

    def main_window_close(self):
        self.main_window.close()

    def message_box(self, title: str, msg: str):
        QMessageBox.about(self.main_window, title, msg)

    def permission_denied(self):
        # QMessageBox.warning(self.ui.pushButton, 'Warning', 'permission denied', QMessageBox.Yes)
        pass

    @staticmethod
    def tools_setup_combobox(combobox_obj, items_init=None, func=None):
        """初始化combobox，items_init为初始化的combobox内容，func用于配置绑定的槽函数"""
        combobox_obj.clear()
        combobox_obj.setEditable(True)
        if not items_init:
            items_init = None
        if items_init is not None or items_init == []:
            # for item in items_init:
            # if type(item) is not str().__class__:
            #     item = str(item)
            combobox_obj.addItems(items_init)
        combobox_obj.setCurrentIndex(-1)
        if func is not None:
            combobox_obj.currentTextChanged.connect(func)

    @staticmethod
    def tools_setup_table(table_widget_obj, mat=None, title=None, clicked_fun=None, double_clicked_fun=None,
                          strategy=None):
        """初始化表格"""
        table_widget_obj.horizontalHeader().setStretchLastSection(True)
        table_widget_obj.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_widget_obj.setSelectionBehavior(1)
        if mat is not None and mat != []:
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
    def tools_set_table_color(table_object, i_index=None, j_index=None, color=QtGui.QColor(100, 100, 150)):
        try:
            if i_index is None and j_index is None:
                row_num = table_object.rowCount()
                col_num = table_object.columnCount()
                for i in range(row_num):
                    for j in range(col_num):
                        table_object.item(i, j).setBackground(color)
        except TypeError:
            pass

    @staticmethod
    def tools_add_row_to_table(table_object, lis):
        """向表格中追加一行"""
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
        """用于页面初始化"""
        pass

    @staticmethod
    def tools_op_object(opacity: float, obj):
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(opacity)
        obj.setGraphicsEffect(op)

    def button_clicked_db_transfer(self):
        """调用controller中的commit接口"""
        self.get_controller().action_submit()

    def button_clicked_cancel(self):
        """调用controller中的rollback接口"""
        self.get_controller().action_roll_back()

    @abstractmethod
    def handle_tab_bar_clicked(self, index):
        """该函数用于管理tab标签页切换"""
        pass

    @staticmethod
    def file_dialog(question: str, path_default: str) -> str:
        path = QFileDialog.getOpenFileName(caption=question, directory=path_default)[0]
        return path

    def vali_box_config(self, txt: str, title: str):
        # 初始化用来验证validate的窗口
        self.vali_box = QMessageBox()
        self.vali_box.setText(txt)
        self.vali_box.setWindowTitle(title)
        self.vali_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    @staticmethod
    def error_window(msg: str):
        QMessageBox.about(QWidget(), "Warning!", msg)

    @staticmethod
    def warning_window(msg: str):
        QMessageBox.about(QWidget(), "Warning!", msg)


# self.message.buttonClicked.connect(self.ans)
class LoginView(View):
    def handle_tab_bar_clicked(self, index):
        pass

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


class MenuView(View):
    def handle_tab_bar_clicked(self, index):
        pass

    def refresh(self):
        pass

    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Menu.Ui_MainWindow()

    def setup_ui(self):
        self.ui.pushButton.clicked.connect(self.open_management)
        self.ui.pushButton_3.clicked.connect(self.open_items_to_be_tested)
        self.ui.pushButton_4.clicked.connect(self.open_list_of_test_means)
        self.ui.pushButton_2.clicked.connect(self.open_list_of_configuration)
        self.ui.pushButton_5.clicked.connect(self.open_test_execution)
        self.ui.pushButton_6.clicked.connect(self.open_exploitation_of_test)

        uid = self.get_controller().get_role().get_uid()
        rg = self.get_controller().right_graph
        if uid not in rg.admin_set and uid not in rg.manager_set:
            # 禁用manager按钮
            self.tools_op_object(obj=self.ui.pushButton, opacity=0.5)
            self.ui.pushButton.clicked.disconnect(self.open_management)

    def open_management(self):
        self.get_controller().action_open_management()

    def open_items_to_be_tested(self):
        self.get_controller().action_open_items_to_be_tested()

    def open_list_of_test_means(self):
        self.get_controller().action_open_list_of_test_means()

    def open_list_of_configuration(self):
        self.get_controller().action_open_list_of_configuration()

    def open_test_execution(self):
        self.get_controller().action_open_test_execution()

    def open_exploitation_of_test(self):
        self.get_controller().action_open_exploitation_of_test()


class ManagementView(View):
    # 这个变量是用来保存当前选中的用户的名称的
    # 修改权限的条件是：知道元素的类型，元素的id，用户的id，权限的大小
    # 在修改mean的时候，必须确保元素id查找成功
    def __init__(self):
        super().__init__()
        # 存储当前编辑的多选框对象，用于配合setup_combobox_allocation函数使用
        self.combobox_object_set = None
        # 被点击选择的角色的姓名
        self.choose_person_name = None
        # 当前元素的类型
        self.choose_element_type = None
        # 当前点击的是左侧表格的成员，则state为0，右侧表格的成员，则state为1
        # 点击左侧表格意味着将用户踢出该element，右侧表格意味着将新用户纳入该元素
        self.state = None

    def cache_insect_widgets(self):
        """隐藏insect的权限编辑qt对象"""
        self.tools_op_object(opacity=0.5, obj=self.ui.tableWidget_2)
        self.tools_op_object(opacity=0.5, obj=self.ui.listWidget)
        self.tools_op_object(opacity=0.5, obj=self.ui.pushButton_8)
        self.tools_op_object(opacity=0.5, obj=self.ui.comboBox_5)

    def setup_combobox_allocation(self, *args):
        """
        很有意思的BUG
        当我在调用这个函数初始化其他combobox的时候，其他combobox的edited函数也会被调用，从而清除当前combobox中的内容
        传入不需要被初始化的多选框对象，作差集以初始化其他多选框

        解决方法，使用setCurrentText，将txt参数重新填到combobox中
        """
        others = self.combobox_object_set - set(args)
        for item in others:
            item.setCurrentIndex(-1)

    def refresh(self):
        pass

    def handle_tab_bar_clicked(self, index):
        if index == 0:
            self.setup_tab_user_management()
        elif index == 1:
            self.setup_tab_user_allocation()

    def setup_tab_user_allocation(self):
        self.tools_setup_combobox(self.ui.comboBox_6,
                                  items_init=self.get_controller().action_fill_simple_element('type_coating'))
        self.tools_setup_combobox(self.ui.comboBox_7,
                                  items_init=self.get_controller().action_fill_simple_element('type_detergent'))

        self.tools_setup_combobox(self.ui.comboBox_9,
                                  items_init=self.get_controller().action_fill_means())
        self.tools_setup_combobox(self.ui.comboBox_10)
        self.tools_setup_combobox(self.ui.comboBox_11)
        self.tools_setup_combobox(self.ui.comboBox_12,
                                  items_init=self.get_controller().action_fill_simple_element('type_tank'))
        self.tools_setup_combobox(self.ui.comboBox_13,
                                  items_init=self.get_controller().action_fill_simple_element('type_sensor'))
        self.tools_setup_combobox(self.ui.comboBox_14,
                                  items_init=self.get_controller().action_fill_simple_element('type_ejector'))
        self.tools_setup_combobox(self.ui.comboBox_15,
                                  items_init=self.get_controller().action_fill_simple_element('type_camera'))
        self.tools_setup_combobox(self.ui.comboBox_16,
                                  items_init=['Yes', 'No'])
        self.tools_setup_combobox(self.ui.comboBox_17,
                                  items_init=self.get_controller().action_fill_simple_element('test_team'))
        self.tools_setup_combobox(self.ui.comboBox_18,
                                  items_init=self.get_controller().action_fill_simple_element('type_test_point'))
        self.tools_setup_combobox(self.ui.comboBox_19,
                                  items_init=self.get_controller().action_fill_simple_element('type_intrinsic_value'))

        # 初始化表格列名
        self.tools_setup_table(self.ui.tableWidget_2, title=['username', 'role'])

        # insect配置
        rg = self.get_controller().right_graph
        # 如果是manager，可以编辑，True的时候，显示权限框，如果为False，隐藏权限框
        uid = self.get_controller().get_role().get_uid()
        if uid in rg.manager_set:
            # manager可以修改Insect
            self.tools_setup_combobox(self.ui.comboBox_8, items_init=['True', 'False'])
        else:
            # 如果不是manager，不可以编辑insect的值，唯独insect的administrator可以修改insect的权限
            self.tools_setup_combobox(self.ui.comboBox_8, items_init=[str(rg.insect)])
            self.ui.comboBox_8.setCurrentText(str(rg.insect))
            self.ui.comboBox_8.setEditable(False)
            # ？怎么修改？

        # 是否可以显示取决于insect的值
        self.edited_insect(str(rg.insect))

    def setup_tab_user_management(self):
        self.tools_setup_combobox(self.ui.comboBox, items_init=self.get_controller().action_fill_organisation())
        self.tools_setup_combobox(self.ui.comboBox_2)
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.tools_setup_combobox(self.ui.comboBox_3)
        self.tools_setup_combobox(self.ui.comboBox_4)
        self.ui.lineEdit_3.clear()

        # 填充用户表格
        data = self.get_controller().action_fill_user_table()
        self.tools_setup_table(self.ui.tableWidget, mat=data, title=['orga', 'uname', 'email', 'fname', 'lname', 'tel'],
                               clicked_fun=self.clicked_user_table)
        """
        https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/
        If you want a table that uses your own data model you should use QTableView rather than this class.
        """

        # 填充管理员表格
        data = self.get_controller().action_fill_administrator_table()
        View.tools_setup_table(self.ui.tableWidget_4, mat=data, title=['element_type', 'element_info', 'admi_name'])

        # user crud
        self.tools_setup_table(self.ui.tableWidget_6, title=['username', 'state'])

        # user right
        self.tools_setup_table(self.ui.tableWidget_3, title=['element_type', 'element_info', 'role'])

    def clicked_user_table(self, i, j):
        organisation = self.ui.tableWidget.item(i, 0).text()
        user_name = self.ui.tableWidget.item(i, 1).text()
        email = self.ui.tableWidget.item(i, 2).text()
        first_name = self.ui.tableWidget.item(i, 3).text()
        last_name = self.ui.tableWidget.item(i, 4).text()
        tele = self.ui.tableWidget.item(i, 5).text()
        self.ui.comboBox.setCurrentText(organisation)
        self.ui.comboBox_2.setCurrentText(user_name)
        self.ui.comboBox_3.setCurrentText(first_name)
        self.ui.comboBox_4.setCurrentText(last_name)
        self.ui.lineEdit.setText(email)
        self.ui.lineEdit_3.setText(tele)

    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Management.Ui_MainWindow()

    def button_db_transfer_tab1(self):
        self.button_clicked_db_transfer()
        self.setup_tab_user_management()

    def button_cancel_tab1(self):
        self.button_clicked_cancel()
        self.setup_tab_user_management()

    def button_db_transfer_tab2(self):
        self.button_clicked_db_transfer()
        self.setup_tab_user_allocation()

    def button_cancel_tab2(self):
        self.button_clicked_cancel()
        self.setup_tab_user_allocation()

    def setup_ui(self):
        self.combobox_object_set = {self.ui.comboBox_6, self.ui.comboBox_7, self.ui.comboBox_8, self.ui.comboBox_9,
                                    self.ui.comboBox_10, self.ui.comboBox_11, self.ui.comboBox_12, self.ui.comboBox_13,
                                    self.ui.comboBox_14, self.ui.comboBox_15, self.ui.comboBox_16, self.ui.comboBox_17,
                                    self.ui.comboBox_18, self.ui.comboBox_19}

        # 初始化tab
        self.ui.tabWidget.tabBarClicked.connect(self.handle_tab_bar_clicked)

        # 初始化user management
        self.ui.comboBox.currentTextChanged.connect(self.edited_organisation)
        self.ui.comboBox_2.currentTextChanged.connect(self.edited_username)
        self.ui.pushButton.clicked.connect(self.button_clicked_password)
        self.ui.pushButton_2.clicked.connect(self.button_clicked_validate)
        self.ui.pushButton_3.clicked.connect(self.button_clicked_remove)
        self.ui.pushButton_5.clicked.connect(self.button_db_transfer_tab1)
        self.ui.pushButton_4.clicked.connect(self.button_cancel_tab1)

        # 初始化user allocation
        self.ui.comboBox_6.currentTextChanged.connect(self.edited_coating)
        self.ui.comboBox_7.currentTextChanged.connect(self.edited_detergent)
        self.ui.comboBox_8.currentTextChanged.connect(self.edited_insect)
        self.ui.comboBox_9.currentTextChanged.connect(self.edited_means_type)
        self.ui.comboBox_10.currentTextChanged.connect(self.edited_means_name)
        self.ui.comboBox_11.currentTextChanged.connect(self.edited_serial_number)
        self.ui.comboBox_12.currentTextChanged.connect(self.edited_tank)
        self.ui.comboBox_13.currentTextChanged.connect(self.edited_sensor)
        self.ui.comboBox_14.currentTextChanged.connect(self.edited_ejector)
        self.ui.comboBox_15.currentTextChanged.connect(self.edited_camera)
        self.ui.comboBox_16.currentTextChanged.connect(self.edited_acqui)
        self.ui.comboBox_17.currentTextChanged.connect(self.edited_teams)
        self.ui.comboBox_18.currentTextChanged.connect(self.edited_points)
        self.ui.comboBox_19.currentTextChanged.connect(self.edited_intrinsic)

        View.tools_setup_combobox(self.ui.comboBox_5,
                                  self.get_controller().action_fill_rights(),
                                  self.edited_rights)
        self.ui.comboBox_5.setEditable(False)

        # validate 按钮初始化
        self.ui.pushButton_8.clicked.connect(self.button_rights_validate_clicked)
        # db_transfer和cancel初始化
        self.ui.pushButton_6.clicked.connect(self.button_db_transfer_tab2)
        self.ui.pushButton_7.clicked.connect(self.button_cancel_tab2)
        # 权限表格初始化
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_2,
                               clicked_fun=self.user_right_row_left_clicked)
        # others表格初始化
        self.tools_setup_list(list_object=self.ui.listWidget,
                              current_row_changed_fun=self.user_right_row_right_clicked)

        # 权限管理，manager有权限打开两个IHM，admin只有权限打开allocation
        uid = self.get_controller().get_role().get_uid()
        if uid in self.get_controller().right_graph.manager_set:
            self.setup_tab_user_management()
        elif uid in self.get_controller().right_graph.admin_set:
            self.ui.tabWidget.setTabVisible(0, False)
            self.ui.tabWidget.setCurrentIndex(1)
            self.setup_tab_user_allocation()

    """
    https://www.geeksforgeeks.org/pyqt5-how-to-add-multiple-items-to-the-combobox/
    """
    """
    https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/
    If you want a table that uses your own data model you should use QTableView rather than this class.
    """

    def add_table_user_modify(self, lis):
        """向增删改查用户的表格中添加一行记录"""
        self.tools_add_row_to_table(self.ui.tableWidget_6, lis)

    def edited_organisation(self, txt):
        user_list = self.get_controller().action_fill_user_list(txt)
        self.ui.comboBox_2.currentTextChanged.disconnect(self.edited_username)
        self.ui.comboBox_2.clear()
        View.tools_setup_combobox(self.ui.comboBox_2, items_init=user_list)
        self.ui.comboBox_2.currentTextChanged.connect(self.edited_username)

    def edited_username(self, txt):
        if txt != '':
            mat = self.get_controller().action_fill_user_right_table(txt)
            self.update_user_rights_table(mat)

            # 填充firstname和lastname
            first_name, last_name = self.get_controller().action_fill_f_name_l_name(txt)
            self.ui.comboBox_3.clear()
            View.tools_setup_combobox(self.ui.comboBox_3, items_init=first_name)
            self.ui.comboBox_4.clear()
            View.tools_setup_combobox(self.ui.comboBox_4, items_init=last_name)

            # 填充个人信息
            lis = self.get_controller().action_fill_user_info(txt)
            if lis is not None:
                self.ui.comboBox.setCurrentText(lis[0])
                self.ui.comboBox_2.setCurrentText(lis[1])
                self.ui.comboBox_3.setCurrentText(lis[3])
                self.ui.comboBox_4.setCurrentText(lis[4])
                self.ui.lineEdit.setText(lis[2])
                self.ui.lineEdit_3.setText(lis[5])

    def edited_coating(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_6)
        self.ui.comboBox_6.setCurrentText(txt)

        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(1, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 1

    def edited_detergent(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_7)
        self.ui.comboBox_7.setCurrentText(txt)

        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(2, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 2

    def edited_insect(self, txt):
        # 这个函数原则上只有manager可以调用
        if txt == 'false':
            # self.ui.tableWidget_2.set
            pass
        self.setup_combobox_allocation(self.ui.comboBox_8)
        self.ui.comboBox_8.setCurrentText(txt)

        if txt != '':
            if txt == 'Yes':
                txt = True
            if txt == 'No':
                txt = False
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(10, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 10

    def edited_means_type(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_9, self.ui.comboBox_10, self.ui.comboBox_11)
        self.ui.comboBox_9.setCurrentText(txt)

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
        self.setup_combobox_allocation(self.ui.comboBox_9, self.ui.comboBox_10, self.ui.comboBox_11)

        mean_type = self.ui.comboBox_9.currentText()
        # if mean_type == '':
        #     self.setup_tab_user_allocation()
        #     self.ui.comboBox_10.setCurrentText(txt)

        means_serial = self.get_controller().action_fill_serial(mean_type, txt)
        self.ui.comboBox_11.currentTextChanged.disconnect(self.edited_serial_number)
        self.ui.comboBox_11.clear()
        View.tools_setup_combobox(self.ui.comboBox_11, items_init=means_serial, func=self.edited_serial_number)
        self.choose_element_type = 0

        self.tools_setup_table(self.ui.tableWidget_2, title=['username', 'role'])
        self.tools_setup_list(self.ui.listWidget)

    def edited_serial_number(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_9, self.ui.comboBox_10, self.ui.comboBox_11)

        test_mean_type = self.ui.comboBox_9.currentText()
        test_mean_name = self.ui.comboBox_10.currentText()

        if test_mean_name == '' or test_mean_type == '':
            # 输入不合法就会重置页面，但是依然会将当前输入的内容保留
            self.setup_tab_user_allocation()
            self.ui.comboBox_9.setCurrentText(test_mean_type)
            self.ui.comboBox_10.setCurrentText(test_mean_name)

        if test_mean_type != '' and test_mean_name != '':
            print(test_mean_type + ' ' + test_mean_name + ' ' + txt)
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(0, (
                test_mean_type, test_mean_name, txt))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 0

    def edited_tank(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_12)
        self.ui.comboBox_12.setCurrentText(txt)

        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(3, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 3

    def edited_sensor(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_13)
        self.ui.comboBox_13.setCurrentText(txt)

        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(4, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 4

    def edited_acqui(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_16)
        self.ui.comboBox_16.setCurrentText(txt)

        if txt != '':
            if txt == 'Yes':
                txt = True
            if txt == 'No':
                txt = False
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(11, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 11

    def edited_ejector(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_14)
        self.ui.comboBox_14.setCurrentText(txt)

        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(5, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 5

    def edited_camera(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_15)
        self.ui.comboBox_15.setCurrentText(txt)

        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(6, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 6

    def edited_teams(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_17)
        self.ui.comboBox_17.setCurrentText(txt)

        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(9, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 9

    def edited_points(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_18)
        self.ui.comboBox_18.setCurrentText(txt)

        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(7, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 7

    def edited_intrinsic(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_19)
        self.ui.comboBox_19.setCurrentText(txt)

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
            organ = self.ui.comboBox.currentText()
            mail = self.ui.lineEdit.text()
            f_name = self.ui.comboBox_3.currentText()
            l_name = self.ui.comboBox_4.currentText()
            tel = self.ui.lineEdit_3.text()
            new_pd = self.ui.lineEdit_2.text()
            lis = [username, organ, f_name, l_name, tel, mail, new_pd]
            self.get_controller().action_validate_user(lis)
            self.setup_tab_user_management()

    def button_clicked_remove(self):
        username = self.ui.comboBox_2.currentText()
        self.get_controller().action_delete_user(username)
        self.setup_tab_user_management()

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

    def button_rights_validate_clicked(self):
        """权限分配validate按钮"""
        if self.choose_element_type is None or self.choose_person_name is None:
            # 不知道元素类型，直接返回
            return

        element_info = {
            # means_type
            0: (self.ui.comboBox_9.currentText(), self.ui.comboBox_10.currentText(), self.ui.comboBox_11.currentText()),
            1: (self.ui.comboBox_6.currentText(),),
            2: (self.ui.comboBox_7.currentText(),),
            3: (self.ui.comboBox_12.currentText(),),
            4: (self.ui.comboBox_13.currentText(),),
            5: (self.ui.comboBox_14.currentText(),),
            6: (self.ui.comboBox_15.currentText(),),
            7: (self.ui.comboBox_18.currentText(),),
            8: (self.ui.comboBox_19.currentText(),),
            9: (self.ui.comboBox_17.currentText(),),
            10: (self.ui.comboBox_8.currentText(),),
            11: (self.ui.comboBox_16.currentText(),)
        }[self.choose_element_type]

        # 当前所勾选的权限由role_str存储
        role_str = self.ui.comboBox_5.currentText()
        if role_str == '':
            # 如果啥都没选，直接返回
            return

        self.get_controller().change_role(self.choose_element_type, ref_tup=element_info,
                                          person_name=self.choose_person_name,
                                          role_str=role_str, state=self.state)

        owner_mat, other_list = self.get_controller().action_fill_user_right_list(self.choose_element_type,
                                                                                  element_info)

        self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
        self.tools_setup_list(self.ui.listWidget, other_list)


class ItemsToBeTestedView(View):
    coating_validate_token = None
    detergent_validate_token = None

    def __init__(self, controller_obj=None):
        super().__init__(controller_obj)

        # 初始化用来验证validate的窗口
        self.message = QMessageBox()
        self.message.setText("Validate or not?")
        self.message.setWindowTitle("Warning!")
        self.message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    def refresh(self):
        pass

    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Items_to_be_tested.Ui_MainWindow()

    def setup_ui(self):
        """因为使用了策略模式，所以在初始化的时候就把coating和detergent的信号和槽函数配置好，
        这样在切换页面的时候不用重复设置信号与槽函数"""
        self.setup_tab_widget()
        # element_type_name和number初始化
        self.tools_setup_combobox(self.ui.comboBox_11, func=self.edited_combobox_element_type)
        self.ui.comboBox_11.setEditable(False)
        self.tools_setup_combobox(self.ui.comboBox_5, func=self.edited_combobox_element_type)
        self.ui.comboBox_5.setEditable(False)
        self.tools_setup_combobox(self.ui.comboBox_12, func=self.edited_combobox_number)
        self.tools_setup_combobox(self.ui.comboBox_6, func=self.edited_combobox_number)

        # create
        self.ui.pushButton_15.clicked.connect(self.button_clicked_create_element)
        self.ui.pushButton_8.clicked.connect(self.button_clicked_create_element)

        # search
        self.ui.pushButton_14.clicked.connect(self.button_clicked_search)
        self.ui.pushButton_7.clicked.connect(self.button_clicked_search)

        # table
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_4, title=['attribute', 'value', 'unity'],
                               clicked_fun=self.clicked_row, double_clicked_fun=self.double_clicked_row)
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_2, title=['attribute', 'value', 'unity'],
                               clicked_fun=self.clicked_row, double_clicked_fun=self.double_clicked_row)

        # db_transfer
        self.ui.pushButton_12.clicked.connect(self.button_clicked_db_transfer)
        self.ui.pushButton_13.clicked.connect(self.button_clicked_cancel)
        self.ui.pushButton_5.clicked.connect(self.button_clicked_db_transfer)

        # insect 界面信号槽初始化
        self.ui.pushButton_11.clicked.connect(self.click_add_insect)
        self.ui.pushButton_9.clicked.connect(self.click_insect_cancel)
        self.ui.pushButton_10.clicked.connect(self.click_insect_db_transfer)

        self.setup_tab_coating_and_detergent()
        self.disable_modify()

        self.setup_tab_insects()

    def setup_tab_coating_and_detergent(self):
        if self.get_controller().tab_state is ccc.TabState.COATING:
            self.tools_setup_combobox(self.ui.comboBox_12)
            self.tools_setup_combobox(self.ui.comboBox_14)
            self.tools_setup_combobox(self.ui.comboBox_13)
            self.ui.lineEdit_8.clear()
            self.tools_setup_table(self.ui.tableWidget_4, title=['attribute', 'value', 'unity'])
        elif self.get_controller().tab_state is ccc.TabState.DETERGENT:
            self.tools_setup_combobox(self.ui.comboBox_6)
            self.tools_setup_combobox(self.ui.comboBox_8)
            self.tools_setup_combobox(self.ui.comboBox_7)
            self.ui.lineEdit_9.clear()
            self.tools_setup_table(self.ui.tableWidget_2, title=['attribute', 'value', 'unity'])
        self.setup_combobox_element_type()
        self.disable_modify()
        self.get_controller().print_state()

    def setup_tab_widget(self):
        self.ui.tabWidget.tabBarClicked.connect(self.handle_tab_bar_clicked)

    def handle_tab_bar_clicked(self, index):
        if index == 1:
            # change to tab detergent
            self.get_controller().tab_state = ccc.TabState.DETERGENT
            self.setup_tab_coating_and_detergent()
        elif index == 2:
            # change to tab insect
            self.get_controller().tab_state = ccc.TabState.INSECT
            self.get_controller().insect_state.refresh()
            self.setup_tab_insects()
        elif index == 0:
            # change to tab coating
            self.get_controller().tab_state = ccc.TabState.COATING
            self.setup_tab_coating_and_detergent()

    def setup_tab_insects(self):
        """负责insect的页面初始化"""
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()

        name, hemo_lymphe = self.get_controller().action_get_names_hm()
        self.tools_setup_combobox(self.ui.comboBox_9, items_init=name, func=self.edited_insect_name)
        self.tools_setup_combobox(self.ui.comboBox_10, items_init=hemo_lymphe, func=self.edited_insect_hemo)

        mat = self.get_controller().action_get_insect_table()
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_3,
                               title=['names', 'mass', 'altitude min', 'altitude max', 'length', 'width', 'thickness',
                                      'hemo', 'state'],
                               clicked_fun=self.click_one_insect,
                               double_clicked_fun=self.double_click_insect,
                               mat=mat)

    def click_insect_cancel(self):
        self.get_controller().insect_state.refresh()
        self.button_clicked_cancel()
        self.setup_tab_insects()

    def click_insect_db_transfer(self):
        self.get_controller().insect_state.refresh()
        self.button_clicked_db_transfer()
        self.setup_tab_insects()

    def click_add_insect(self):
        """和manager里创建新用户一致"""
        name = self.ui.comboBox_9.currentText()
        if name == '':
            return
        mass = self.ui.lineEdit.text()
        at_min = self.ui.lineEdit_2.text()
        at_max = self.ui.lineEdit_3.text()
        length = self.ui.lineEdit_5.text()
        width = self.ui.lineEdit_6.text()
        thick = self.ui.lineEdit_7.text()
        hemo = self.ui.comboBox_10.currentText()
        self.get_controller().action_add_insect(name=name, masse=mass, alt_min=at_min, alt_max=at_max, length=length,
                                                width=width, thickness=thick, hemolymphe=hemo,
                                                str_type=['name', 'hemolymphe'])
        self.setup_tab_insects()

    def click_one_insect(self, i):
        name = self.ui.tableWidget_3.item(i, 0).text()
        mass = self.ui.tableWidget_3.item(i, 1).text()
        at_min = self.ui.tableWidget_3.item(i, 2).text()
        at_max = self.ui.tableWidget_3.item(i, 3).text()
        length = self.ui.tableWidget_3.item(i, 4).text()
        width = self.ui.tableWidget_3.item(i, 5).text()
        thick = self.ui.tableWidget_3.item(i, 6).text()
        he_mo = self.ui.tableWidget_3.item(i, 7).text()
        self.ui.comboBox_9.setCurrentText(name)
        self.ui.comboBox_10.setCurrentText(he_mo)
        self.ui.lineEdit.setText(mass)
        self.ui.lineEdit_2.setText(at_min)
        self.ui.lineEdit_3.setText(at_max)
        self.ui.lineEdit_5.setText(length)
        self.ui.lineEdit_6.setText(width)
        self.ui.lineEdit_7.setText(thick)

    def double_click_insect(self, i, j):
        pass

    def edited_insect_name(self, txt):
        pass

    def edited_insect_hemo(self, txt):
        pass

    def refresh_table(self, mat, strategy=ccc.TabState.COATING):
        if strategy is ccc.TabState.COATING:
            self.tools_setup_table(table_widget_obj=self.ui.tableWidget_4, mat=mat)
        elif strategy is ccc.TabState.DETERGENT:
            self.tools_setup_table(table_widget_obj=self.ui.tableWidget_2, mat=mat)

    def clicked_row(self, i, j):
        """
        点击表格的某一行，将数据填入attribute，value和unity
        """
        if self.get_controller().tab_state is ccc.TabState.COATING:
            attribute_name = self.ui.tableWidget_4.item(i, 0).text()
            value = self.ui.tableWidget_4.item(i, 1).text()
            unity = self.ui.tableWidget_4.item(i, 2).text()
            self.ui.comboBox_14.setCurrentText(attribute_name)
            self.ui.comboBox_13.setCurrentText(unity)
            self.ui.lineEdit_8.setText(value)
        elif self.get_controller().tab_state is ccc.TabState.DETERGENT:
            attribute_name = self.ui.tableWidget_2.item(i, 0).text()
            value = self.ui.tableWidget_2.item(i, 1).text()
            unity = self.ui.tableWidget_2.item(i, 2).text()
            self.ui.comboBox_8.setCurrentText(attribute_name)
            self.ui.comboBox_7.setCurrentText(unity)
            self.ui.lineEdit_9.setText(value)

    def double_clicked_row(self, i, j):
        """双击表格的某一行，将attribute删除"""
        element_type_name, number, attribute_name, value, unity = '', '', '', '', ''
        if self.get_controller().tab_state is ccc.TabState.COATING:
            element_type_name = self.ui.comboBox_11.currentText()
            number = self.ui.comboBox_12.currentText()
            attribute_name = self.ui.tableWidget_4.item(i, 0).text()
            value = self.ui.tableWidget_4.item(i, 1).text()
            unity = self.ui.tableWidget_4.item(i, 2).text()
        elif self.get_controller().tab_state is ccc.TabState.DETERGENT:
            element_type_name = self.ui.comboBox_5.currentText()
            number = self.ui.comboBox_6.currentText()
            attribute_name = self.ui.tableWidget_2.item(i, 0).text()
            value = self.ui.tableWidget_2.item(i, 1).text()
            unity = self.ui.tableWidget_2.item(i, 2).text()

        self.get_controller().action_delete_element_attribute(element_type_name, number,
                                                              attribute_name, value, unity)

    def setup_combobox_element_type(self):
        data = self.get_controller().action_get_element_type()
        if self.get_controller().tab_state is ccc.TabState.COATING:
            self.tools_setup_combobox(self.ui.comboBox_11, items_init=data)
            self.ui.comboBox_11.setEditable(False)
        elif self.get_controller().tab_state is ccc.TabState.DETERGENT:
            self.tools_setup_combobox(self.ui.comboBox_5, items_init=data)
            self.ui.comboBox_5.setEditable(False)

    def fill_combobox_position(self, items=None):
        if self.get_controller().tab_state is ccc.TabState.COATING:
            self.tools_setup_combobox(self.ui.comboBox_12, items_init=items)
        elif self.get_controller().tab_state is ccc.TabState.DETERGENT:
            self.tools_setup_combobox(self.ui.comboBox_6, items_init=items)

    def setup_combobox_unity(self, items=None, strategy=ccc.TabState.COATING):
        if strategy is ccc.TabState.COATING:
            self.tools_setup_combobox(self.ui.comboBox_13, items_init=items)
        elif strategy is ccc.TabState.DETERGENT:
            self.tools_setup_combobox(self.ui.comboBox_7, items_init=items)

    def edited_combobox_element_type(self, txt):
        if txt != '':
            data = self.get_controller().action_get_element_position(element_type=txt)
            if self.get_controller().tab_state is ccc.TabState.COATING:
                self.ui.comboBox_12.currentTextChanged.disconnect(self.edited_combobox_number)
                self.ui.comboBox_12.clear()
                View.tools_setup_combobox(self.ui.comboBox_12, items_init=data)
                self.ui.comboBox_12.currentTextChanged.connect(self.edited_combobox_number)
            elif self.get_controller().tab_state is ccc.TabState.DETERGENT:
                self.ui.comboBox_6.currentTextChanged.disconnect(self.edited_combobox_number)
                self.ui.comboBox_6.clear()
                View.tools_setup_combobox(self.ui.comboBox_6, items_init=data)
                self.ui.comboBox_6.currentTextChanged.connect(self.edited_combobox_number)

    def edited_combobox_number(self, txt):
        if txt != '':
            element_type = ''
            if self.get_controller().tab_state is ccc.TabState.COATING:
                element_type = self.ui.comboBox_11.currentText()
            elif self.get_controller().tab_state is ccc.TabState.DETERGENT:
                element_type = self.ui.comboBox_5.currentText()
            number = txt
            chara, unity, mat = self.get_controller().action_config_by_type_number(element_type, number)
            if self.get_controller().tab_state is ccc.TabState.COATING:
                self.tools_setup_combobox(self.ui.comboBox_14, items_init=chara)
                self.tools_setup_combobox(self.ui.comboBox_13, items_init=unity)
                self.tools_setup_table(self.ui.tableWidget_4, mat=mat, title=['attribute', 'value', 'unity'])
            elif self.get_controller().tab_state is ccc.TabState.DETERGENT:
                self.tools_setup_combobox(self.ui.comboBox_8, items_init=chara)
                self.tools_setup_combobox(self.ui.comboBox_7, items_init=unity)
                self.tools_setup_table(self.ui.tableWidget_2, mat=mat, title=['attribute', 'value', 'unity'])

    def button_clicked_search(self):
        pass

    def button_clicked_create_element(self):
        element_type, number, attribute_name, unity, value = None, None, None, None, None
        if self.get_controller().tab_state is ccc.TabState.COATING:
            element_type = self.ui.comboBox_11.currentText()
            number = self.ui.comboBox_12.currentText()
            attribute_name = self.ui.comboBox_14.currentText()
            unity = self.ui.comboBox_13.currentText()
            value = self.ui.lineEdit_8.text()
        elif self.get_controller().tab_state is ccc.TabState.DETERGENT:
            element_type = self.ui.comboBox_5.currentText()
            number = self.ui.comboBox_6.currentText()
            attribute_name = self.ui.comboBox_8.currentText()
            unity = self.ui.comboBox_7.currentText()
            value = self.ui.lineEdit_9.text()

        self.get_controller().action_create_element(element_type, number, attribute_name, unity, value)

    def disable_modify(self):
        try:
            if self.get_controller().tab_state is ccc.TabState.COATING:
                self.tools_op_object(obj=self.ui.pushButton_14, opacity=0)
                self.ui.pushButton_14.clicked.disconnect(self.button_clicked_search)
                self.tools_op_object(obj=self.ui.pushButton_15, opacity=0)
                self.ui.pushButton_15.clicked.disconnect()
                self.tools_op_object(obj=self.ui.pushButton_12, opacity=0)
                self.ui.pushButton_12.clicked.disconnect()
                self.get_controller().flag_coating_enabled = False
            elif self.get_controller().tab_state is ccc.TabState.DETERGENT:
                self.tools_op_object(obj=self.ui.pushButton_7, opacity=0)
                self.ui.pushButton_7.clicked.disconnect()
                self.tools_op_object(obj=self.ui.pushButton_8, opacity=0)
                self.ui.pushButton_8.clicked.disconnect()
                self.tools_op_object(obj=self.ui.pushButton_5, opacity=0)
                self.ui.pushButton_5.clicked.disconnect()
                self.get_controller().flag_detergent_enabled = False
        except TypeError:
            pass

    def enable_modify(self):
        try:
            if self.get_controller().tab_state is ccc.TabState.COATING:
                self.tools_op_object(obj=self.ui.pushButton_14, opacity=1)
                self.tools_op_object(obj=self.ui.pushButton_15, opacity=1)
                self.tools_op_object(obj=self.ui.pushButton_12, opacity=1)
                self.ui.pushButton_14.clicked.connect(self.button_clicked_search)
                self.ui.pushButton_15.clicked.connect(self.button_clicked_create_element)
                self.ui.pushButton_12.clicked.connect(self.button_clicked_db_transfer)
                self.get_controller().flag_coating_enabled = True
            elif self.get_controller().tab_state is ccc.TabState.DETERGENT:
                self.tools_op_object(obj=self.ui.pushButton_7, opacity=1)
                self.tools_op_object(obj=self.ui.pushButton_8, opacity=1)
                self.tools_op_object(obj=self.ui.pushButton_5, opacity=1)
                self.ui.pushButton_7.clicked.connect(self.button_clicked_search)
                self.ui.pushButton_8.clicked.connect(self.button_clicked_create_element)
                self.ui.pushButton_5.clicked.connect(self.button_clicked_db_transfer)
                self.get_controller().flag_detergent_enabled = True
        except TypeError:
            pass

    def direct_commit(self, strategy):
        """
        用于维护view对象中的token
        让coating和detergent都直接提交，不询问是否validate
        参见question_for_validate方法
        """
        if strategy is ccc.TabState.COATING:
            self.coating_validate_token = False
        elif strategy is ccc.TabState.DETERGENT:
            self.detergent_validate_token = False

    def question_for_validate(self, strategy=ccc.TabState.COATING):
        """
        用于维护view对象中的token，在commit按钮按下之后，询问用户是否validate，参见direct_commit方法
        """
        if strategy is ccc.TabState.COATING:
            self.coating_validate_token = True
        elif strategy is ccc.TabState.DETERGENT:
            self.detergent_validate_token = True

    def button_clicked_db_transfer(self):
        if self.get_controller().tab_state is ccc.TabState.COATING:
            if self.coating_validate_token:
                res = self.message.exec_()
                if res == 1024:
                    coating_name = self.ui.comboBox_11.currentText()
                    coating_number = self.ui.comboBox_12.currentText()
                    self.get_controller().action_validate_element(coating_name, coating_number)
            # 对coating界面清空
        elif self.get_controller().tab_state is ccc.TabState.DETERGENT:
            if self.detergent_validate_token:
                res = self.message.exec_()
                if res == 1024:
                    detergent_name = self.ui.comboBox_5.currentText()
                    detergent_number = self.ui.comboBox_6.currentText()
                    self.get_controller().action_validate_element(detergent_name, detergent_number)
            # 对detergent界面清空
        self.get_controller().action_submit()

    def button_clicked_cancel(self):
        super().button_clicked_cancel()
        self.setup_tab_coating_and_detergent()

    def refresh_value(self, strategy=ccc.TabState.COATING):
        if strategy is ccc.TabState.COATING:
            self.ui.lineEdit_8.clear()
        elif strategy is ccc.TabState.DETERGENT:
            self.ui.lineEdit_9.clear()


class ListOfTestMeansView(View):
    means_validate_token = None
    ejector_or_camera = None

    def __init__(self, controller_obj=None):
        super().__init__(controller_obj)
        self.test_mean_table = [item.value for item in ccc.TestMeanAttribute]
        self.test_mean_param = [item.value for item in ccc.ParamTable]
        self.flag_modify = None

        # 初始化用来验证validate的窗口
        self.message = QMessageBox()
        self.message.setText("Validate or not?")
        self.message.setWindowTitle("Warning!")
        self.message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # self.message.buttonClicked.connect(self.ans)

        # template header for table sensor
        self.sensor_table_title = ['sensor_number', 'order', 'calibration', 'config or in store']
        # template header for table sensor param
        self.sensor_param_table_title = ['param', 'unity', 'x', 'y', 'z']
        self.sensor_state = [item.value for item in ccc.State]
        self.sensor_loc = [item.value for item in ccc.Loc]
        self.tank_table = [item.value for item in ccc.FieldTankPos]

    def handle_tab_bar_clicked(self, index):
        if index == 0:
            self.setup_tab_aircraft()
        elif index == 1:
            self.setup_tab_instrumentation()

    def handle_tab_bar_clicked_2(self, index):
        if index == 0:
            self.setup_tab_sensors()
        elif index == 1:
            self.setup_tab_tank()
        elif index == 2:
            self.setup_tab_ejector()
        elif index == 3:
            self.setup_tab_camera()
        elif index == 4:
            self.setup_tab_acq()

    def setup_tab_sensors(self):
        self.get_controller().sensor_type_token = None
        lis_sensor_type = self.get_controller().get_sensor_type()
        self.tools_setup_combobox(self.ui.comboBox_8, items_init=lis_sensor_type)
        self.ui.comboBox_8.setEditable(False)
        self.tools_setup_combobox(self.ui.comboBox_11, items_init=self.sensor_state)
        self.ui.comboBox_11.setEditable(False)
        self.tools_setup_combobox(self.ui.comboBox_9)
        self.tools_setup_combobox(self.ui.comboBox_10)
        self.tools_setup_combobox(self.ui.comboBox_13)
        self.tools_setup_combobox(self.ui.comboBox_14)
        self.tools_setup_combobox(self.ui.comboBox_15, items_init=['0', '1'])
        self.tools_setup_combobox(self.ui.comboBox_16, items_init=['0', '1'])
        self.tools_setup_combobox(self.ui.comboBox_17, items_init=['0', '1'])

        self.tools_setup_table(self.ui.tableWidget_3, title=self.sensor_table_title, mat=None)
        self.tools_setup_table(self.ui.tableWidget_4, title=self.sensor_param_table_title, mat=None)

    def setup_tab_tank(self):
        tank_ref = self.get_controller().tank_ref()
        self.tools_setup_combobox(self.ui.comboBox_18, items_init=tank_ref)
        self.ui.comboBox_18.setEditable(False)
        self.tools_setup_combobox(self.ui.comboBox_19)

        lis = self.get_controller().tank_sensor_coating_type()
        self.tools_setup_combobox(self.ui.comboBox_20, items_init=lis)
        self.tools_setup_combobox(self.ui.comboBox_22)
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()
        self.ui.lineEdit_9.clear()
        self.ui.lineEdit_10.clear()
        self.ui.lineEdit_11.clear()
        self.ui.lineEdit_12.clear()
        self.ui.lineEdit_13.clear()
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_5, mat=None,
                               title=self.tank_table)

        self.disable_modify_tank()

    def setup_tab_ejector(self):
        self.ejector_or_camera = 1

        lis = self.get_controller().ejector_type()
        self.tools_setup_combobox(self.ui.comboBox_23, items_init=lis)

        self.tools_setup_combobox(self.ui.comboBox_24, items_init=None)

        mat = self.get_controller().ejector_table()
        self.tools_setup_table(self.ui.tableWidget_9,
                               title=['ref', 'serial', 'V_min (m/s)', 'V_max (m/s)',
                                      'Ejection Axis', 'Insect vol (mm3)', 'nbr'],
                               mat=mat)

    def setup_tab_camera(self):
        self.ejector_or_camera = 0

        lis = self.get_controller().camera_type()
        self.tools_setup_combobox(self.ui.comboBox_25, items_init=lis)
        self.tools_setup_combobox(self.ui.comboBox_26, items_init=None)
        mat = self.get_controller().camera_table()
        self.tools_setup_table(self.ui.tableWidget_8,
                               title=['ref', 'serial', 'shutter speed min(fps)', 'shutter speed max(fps)', 'view axis',
                                      'height aperture(degree)', 'width aperture(degree)'],
                               mat=mat)

    def setup_tab_acq(self):
        pass

    def setup_tab_aircraft(self):
        # 初始化test_mean权限
        self.get_controller().test_mean_token = None
        self.get_controller().test_mean_validate = None

        self.tools_setup_combobox(self.ui.comboBox,
                                  items_init=self.get_controller().action_fill_means())
        self.ui.comboBox.setEditable(False)
        self.tools_setup_combobox(self.ui.comboBox_2)
        self.ui.comboBox_2.setEditable(False)
        self.tools_setup_combobox(self.ui.comboBox_3)
        self.ui.comboBox_3.setEditable(False)
        self.tools_setup_combobox(self.ui.comboBox_6)
        self.tools_setup_combobox(self.ui.comboBox_7)

        self.tools_setup_table(self.ui.tableWidget, mat=None, title=self.test_mean_table)
        self.tools_setup_table(self.ui.tableWidget_2, mat=None, title=self.test_mean_param)

        self.tools_setup_combobox(self.ui.comboBox_4)
        self.tools_setup_combobox(self.ui.comboBox_5)
        self.ui.lineEdit.clear()

        # 解绑create组件
        self.disable_modify_test_means(strategy=1)

        # 一些没用的组件
        self.tools_op_object(obj=self.ui.pushButton_4, opacity=0.5)

    def setup_tab_instrumentation(self):
        self.setup_tab_sensors()
        self.ui.tabWidget_2.setCurrentIndex(0)

    def refresh(self):
        pass

    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.List_of_test_means.Ui_MainWindow()

    def setup_ui(self):
        self.ui.tabWidget.tabBarClicked.connect(self.handle_tab_bar_clicked)
        self.ui.tabWidget_2.tabBarClicked.connect(self.handle_tab_bar_clicked_2)
        # Test means identification初始化
        self.ui.comboBox.currentTextChanged.connect(self.edited_means_type)
        self.ui.comboBox.setEditable(False)
        self.ui.comboBox_2.currentTextChanged.connect(self.edited_means_name)
        self.ui.comboBox_2.setEditable(False)
        self.ui.comboBox_3.currentTextChanged.connect(self.edited_serial_number)
        self.ui.comboBox_3.setEditable(False)

        self.ui.pushButton_3.clicked.connect(self.attr_create_clicked)
        self.ui.pushButton_4.clicked.connect(self.attr_search_clicked)
        self.ui.pushButton.clicked.connect(self.attr_cancel_clicked)
        self.ui.pushButton_2.clicked.connect(self.means_db_transfer_clicked)
        self.ui.pushButton_6.clicked.connect(self.param_create_clicked)
        self.ui.pushButton_5.clicked.connect(self.param_search_clicked)

        self.tools_setup_table(self.ui.tableWidget, title=['attributes', 'value', 'unity'],
                               clicked_fun=self.attr_table_clicked,
                               double_clicked_fun=self.attr_table_double_clicked)

        self.tools_setup_table(self.ui.tableWidget_2, title=['param', 'unity'],
                               clicked_fun=self.param_table_clicked,
                               double_clicked_fun=self.param_table_double_clicked)

        # instrument 初始化
        # tank 初始化
        self.ui.comboBox_18.currentTextChanged.connect(self.edited_tank_ref)
        self.ui.comboBox_19.currentTextChanged.connect(self.edited_tank_number)
        self.ui.comboBox_20.currentTextChanged.connect(self.edited_sc_type)
        self.ui.pushButton_13.clicked.connect(self.import_tank_pos)
        self.ui.pushButton_14.clicked.connect(self.pushed_add_tank_number)
        self.ui.pushButton_33.clicked.connect(self.tank_add_pos)
        self.ui.pushButton_28.clicked.connect(self.tank_cancel)
        self.ui.pushButton_31.clicked.connect(self.db_transfer_tank)
        self.ui.pushButton_35.clicked.connect(self.clicked_extraire_tank_pos)

        self.tools_setup_table(self.ui.tableWidget_5, clicked_fun=self.clicked_table_tank,
                               double_clicked_fun=self.double_clicked_table_tank)

        # initialization of tab sensor
        self.ui.comboBox_8.currentTextChanged.connect(self.edited_sensor_type)
        self.ui.comboBox_9.currentTextChanged.connect(self.edited_sensor_reference)
        self.ui.comboBox_10.currentTextChanged.connect(self.edited_sensor_number)

        self.ui.pushButton_9.clicked.connect(self.button_clicked_add_sensor)
        self.ui.pushButton_10.clicked.connect(self.button_clicked_calibration_sensor)
        self.ui.pushButton_11.clicked.connect(self.button_clicked_sensor_history)
        self.ui.pushButton_12.clicked.connect(self.button_clicked_add_param)
        self.ui.pushButton_32.clicked.connect(self.button_clicked_search_sensor)
        self.ui.pushButton_7.clicked.connect(self.button_clicked_cancel_sensor)
        self.ui.pushButton_8.clicked.connect(self.button_clicked_db_transfer_sensor)
        self.ui.pushButton_34.clicked.connect(self.button_clicked_add_sensor_ref)

        self.tools_setup_table(self.ui.tableWidget_3,
                               title=self.sensor_table_title,
                               clicked_fun=self.sensor_table_clicked,
                               double_clicked_fun=self.sensor_table_double_clicked)
        self.tools_setup_table(self.ui.tableWidget_4,
                               title=['param', 'unity', 'x', 'y', 'z'],
                               clicked_fun=self.param_table_sensor_clicked,
                               double_clicked_fun=self.param_table_sensor_double_clicked)

        # ejector初始化
        self.ui.comboBox_23.currentTextChanged.connect(self.camera_ejector_type_changed)
        self.ui.comboBox_24.currentTextChanged.connect(self.camera_ejector_number_changed)
        self.ui.pushButton_17.clicked.connect(self.add_ejector_camera)
        self.ui.pushButton_15.clicked.connect(self.cancel_ejector_camera)
        self.ui.pushButton_16.clicked.connect(self.db_transfer_ejector_camera)

        # camera初始化
        self.ui.comboBox_25.currentTextChanged.connect(self.camera_ejector_type_changed)
        self.ui.comboBox_26.currentTextChanged.connect(self.camera_ejector_number_changed)
        self.ui.pushButton_20.clicked.connect(self.add_ejector_camera)
        self.ui.pushButton_18.clicked.connect(self.cancel_ejector_camera)
        self.ui.pushButton_19.clicked.connect(self.db_transfer_ejector_camera)

        self.setup_tab_aircraft()

    def attr_create_clicked(self):
        """创建means的attributes"""
        if self.get_controller().test_mean_token is None:
            return
        if self.get_controller().test_mean_token <= 4 and not self.get_controller().test_mean_validate:
            # 权限检查
            means_type = self.ui.comboBox.currentText()
            means_name = self.ui.comboBox_2.currentText()
            means_number = self.ui.comboBox_3.currentText()
            attr = self.ui.comboBox_4.currentText()
            unity = self.ui.comboBox_5.currentText()
            value = self.ui.lineEdit.text()

            means = means_type, means_name, means_number
            attribute = attr, unity, value

            mat = self.get_controller().action_create_means_attr(means, attribute)
            self.refresh_table(mat=mat)

    def attr_search_clicked(self):
        pass

    def attr_cancel_clicked(self):
        self.get_controller().action_roll_back()
        self.setup_tab_aircraft()

    def param_search_clicked(self):
        if self.get_controller().test_mean_token is None:
            return
        if self.get_controller().test_mean_token <= 4 and not self.get_controller().test_mean_validate:
            path = self.file_dialog('choose param file to import', self.input_file_path)
            if path == '':
                return
            means_type = self.ui.comboBox.currentText()
            means_name = self.ui.comboBox_2.currentText()
            means_number = self.ui.comboBox_3.currentText()
            self.get_controller().action_delete_all_param_link((means_type, means_name, means_number))

            print("\nimport file path : " + path + "---;-)\n")
            self.get_controller().param_file_import((means_type, means_name, means_number), path)

            self.edited_serial_number(self.ui.comboBox_3.currentText())

    def param_create_clicked(self):
        """创建新param，并绑定该param和test_mean"""
        if self.get_controller().test_mean_token is None:
            return
        if self.get_controller().test_mean_token <= 4 and not self.get_controller().test_mean_validate:
            # 权限判断
            test_mean_type = self.ui.comboBox.currentText()
            test_mean_name = self.ui.comboBox_2.currentText()
            test_mean_number = self.ui.comboBox_3.currentText()

            param_name = self.ui.comboBox_6.currentText()
            unity_name = self.ui.comboBox_7.currentText()

            self.get_controller().action_param_link((test_mean_type, test_mean_name, test_mean_number),
                                                    (param_name, unity_name))
            self.edited_serial_number(self.ui.comboBox_3.currentText())

    def edited_means_type(self, txt):
        means_type = self.get_controller().action_fill_combobox_test_mean(txt)
        self.ui.comboBox_2.currentTextChanged.disconnect(self.edited_means_name)
        self.ui.comboBox_2.clear()
        View.tools_setup_combobox(self.ui.comboBox_2, items_init=means_type)
        self.ui.comboBox_2.currentTextChanged.connect(self.edited_means_name)
        self.ui.comboBox_2.setEditable(False)
        self.ui.comboBox_3.clear()

    def edited_means_name(self, txt):
        mean_type = self.ui.comboBox.currentText()
        means_serial = self.get_controller().action_fill_serial(mean_type, txt)
        self.ui.comboBox_3.currentTextChanged.disconnect(self.edited_serial_number)
        self.ui.comboBox_3.clear()

        View.tools_setup_combobox(self.ui.comboBox_3, items_init=means_serial, func=self.edited_serial_number)
        self.ui.comboBox_3.setEditable(False)

    def edited_serial_number(self, txt):
        test_mean_type = self.ui.comboBox.currentText()
        test_mean_name = self.ui.comboBox_2.currentText()

        if test_mean_type != '' and test_mean_name != '':
            ret = self.get_controller().action_get_attributes_and_params(test_mean_type, test_mean_name, txt)
            print(ret)
            chara_list, attr_unity_list, params_combobox, params_table = ret[0], ret[1], ret[2], ret[3]
            params_unity, attr = ret[4], ret[5]

            self.tools_setup_combobox(self.ui.comboBox_4, items_init=chara_list)
            self.tools_setup_combobox(self.ui.comboBox_5, items_init=attr_unity_list)
            self.tools_setup_combobox(self.ui.comboBox_6, items_init=params_combobox)
            self.tools_setup_combobox(self.ui.comboBox_7, items_init=params_unity)

            self.tools_setup_table(self.ui.tableWidget, mat=attr, title=self.test_mean_table)
            self.tools_setup_table(self.ui.tableWidget_2, title=self.test_mean_param, mat=params_table)

    def attr_table_clicked(self, i, j):
        attribute = self.ui.tableWidget.item(i, 0).text()
        value = self.ui.tableWidget.item(i, 1).text()
        unity = self.ui.tableWidget.item(i, 2).text()
        self.ui.comboBox_4.setCurrentText(attribute)
        self.ui.comboBox_5.setCurrentText(unity)
        self.ui.lineEdit.setText(value)

    def attr_table_double_clicked(self, i, j):
        """双击解绑某个attribute"""
        if self.get_controller().test_mean_token <= 4 and not self.get_controller().test_mean_validate:
            attribute = self.ui.comboBox_4.currentText(), self.ui.lineEdit.text(), self.ui.comboBox_5.currentText()
            mean = self.ui.comboBox.currentText(), self.ui.comboBox_2.currentText(), self.ui.comboBox_3.currentText()
            self.get_controller().action_delete_means_attr(mean, attribute)
            self.edited_serial_number(self.ui.comboBox_3.currentText())

            self.ui.comboBox_4.setCurrentText('')
            self.ui.comboBox_5.setCurrentText('')
            self.ui.lineEdit.setText('')

    def param_table_clicked(self, i, j):
        param = self.ui.tableWidget_2.item(i, 0).text()
        unity = self.ui.tableWidget_2.item(i, 1).text()
        self.ui.comboBox_6.setCurrentText(param)
        self.ui.comboBox_7.setCurrentText(unity)

    def param_table_double_clicked(self, i, j):
        """删除test_mean的param"""
        mean_type = self.ui.comboBox.currentText()
        mean_name = self.ui.comboBox_2.currentText()
        mean_number = self.ui.comboBox_3.currentText()

        param = self.ui.tableWidget_2.item(i, 0).text()
        unity = self.ui.tableWidget_2.item(i, 1).text()
        self.get_controller().action_delete_param((mean_type, mean_name, mean_number), (param, unity))

        # 更新
        self.edited_serial_number(self.ui.comboBox_3.currentText())

    def edited_sensor_type(self, txt):
        if txt != '':
            ret = self.get_controller().get_sensor_ref(sensor_type=txt)
            self.tools_setup_combobox(self.ui.comboBox_9, items_init=ret)
            self.tools_setup_table(self.ui.tableWidget_4, title=self.sensor_param_table_title)

            param_type = self.get_controller().get_sensor_param_combo()
            unity_type = self.get_controller().get_sensor_unity_combo()
            self.tools_setup_combobox(self.ui.comboBox_13, items_init=param_type)
            self.tools_setup_combobox(self.ui.comboBox_14, items_init=unity_type)
            self.tools_setup_combobox(self.ui.comboBox_10)

            self.tools_setup_combobox(self.ui.comboBox_10)
            self.ui.comboBox_11.setCurrentIndex(-1)
            self.tools_setup_table(self.ui.tableWidget_3, title=self.sensor_table_title)

    def edited_sensor_reference(self, txt):
        if txt != '':
            # 填充sensor number
            ret, table_sensor, sensor_param_table = self.get_controller().filled_sensor_ref(
                sensor_type=self.ui.comboBox_8.currentText(),
                sensor_ref=txt)
            self.tools_setup_combobox(self.ui.comboBox_10, items_init=ret)
            self.tools_setup_table(self.ui.tableWidget_3,
                                   title=self.sensor_table_title,
                                   mat=table_sensor)
            self.tools_setup_table(self.ui.tableWidget_4, title=self.sensor_param_table_title,
                                   mat=sensor_param_table)

            param_lis = self.get_controller().action_get_all_param()
            unity_lis = self.get_controller().action_get_all_unity()

            self.tools_setup_combobox(self.ui.comboBox_13, items_init=param_lis)
            self.tools_setup_combobox(self.ui.comboBox_14, items_init=unity_lis)

    def button_clicked_add_sensor_ref(self):
        sensor_type = self.ui.comboBox_8.currentText()
        sensor_ref = self.ui.comboBox_9.currentText()
        if sensor_type == '' or sensor_ref == '':
            return

        sensor_tup = (sensor_type, sensor_ref)
        self.get_controller().action_add_sensor_ref(sensor_tuple=sensor_tup)

        self.setup_tab_sensors()

    def edited_sensor_number(self, sensor_number):
        pass

    def sensor_table_clicked(self, i, j):
        """单击table，填充sensor的信息"""
        sensor_number = self.ui.tableWidget_3.item(i, 0).text()
        order = self.ui.tableWidget_3.item(i, 1).text()
        self.ui.comboBox_10.setCurrentText(sensor_number)
        self.ui.comboBox_11.setCurrentText(order)

    def sensor_table_double_clicked(self, i, j):
        """双击sensor table 删除该sensor"""
        sensor_number = self.ui.tableWidget_3.item(i, 0).text()
        sensor_type = self.ui.comboBox_8.currentText()
        sensor_ref = self.ui.comboBox_9.currentText()
        state_num, info = self.get_controller().delete_sensor((sensor_type, sensor_ref, sensor_number))
        self.warning_window(info)
        self.ui.comboBox_9.setCurrentText(sensor_ref)
        self.edited_sensor_reference(sensor_ref)

    def param_table_sensor_clicked(self, i, j):
        param = self.ui.tableWidget_4.item(i, 0).text()
        unity = self.ui.tableWidget_4.item(i, 1).text()
        x = self.ui.tableWidget_4.item(i, 2).text()
        y = self.ui.tableWidget_4.item(i, 3).text()
        z = self.ui.tableWidget_4.item(i, 4).text()
        self.ui.comboBox_13.setCurrentText(param)
        self.ui.comboBox_14.setCurrentText(unity)
        self.ui.comboBox_15.setCurrentText(x)
        self.ui.comboBox_16.setCurrentText(y)
        self.ui.comboBox_17.setCurrentText(z)

    def param_table_sensor_double_clicked(self, i, j):
        sensor_type = self.ui.comboBox_8.currentText()
        sensor_ref = self.ui.comboBox_9.currentText()
        param = self.ui.comboBox_13.currentText()
        unity = self.ui.comboBox_14.currentText()
        x = self.ui.comboBox_15.currentText()
        y = self.ui.comboBox_16.currentText()
        z = self.ui.comboBox_17.currentText()
        self.get_controller().action_delete_param_sensor(sensor_=(sensor_type, sensor_ref),
                                                         param_tup=(param, unity, [x, y, z]))

        self.edited_sensor_reference(self.ui.comboBox_9.currentText())

    def button_clicked_add_sensor(self):
        sensor_type = self.ui.comboBox_8.currentText()
        sensor_ref = self.ui.comboBox_9.currentText()
        sensor_number = self.ui.comboBox_10.currentText()
        sensor_order = self.ui.comboBox_11.currentText()

        for item in ccc.State:
            if sensor_order == item.value:
                sensor_order = item
        if sensor_order == '':
            sensor_order = ccc.State.ORDER

        if sensor_type == '' or sensor_ref == '':
            return

        sensor_tup = (sensor_type, sensor_ref, sensor_number)
        self.get_controller().add_sensor(sensor_tup, sensor_order)
        # sensor number, sensor order, sensor config, table：refresh
        self.edited_sensor_reference(self.ui.comboBox_9.currentText())

    def button_clicked_add_sensor_reference(self):
        pass

    def button_clicked_calibration_sensor(self):
        path = self.file_dialog(question='Select calibration format file', path_default='.')
        if path is None:
            return
        self.get_controller().action_import_calibration(path=path)

    def button_clicked_sensor_history(self):
        sensor_tup = [self.ui.comboBox_8, self.ui.comboBox_9, self.ui.comboBox_10]
        sensor_tup = [item.currentText() for item in sensor_tup]
        sensor_tup = tuple(sensor_tup)

        for item in sensor_tup:
            if item == '':
                self.warning_window("ERROR!\nSENSOR FORMAT INVALID!")
                return

        row_number = self.get_controller().action_sensor_history(sensor_tup=sensor_tup)

        if row_number == -1:
            self.warning_window("ERROR!\nSENSOR NOT EXIST!")
        else:
            self.warning_window("EXTRAIRE SUCCESS\nROW NUMBER: " + str(row_number))

    def button_clicked_search_sensor(self):
        pass

    def button_clicked_add_param(self):
        sensor_type = self.ui.comboBox_8.currentText()
        if sensor_type == '':
            return

        sensor_ref = self.ui.comboBox_9.currentText()
        if sensor_ref == '':
            return

        param = self.ui.comboBox_13.currentText()
        unity = self.ui.comboBox_14.currentText()
        x = self.ui.comboBox_15.currentText()
        y = self.ui.comboBox_16.currentText()
        z = self.ui.comboBox_17.currentText()
        self.get_controller().action_param_link_sensor(sensor_=(sensor_type, sensor_ref),
                                                       param_tup=(param, unity, [x, y, z]))
        self.edited_sensor_reference(sensor_ref)

    def button_clicked_cancel_sensor(self):
        self.button_clicked_cancel()
        self.setup_tab_sensors()

    def button_clicked_db_transfer_sensor(self):
        self.button_clicked_db_transfer()
        self.setup_tab_sensors()

    def means_db_transfer_clicked(self):
        if self.means_validate_token:
            res = self.message.exec_()
            if res == 1024:
                mean_type = self.ui.comboBox.currentText()
                mean_name = self.ui.comboBox_2.currentText()
                mean_number = self.ui.comboBox_3.currentText()
                self.get_controller().action_validate_mean((mean_type, mean_name, mean_number))
        self.get_controller().action_submit()
        self.setup_tab_aircraft()

    def refresh_table(self, mat):
        """在创建完attribute之后，更新IHM页面"""
        # 更新表格
        self.tools_setup_table(self.ui.tableWidget, title=['attributes', 'value', 'unity'], mat=mat)
        # 更新unity和attribute的combobox，通过直接调用该信号实现
        self.edited_serial_number(self.ui.comboBox_3.currentText())

    def enable_modify_test_means(self, strategy: int):
        try:
            if strategy == 1:
                if not self.get_controller().modify_flag or self.get_controller().modify_flag is None:
                    self.tools_op_object(obj=self.ui.pushButton_3, opacity=1)
                    self.tools_op_object(obj=self.ui.pushButton_2, opacity=1)
                    self.tools_op_object(obj=self.ui.pushButton_6, opacity=1)
                    self.ui.pushButton_3.clicked.connect(self.attr_create_clicked)
                    self.ui.pushButton_2.clicked.connect(self.means_db_transfer_clicked)
                    self.ui.pushButton_6.clicked.connect(self.param_create_clicked)
                    self.get_controller().modify_flag = True
        except TypeError:
            pass

    def disable_modify_test_means(self, strategy: int):
        try:
            if strategy == 1:
                if self.get_controller().modify_flag or self.get_controller().modify_flag is None:
                    self.tools_op_object(obj=self.ui.pushButton_3, opacity=0.5)
                    self.tools_op_object(obj=self.ui.pushButton_2, opacity=0.5)
                    self.tools_op_object(obj=self.ui.pushButton_6, opacity=0.5)
                    self.ui.pushButton_3.clicked.disconnect(self.attr_create_clicked)
                    self.ui.pushButton_2.clicked.disconnect(self.means_db_transfer_clicked)
                    self.ui.pushButton_6.clicked.disconnect(self.param_create_clicked)
                    self.get_controller().modify_flag = False
        except TypeError:
            pass

    def enable_modify_tank(self):
        try:
            # It's necessary to check the flag, because multiple connect will cause program errors
            if not self.get_controller().modify_flag_tank:
                self.tools_op_object(obj=self.ui.pushButton_14, opacity=1)
                self.tools_op_object(obj=self.ui.pushButton_33, opacity=1)
                self.tools_op_object(obj=self.ui.pushButton_13, opacity=1)
                self.tools_op_object(obj=self.ui.pushButton_31, opacity=1)
                self.ui.pushButton_14.clicked.connect(self.pushed_add_tank_number)
                self.ui.pushButton_33.clicked.connect(self.tank_add_pos)
                self.ui.pushButton_13.clicked.connect(self.import_tank_pos)
                self.ui.pushButton_31.clicked.connect(self.db_transfer_tank)
                self.get_controller().modify_flag_tank = True
        except TypeError:
            pass

    def disable_modify_tank(self):
        try:
            # The modification flag in the controller object is not checked here, because multiple disconnects will not
            # affect the program. On the contrary, multiple connections will affect the program.
            self.tools_op_object(obj=self.ui.pushButton_14, opacity=0.5)
            self.tools_op_object(obj=self.ui.pushButton_33, opacity=0.5)
            self.tools_op_object(obj=self.ui.pushButton_13, opacity=0.5)
            self.tools_op_object(obj=self.ui.pushButton_31, opacity=0.5)
            self.ui.pushButton_14.clicked.disconnect(self.pushed_add_tank_number)
            self.ui.pushButton_33.clicked.disconnect(self.tank_add_pos)
            self.ui.pushButton_13.clicked.disconnect(self.import_tank_pos)
            self.ui.pushButton_31.clicked.disconnect(self.db_transfer_tank)
            self.get_controller().modify_flag_tank = False
        except TypeError:
            pass

    def camera_ejector_type_changed(self, txt):
        if txt == '':
            return
        if self.ejector_or_camera == 1:
            ret = self.get_controller().ejector_num(txt)
            self.tools_setup_combobox(self.ui.comboBox_24, items_init=ret)
        elif self.ejector_or_camera == 0:
            ret = self.get_controller().camera_num(txt)
            self.tools_setup_combobox(self.ui.comboBox_26, items_init=ret)

    def add_ejector_camera(self):
        if self.ejector_or_camera == 1:
            self.get_controller().add_ejector()
        elif self.ejector_or_camera == 0:
            self.get_controller().add_camera()

    def cancel_ejector_camera(self):
        pass

    def db_transfer_ejector_camera(self):
        pass

    def camera_ejector_number_changed(self, txt):
        pass

    """tank"""

    def edited_tank_ref(self, txt):
        self.disable_modify_tank()
        if txt != '':
            tank_num = self.get_controller().tank_num(tank_ref=txt)
            self.tools_setup_combobox(self.ui.comboBox_19, items_init=tank_num)
            self.tools_setup_table(self.ui.tableWidget_5, title=self.tank_table)
            self.ui.comboBox_20.clear()
            self.ui.comboBox_22.clear()

    def edited_tank_number(self, txt):
        self.disable_modify_tank()
        if txt == '':
            return
        tank_type = self.ui.comboBox_18.currentText()
        tank_tup = (tank_type, txt)
        mat = self.get_controller().tank_num_edited(tank_tup=tank_tup)
        self.tools_setup_table(self.ui.tableWidget_5, mat=mat, title=self.tank_table)

        lis = self.get_controller().tank_sensor_coating_type()
        self.tools_setup_combobox(self.ui.comboBox_20, items_init=lis)
        self.tools_setup_combobox(self.ui.comboBox_22)
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()
        self.ui.lineEdit_9.clear()
        self.ui.lineEdit_10.clear()
        self.ui.lineEdit_11.clear()
        self.ui.lineEdit_12.clear()
        self.ui.lineEdit_13.clear()
        self.ui.comboBox_22.clear()

    def pushed_add_tank_number(self):
        tank_type = self.ui.comboBox_18.currentText()
        tank_number = self.ui.comboBox_19.currentText()
        if tank_type == '' or tank_number == '':
            return
        tank_tup = (tank_type, tank_number)
        self.get_controller().tank_add_num(tank_tup=tank_tup)
        self.setup_tab_tank()

    def import_tank_pos(self):
        tank_type = self.ui.comboBox_18.currentText()
        tank_number = self.ui.comboBox_19.currentText()
        if tank_type == '' or tank_number == '':
            return
        tank_tup = (tank_type, tank_number)

        path = self.file_dialog(question="choose geome file for tank", path_default=r'.\file_input')
        if path is None:
            self.warning_window("file invalid\n")

        msg, state = self.get_controller().tank_pos_import(tank_tup=tank_tup, path=path)
        if state:
            self.button_clicked_cancel()
        self.warning_window(msg)

        self.edited_tank_number(tank_number)

    def tank_add_pos(self):
        tank_type = self.ui.comboBox_18.currentText()
        num = self.ui.comboBox_19.currentText()

        tank_tup = (tank_type, num)

        tp = self.ui.comboBox_20.currentText()
        lo = self.ui.comboBox_22.currentText()
        x = self.ui.lineEdit_2.text()
        y = self.ui.lineEdit_3.text()
        z = self.ui.lineEdit_4.text()
        ux = self.ui.lineEdit_5.text()
        uy = self.ui.lineEdit_6.text()
        uz = self.ui.lineEdit_7.text()
        vx = self.ui.lineEdit_8.text()
        vy = self.ui.lineEdit_9.text()
        vz = self.ui.lineEdit_10.text()
        nx = self.ui.lineEdit_11.text()
        ny = self.ui.lineEdit_12.text()
        nz = self.ui.lineEdit_13.text()

        test = tc.PosOnTankChecker.type_check_line(
            {tank_type, num, tp, lo, x, y, z, ux, uy, uz, vx, vy, vz, nx, ny, nz})
        if not test:
            self.warning_window("ERROR\nSomething is null")
            return

        tup = (tp, lo, x, y, z, ux, uy, uz, vx, vy, vz, nx, ny, nz)
        tc_ret = tc.PosOnTankChecker.type_check(tup)
        if not tc_ret[0]:
            self.warning_window("Syntax ERROR!" + "\nERROR NUMBER: " + tc_ret[1])
            return

        co = (x, y, z)
        me = ((ux, uy, uz), (vx, vy, vz), (nx, ny, nz))
        self.get_controller().tank_add_pos_table(tank_tup=tank_tup, elem_type=tp, element_pos=lo, coord=co, met=me)
        self.edited_tank_number(txt=self.ui.comboBox_19.currentText())

    def tank_cancel(self):
        self.button_clicked_cancel()
        self.setup_tab_tank()

    def clicked_table_tank(self, i, j):
        tp = self.ui.tableWidget_5.item(i, 0).text()
        nr = self.ui.tableWidget_5.item(i, 1).text()
        xmm = self.ui.tableWidget_5.item(i, 2).text()
        ymm = self.ui.tableWidget_5.item(i, 3).text()
        zmm = self.ui.tableWidget_5.item(i, 4).text()
        ux = self.ui.tableWidget_5.item(i, 5).text()
        uy = self.ui.tableWidget_5.item(i, 6).text()
        uz = self.ui.tableWidget_5.item(i, 7).text()
        vx = self.ui.tableWidget_5.item(i, 8).text()
        vy = self.ui.tableWidget_5.item(i, 9).text()
        vz = self.ui.tableWidget_5.item(i, 10).text()
        nx = self.ui.tableWidget_5.item(i, 11).text()
        ny = self.ui.tableWidget_5.item(i, 12).text()
        nz = self.ui.tableWidget_5.item(i, 13).text()
        self.ui.comboBox_20.setCurrentText(tp)
        self.ui.comboBox_22.setCurrentText(nr)
        self.ui.lineEdit_2.setText(xmm)
        self.ui.lineEdit_3.setText(ymm)
        self.ui.lineEdit_4.setText(zmm)
        self.ui.lineEdit_5.setText(ux)
        self.ui.lineEdit_6.setText(vx)
        self.ui.lineEdit_7.setText(nx)
        self.ui.lineEdit_8.setText(uy)
        self.ui.lineEdit_9.setText(uz)
        self.ui.lineEdit_10.setText(vy)
        self.ui.lineEdit_11.setText(vz)
        self.ui.lineEdit_12.setText(ny)
        self.ui.lineEdit_13.setText(nz)

    def double_clicked_table_tank(self, i, j):
        tank_type = self.ui.comboBox_18.currentText()
        num = self.ui.comboBox_19.currentText()
        tank_tup = (tank_type, num)

        nr = self.ui.tableWidget_5.item(i, 1).text()
        self.get_controller().tank_del_pos_table(tank_tup=tank_tup, loc=nr)

        self.edited_tank_number(num)

    def db_transfer_tank(self):
        tank_tp = self.ui.comboBox_18.currentText()
        tank_num = self.ui.comboBox_19.currentText()
        tank_tup = (tank_tp, tank_num)

        flag = self.get_controller().vali_test(tk_tup=tank_tup)
        if flag:
            txt = "Push yes to validate tank : " + str(tank_tup)
            title = "Warning"
            self.vali_box_config(txt=txt, title=title)
            res = self.vali_box.exec_()
            if res == 1024:
                self.get_controller().vali_tank(tank_tup)

        self.button_clicked_db_transfer()
        self.setup_tab_tank()

    def clicked_extraire_tank_pos(self):
        tk_tup = self.ui.comboBox_18.currentText(), self.ui.comboBox_19.currentText()
        info, state = self.get_controller().action_extraire_tank_pos(tk_tup=tk_tup)
        self.warning_window(info)

    def edited_sc_type(self, txt):
        if txt == '':
            return
        tk_tup = self.ui.comboBox_18.currentText(), self.ui.comboBox_19.currentText()
        sc_type = self.ui.comboBox_20.currentText()
        ls = self.get_controller().action_get_tank_location_list(tk_tup, sc_type)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_22, items_init=ls)


class CopyTkConfig(QWidget):
    def __init__(self, father_window):
        super(CopyTkConfig, self).__init__()
        self.lb = None
        self.el = None
        self.lo = None
        self.pushB_ok = None
        self.setWindowTitle("Clone new configuration")
        self.f_window = father_window
        self.txt = ""
        self.init_window()

    def init_window(self):
        self.lo = QGridLayout()
        self.pushB_ok = QPushButton("Ok")
        self.lb = QLabel()
        self.el = QLineEdit(self.txt)
        self.lo.addWidget(self.lb, 0, 0)
        self.lo.addWidget(self.el, 0, 1)
        self.lo.addWidget(self.pushB_ok, 0, 2)
        self.setLayout(self.lo)

        self.pushB_ok.clicked.connect(self.clone)

    def change_label_txt(self, txt):
        self.txt = txt
        self.lb.setText(self.txt)

    def clone(self):
        self.close()
        self.f_window.clone_to_new_config(self.el.text())


class ListOfConfigurationView(View):
    def __init__(self, controller_obj=None):
        super(ListOfConfigurationView, self).__init__(controller_obj)
        self.tank_title = [item.value for item in ccc.FieldTkConfig]
        self.order_lis = [item.value for item in ccc.State]
        self.pos_lis = [item.value for item in ccc.Loc]
        self.copy_window = CopyTkConfig(self)

    def refresh(self):
        pass

    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.List_of_configuration.Ui_MainWindow()

    def handle_tab_bar_clicked(self, index):
        if index == 0:
            self.setup_tab_tank()
        elif index == 1:
            self.setup_tab_camera()
        elif index == 2:
            self.setup_tab_ejector()
        elif index == 3:
            self.setup_tab_acquisition()

    def setup_tab_tank(self):
        tank_type = self.get_controller().action_get_tank_type()
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox, items_init=tank_type)
        self.ui.comboBox.setEditable(False)
        self.ui.comboBox_2.setEditable(False)
        self.ui.comboBox_3.setEditable(True)
        self.ui.label_37.setText('None')

        self.ui.label_29.setText("----/--/--")
        self.refresh_tk_config_table()

    def refresh_tk_config_table(self):
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget, title=self.tank_title)

        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_4)
        self.ui.comboBox_4.setEditable(False)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_5)
        self.ui.comboBox_5.setEditable(False)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_6)
        self.ui.comboBox_6.setEditable(False)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_26)
        self.ui.comboBox_26.setEditable(False)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_27)
        self.ui.comboBox_27.setEditable(False)

    def setup_tab_camera(self):
        pass

    def setup_tab_ejector(self):
        pass

    def setup_tab_acquisition(self):
        pass

    def setup_ui(self):
        self.ui.tabWidget.tabBarClicked.connect(self.handle_tab_bar_clicked)

        # tank GUI
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox, func=self.edited_tank_type)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_2, func=self.edited_tank_serial_number)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_3, func=self.edited_tank_configuration)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_4, func=self.edited_loc)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_5, func=self.edited_ref_sensor_coating)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_6, func=self.edited_sensor_coating_num)

        self.tools_setup_table(table_widget_obj=self.ui.tableWidget,
                               clicked_fun=self.clicked_tank_config_table,
                               double_clicked_fun=self.double_clicked_config_table)

        self.ui.pushButton.clicked.connect(self.cancel_clicked)
        self.ui.pushButton_2.clicked.connect(self.db_transfer_clicked)
        self.ui.pushButton_3.clicked.connect(self.clicked_button_add)
        self.ui.pushButton_13.clicked.connect(self.clicked_create_config)

        self.setup_tab_tank()

    def edited_tank_type(self, txt):
        ret = self.get_controller().action_get_tank_num(txt)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_2, items_init=ret)
        self.ui.comboBox_2.setEditable(False)
        self.ui.label_29.setText("----/--/--")

        self.refresh_tk_config_table()

    def edited_tank_serial_number(self, txt):
        ret = self.get_controller().action_get_tank_config((self.ui.comboBox.currentText(), txt))
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_3, items_init=ret)
        self.ui.comboBox_3.setEditable(True)
        self.ui.label_29.setText("----/--/--")

        self.refresh_tk_config_table()

    def edited_tank_configuration(self, txt):
        if txt == '':
            self.ui.label_29.setText("----/--/--")
            return

        tk_tup = self.tools_get_tank_tup()
        date = self.get_controller().action_fill_config_date(tk_tup, txt)
        self.ui.label_29.setText(date)

        # 配置下拉框
        location_nr = self.get_controller().action_get_location_nr(self.tools_get_tank_tup())
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_4, items_init=location_nr)
        self.ui.comboBox_4.setEditable(False)

        sensor_coating_lis = self.get_controller().action_get_all_sensor_coating()
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_5, items_init=sensor_coating_lis)
        self.ui.comboBox_5.setEditable(False)

        serial_number_lis = self.get_controller().action_get_serial_number()
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_6, items_init=serial_number_lis)
        self.ui.comboBox_6.setEditable(False)

        order = self.order_lis
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_26, items_init=order)
        self.ui.comboBox_26.setEditable(False)

        pos = self.pos_lis
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_27, items_init=pos)
        self.ui.comboBox_27.setEditable(False)

        # 配置表格
        mat = self.get_controller().action_tank_config_table(tk_config_tup=(self.ui.comboBox.currentText(),
                                                                            self.ui.comboBox_2.currentText(),
                                                                            self.ui.comboBox_3.currentText()))
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget, title=self.tank_title, mat=mat)

        self.ui.label_37.setText('None')

    def clicked_create_config(self):
        tk_tup = self.ui.comboBox.currentText(), self.ui.comboBox_2.currentText()
        if tk_tup[0] == '':
            self.warning_window("ERROR!\nTank type is null")
            return
        if tk_tup[1] == '':
            self.warning_window("ERROR\nTank num is null")
            return
        tk_config = self.ui.comboBox_3.currentText()
        if tk_config == '':
            self.warning_window("ERROR\nTank config is null")
            return
        info, state = self.get_controller().action_create_new_config((tk_tup[0], tk_tup[1], tk_config))
        self.warning_window(info)
        self.edited_tank_serial_number(tk_tup[1])

    def edited_ref_sensor_coating(self, txt):
        serial_num_lis = self.get_controller().action_get_serial_number_by_ref(txt)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_6, items_init=serial_num_lis)
        self.ui.comboBox_6.setEditable(False)

    def edited_loc(self, txt):
        if txt == '':
            return

        tk_tup = self.tools_get_tank_tup()
        tk_config_tup = (tk_tup[0], tk_tup[1], self.ui.comboBox_3.currentText())

        ret, pot_type = self.get_controller().action_get_ele_ref_by_loc(txt, tk_config_tup=tk_config_tup)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_5, items_init=ret)
        self.ui.comboBox_5.setEditable(False)

        self.ui.label_37.setText(pot_type)

    def edited_sensor_coating_num(self, txt):
        pass

    def tools_get_tank_tup(self) -> tuple:
        return self.ui.comboBox.currentText(), self.ui.comboBox_2.currentText()

    def clicked_tank_config_table(self, i, j):
        loc_num = self.ui.tableWidget.item(i, 0).text()
        ref = self.ui.tableWidget.item(i, 1).text()
        serial_number = self.ui.tableWidget.item(i, 2).text()
        order = self.ui.tableWidget.item(i, 3).text()
        pos = self.ui.tableWidget.item(i, 4).text()

        self.ui.comboBox_4.setCurrentText(loc_num)
        self.ui.comboBox_5.setCurrentText(ref)
        self.ui.comboBox_6.setCurrentText(serial_number)
        self.ui.comboBox_26.setCurrentText(order)
        self.ui.comboBox_27.setCurrentText(pos)

    def double_clicked_config_table(self, i, j):
        # 检查tank_config是否validated
        tk_tup = self.tools_get_tank_tup()
        tk_config_tup = (tk_tup[0], tk_tup[1], self.ui.comboBox_3.currentText())
        state = self.get_controller().action_is_tank_config_validated(tank_config_tup=tk_config_tup)
        if state is True:
            # 询问是否创建一个新的config
            self.warning_window("Tank configuration\n(" + str(tk_config_tup) + ")\n is validated\nYou cannot modify!")
            self.copy_window.change_label_txt("Copy: " + tk_config_tup[2] + " ---> ")
            self.copy_window.show()
            return

        # 其次检查该"public.sensor_coating_config"记录是否被data_sensor引用
        else:
            loc_num = self.ui.tableWidget.item(i, 0).text()
            state = self.get_controller().action_check_is_refer(tk_config_str=tk_config_tup[2], loc=loc_num)
            sensor_coating_tup = (tk_config_tup[2], loc_num)
            if state:
                # 被引用了，询问是否创建一个新的config
                self.warning_window("Sensor_coating_config: " + str(sensor_coating_tup)
                                    + " is reffered by table <<sensor data>>\nSo you cannot "
                                      "delete this row in table sensor_coating_config")
                return
            else:
                # 未被引用，直接删除
                self.get_controller().action_delete_tk_config_row(tk_config_tup=tk_config_tup, loc_str=loc_num)
                # 刷新页面
                self.edited_tank_configuration(self.ui.comboBox_3.currentText())

    def db_transfer_clicked(self):
        # validate test
        # 先判断是否validated
        tk_tup = self.tools_get_tank_tup()
        tk_config_tup = (tk_tup[0], tk_tup[1], self.ui.comboBox_3.currentText())
        for item in tk_config_tup:
            if item == '':
                return

        state = self.get_controller().action_is_tank_config_validated(tank_config_tup=tk_config_tup)
        if not state:
            txt = "Push yes to validate this configuration:\n" + str(tk_config_tup)
            title = "Warning"
            self.vali_box_config(txt=txt, title=title)
            res = self.vali_box.exec_()
            if res == 1024:
                self.get_controller().action_validate_tk_config(tk_config_tup)

            self.button_clicked_db_transfer()

        self.setup_tab_tank()

    def cancel_clicked(self):
        self.button_clicked_cancel()
        self.setup_tab_tank()

    def clone_to_new_config(self, txt):
        # 输入的tank_config不能为空
        if txt == '':
            self.warning_window("ERROR!\nConfig name cannot be null!")
            return

        # 查询是否已经存在这个config
        state = self.get_controller().action_is_exist_tk_config(txt)
        if state:
            self.warning_window("ERROR!\nConfig name is existed!")
            return

        # clone
        new_id, row_number = self.get_controller().action_clone_tk_config(fro=self.ui.comboBox_3.currentText(),
                                                                          to=txt)
        self.warning_window("INSERT SUCCESS\nROW: " + str(row_number))

        # refresh
        tk_type = self.ui.comboBox.currentText()
        tk_num = self.ui.comboBox_2.currentText()
        self.setup_tab_tank()
        self.ui.comboBox.setCurrentText(tk_type)
        self.ui.comboBox_2.setCurrentText(tk_num)

    def clicked_button_add(self):
        tank_type = self.ui.comboBox.currentText()
        tk_num = self.ui.comboBox_2.currentText()
        tk_config = self.ui.comboBox_3.currentText()

        tk_config_tup = tank_type, tk_num, tk_config
        for item in tk_config_tup:
            if item == '':
                self.warning_window("ERROR\nTank message is NULL")
                return

        tk_loc_num = self.ui.comboBox_4.currentText()
        ref_sensor_coating = self.ui.comboBox_5.currentText()
        serial_num = self.ui.comboBox_6.currentText()
        order_ = self.ui.comboBox_26.currentText()
        pos = self.ui.comboBox_27.currentText()

        ref_info = tk_loc_num, ref_sensor_coating, serial_num, order_, pos
        for item in ref_info:
            if item == '':
                self.warning_window("ERROR\nRef info message is NULL")
                return

        state = self.get_controller().action_is_tank_config_validated(tank_config_tup=tk_config_tup)
        if state is True:
            # 询问是否创建一个新的config
            self.warning_window("Tank configuration\n(" + str(tk_config_tup) + ")\n is validated\nYou cannot modify!")
            self.copy_window.change_label_txt("Copy: " + tk_config_tup[2] + " ---> ")
            self.copy_window.show()
            return
        else:
            state, info = self.get_controller().action_push_add_ref(tk_config_tup, ref_info)
            if state != 0:
                self.warning_window(info)
            self.edited_tank_configuration(self.ui.comboBox_3.currentText())


class TestExecutionView(View):
    def __init__(self, controller_obj=None):
        super(TestExecutionView, self).__init__(controller_obj)

        self.error_message = ""

        self.ac_combo = None
        self.ac_line = None

        self.flight_data_data_resume = [item.value for item in ccc.FlightDataState]
        self.sensor_data_resume = [item.value for item in ccc.SensorDataState]

    def setup_ui(self):
        self.add_ele()
        self.ui.tabWidget.tabBarClicked.connect(self.handle_tab_bar_clicked)

        # means
        self.ui.comboBox.currentTextChanged.connect(self.edited_means_type)
        self.ui.comboBox_2.currentTextChanged.connect(self.edited_means_name)
        self.ui.comboBox_3.currentTextChanged.connect(self.edited_means_number)

        # test number
        self.ui.comboBox_4.currentTextChanged.connect(self.edited_test_number)

        # create new test
        self.ui.pushButton_3.clicked.connect(self.create_new_test)

        # cancel db_transfer
        self.ui.pushButton.clicked.connect(self.clicked_cancel_ac)

        # air
        self.ui.comboBox_16.currentTextChanged.connect(self.edited_airfield)
        self.ui.comboBox_17.currentTextChanged.connect(self.edited_run)

        # data file
        self.ui.comboBox_18.currentTextChanged.connect(self.edited_test_file_type)
        self.ui.pushButton_7.clicked.connect(self.clicked_add_data)
        self.ui.pushButton_6.clicked.connect(self.extraire_file)

        # db transfer
        self.ui.pushButton_2.clicked.connect(self.clicked_db_transfer_ac)

        self.setup_tab_ac()

    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Test_execution.Ui_MainWindow()

    def refresh(self):
        pass

    def add_ele(self):
        self.ac_line = {self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_3, self.ui.lineEdit_4,
                        self.ui.lineEdit_5, self.ui.lineEdit_6, self.ui.lineEdit_7, self.ui.lineEdit_8,
                        self.ui.lineEdit_9, self.ui.lineEdit_10, self.ui.lineEdit_12, self.ui.lineEdit_13}

        self.ac_combo = {self.ui.comboBox_5, self.ui.comboBox_6, self.ui.comboBox_7, self.ui.comboBox_8,
                         self.ui.comboBox_12, self.ui.comboBox_13, self.ui.comboBox_14, self.ui.comboBox_15,
                         self.ui.comboBox_16, self.ui.comboBox_17, self.ui.comboBox_36}

    def create_new_test(self):
        mean_tup = self.get_mean_tup()
        test_tup = (mean_tup[0], mean_tup[1], mean_tup[2], self.ui.comboBox_4.currentText())
        # 如果输入数据不合法，直接返回
        for item in test_tup:
            if item == "":
                self.warning_window("ERROR\nTest format is invalid!")
                return

        info = self.get_controller().action_create_test(test_tup=test_tup)
        self.warning_window(info)

    def refresh_ac(self):
        for item in self.ac_line:
            item.clear()

        self.tools_setup_combobox(self.ui.comboBox_9)
        self.tools_setup_combobox(self.ui.comboBox_10)
        self.tools_setup_combobox(self.ui.comboBox_11)
        self.tools_setup_combobox(self.ui.comboBox_18)

        # test_type
        ret = self.get_controller().get_test_type()
        self.tools_setup_combobox(self.ui.comboBox_5, items_init=ret)

        # test driver
        ret = self.get_controller().get_test_driver()
        self.tools_setup_combobox(self.ui.comboBox_6, items_init=ret)
        self.ui.comboBox_6.setEditable(False)

        # pilot and copilot
        ret = self.get_controller().get_pilot()
        self.tools_setup_combobox(self.ui.comboBox_7, items_init=ret)

        ret = self.get_controller().get_copilot()
        self.tools_setup_combobox(self.ui.comboBox_8, items_init=ret)

        # tank
        ret = self.get_controller().get_tank_config()
        self.tools_setup_combobox(self.ui.comboBox_12, items_init=ret)
        self.ui.comboBox_12.setEditable(False)

        # came
        ret = self.get_controller().get_came_config()
        self.tools_setup_combobox(self.ui.comboBox_13, items_init=ret)
        self.ui.comboBox_13.setEditable(False)

        # acq
        ret = self.get_controller().get_acq_config()
        self.tools_setup_combobox(self.ui.comboBox_14, items_init=ret)
        self.ui.comboBox_14.setEditable(False)

        # insect combo
        ret = self.get_controller().get_insect_comb()
        self.tools_setup_combobox(self.ui.comboBox_15, items_init=ret)
        self.ui.comboBox_15.setEditable(False)

        # kind of data
        ret = [item.value for item in ccc.DataType]
        self.tools_setup_combobox(self.ui.comboBox_18, items_init=ret)
        self.ui.comboBox_18.setEditable(False)

        # air
        ret = self.get_controller().get_airfield_tree()
        self.tools_setup_combobox(self.ui.comboBox_16, items_init=ret)

        # runway
        self.tools_setup_combobox(self.ui.comboBox_17)

        # alt
        self.tools_setup_combobox(self.ui.comboBox_36)

        # state vali of test_number
        self.ui.label_49.setText('None')

        self.refresh_test_table_ac()

    def handle_tab_bar_clicked(self, index):
        if index == 0:
            self.setup_tab_ac()
        if index == 1:
            self.setup_tab_wt()

    def setup_tab_ac(self):
        # means setup
        ret = self.get_controller().action_fill_means()
        self.tools_setup_combobox(self.ui.comboBox, items_init=ret)
        self.ui.comboBox.setEditable(False)
        self.ui.comboBox_2.setEditable(False)
        self.ui.comboBox_3.setEditable(False)

        # test number
        self.tools_setup_combobox(self.ui.comboBox_4)

        self.refresh_ac()

    def setup_tab_wt(self):
        pass

    """slot"""

    def edited_means_type(self, txt):
        if txt == '':
            return
        ret = self.get_controller().action_fill_combobox_test_mean(txt)

        self.tools_setup_combobox(self.ui.comboBox_2, items_init=ret)
        self.ui.comboBox_2.setEditable(False)

        self.tools_setup_combobox(self.ui.comboBox_3)
        self.ui.comboBox_3.setEditable(False)

        self.tools_setup_combobox(self.ui.comboBox_4)
        self.ui.comboBox_3.setEditable(False)

        """需要刷新剩余的combobox"""
        self.refresh_ac()

    def edited_means_name(self, txt):
        if txt == '':
            return
        mean_type = self.ui.comboBox.currentText()
        ret = self.get_controller().action_fill_serial(mean_type=mean_type, mean_name=txt)

        self.tools_setup_combobox(self.ui.comboBox_3, items_init=ret)
        self.ui.comboBox_3.setEditable(False)

        self.tools_setup_combobox(self.ui.comboBox_4)

        """需要刷新剩余的combobox"""
        self.refresh_ac()

    def edited_means_number(self, txt):
        if txt == '':
            return
        mean_tup = self.get_mean_tup()
        ret = self.get_controller().action_get_test_number(mean_tup)
        self.tools_setup_combobox(self.ui.comboBox_4, items_init=ret)
        self.refresh_ac()

    def edited_test_number(self, txt):
        if txt == '':
            return
        mean_tup = self.get_mean_tup()
        test_tup = (mean_tup[0], mean_tup[1], mean_tup[2], txt)

        ret = self.get_controller().action_filled_test_number(test_tup=test_tup)
        if not ret:
            self.refresh_ac()
            return

        self.ui.comboBox_5.setCurrentText(ret[0][0])
        self.ui.comboBox_6.setCurrentText(ret[0][1])

        self.ui.comboBox_7.setCurrentText(ret[0][9])
        self.ui.comboBox_8.setCurrentText(ret[0][10])

        self.ui.lineEdit.setText(ret[0][2])
        self.ui.lineEdit_2.setText(ret[0][3])
        self.ui.lineEdit_3.setText(ret[0][4])

        # achivement
        if ret[0][14] != 'None':
            self.ui.lineEdit_4.setText(ret[0][14])
        else:
            self.ui.lineEdit_4.setText('')

        self.ui.comboBox_12.setCurrentText(ret[0][5])
        self.ui.comboBox_13.setCurrentText(ret[0][7])
        self.ui.comboBox_14.setCurrentText(ret[0][6])

        # air info
        self.ui.comboBox_16.setCurrentText(ret[0][11])
        self.ui.comboBox_17.setCurrentText(ret[0][12])

        if ret[0][13] != 'None':
            self.ui.comboBox_36.setCurrentText(ret[0][13])
        else:
            self.ui.comboBox_36.setCurrentText('')

        # format json
        lis = ret[0][8]
        self.ui.lineEdit_5.setText(lis[0])
        self.ui.lineEdit_7.setText(lis[1])
        self.ui.lineEdit_9.setText(lis[2])
        self.ui.lineEdit_12.setText(lis[3])
        self.ui.lineEdit_6.setText(lis[4])
        self.ui.lineEdit_8.setText(lis[5])
        self.ui.lineEdit_10.setText(lis[6])
        self.ui.lineEdit_13.setText(lis[7])

        self.ui.label_49.setText(ret[0][15])

        self.refresh_test_table_ac()

    def edited_airfield(self, txt):
        if txt == '':
            return
        ret = self.get_controller().action_fill_combobox_runway(txt)
        self.tools_setup_combobox(self.ui.comboBox_17, items_init=ret)

    def edited_run(self, txt):
        if txt == '' or self.ui.comboBox_16.currentText() == '':
            return
        af = self.ui.comboBox_16.currentText()
        ret = self.get_controller().action_fill_alt(airfield=af, runway=txt)
        self.tools_setup_combobox(self.ui.comboBox_36, items_init=ret)

    """Process Optimization"""

    def get_mean_tup(self) -> tuple:
        mean_type = self.ui.comboBox.currentText()
        mean_name = self.ui.comboBox_2.currentText()
        mean_num = self.ui.comboBox_3.currentText()
        mean_tup = (mean_type, mean_name, mean_num)
        return mean_tup

    def clicked_cancel_ac(self):
        self.button_clicked_cancel()
        self.setup_tab_ac()

    def get_test_identification(self):
        mean_tup = self.get_mean_tup()
        test_tup = (mean_tup[0], mean_tup[1], mean_tup[2], self.ui.comboBox_4.currentText())

        test_type = self.ui.comboBox_5.currentText()
        test_driver = self.ui.comboBox_6.currentText()

        pilot = self.ui.comboBox_7.currentText()
        copilot = self.ui.comboBox_8.currentText()

        date = self.ui.lineEdit.text()
        time_begin = self.ui.lineEdit_2.text()
        time_end = self.ui.lineEdit_3.text()
        ach = self.ui.lineEdit_4.text()

        ti_tuple = (mean_tup, test_tup, test_type, test_driver, pilot, copilot, date, time_begin, time_end, ach)
        return ti_tuple

    def get_configuration(self):
        tkc = self.ui.comboBox_12.currentText()
        cac = self.ui.comboBox_13.currentText()
        acc = self.ui.comboBox_14.currentText()

        config_tuple = (tkc, cac, acc)

        for item in config_tuple:
            if not item:
                self.error_message += "configuration of the test, "
                break

        return config_tuple

    def get_initial_conditions(self):
        # air info
        af = self.ui.comboBox_16.currentText()
        run = self.ui.comboBox_17.currentText()
        alt = self.ui.comboBox_36.currentText()

        # format json
        j_1 = self.ui.lineEdit_5.text()
        j_2 = self.ui.lineEdit_7.text()
        j_3 = self.ui.lineEdit_9.text()
        j_4 = self.ui.lineEdit_12.text()
        j_5 = self.ui.lineEdit_6.text()
        j_6 = self.ui.lineEdit_8.text()
        j_7 = self.ui.lineEdit_10.text()
        j_8 = self.ui.lineEdit_13.text()

        json_list = [j_1, j_2, j_3, j_4, j_5, j_6, j_7, j_8]

        condition_tuple = (af, run, alt, str(json_list))

        for item in condition_tuple[:-1]:
            if not str(item):
                self.error_message += "initial condition, "
                break

        for item in json_list:
            if not str(item):
                self.error_message += "json string, "
                break

        return condition_tuple

    def update_test_config(self):
        """
        更细粒度的业务拆解
        """
        self.error_message = "Plz check : "

        ti = self.get_test_identification()
        ret = self.get_controller().is_test_exist(test_tup=ti[1])

        if not ret:
            self.error_message += "Test not exist, plz check your test!"
            # 弹窗
            # self.message_box(title="Warning", msg=self.error_message)
            print(self.error_message)
            return

        # 判断是否validated？
        ret = self.get_controller().is_test_validated(test_tup=ti[1])
        if ret:
            self.error_message += "Test is already validated, you cannot modify this test."
            # 弹窗
            # self.message_box(title="Warning", msg=self.error_message)
            print(self.error_message)
            return

        test_config = self.get_configuration()
        test_ic = self.get_initial_conditions()

        if self.error_message != "Plz check : ":
            # 弹窗显示error_message
            print(self.error_message)
        self.get_controller().action_update_test(ti, test_config, test_ic)

        return ti

    def clicked_db_transfer_ac(self):
        """
        两种异常，
        其一：不存在这个test_tup，要db_transfer必须先创建这个test_tup
        其二：该test_tup已经被validated了
        """
        ti = self.update_test_config()

        # validate test
        txt = "Push yes to validate this test: " + str(ti[1])
        title = "Warning"
        self.vali_box_config(txt=txt, title=title)
        res = self.vali_box.exec_()
        if res == 1024:
            self.get_controller().validate_test(ti[1])

        self.button_clicked_db_transfer()

        self.setup_tab_ac()

    def clicked_add_data(self):
        # 询问是否将现有数据提交至数据库以开始新的事务
        # commit test
        txt = "Push <<Yes>> to commit your change and start a new transaction to import data; If not push <<No>>"
        title = "Warning"
        self.vali_box_config(txt=txt, title=title)
        res = self.vali_box.exec_()
        if res == 1024:
            self.update_test_config()
            self.button_clicked_db_transfer()
            self.warning_window("Changes committed, new transaction started...")
        else:
            self.warning_window("Changes not committed...")
            return

        file_type = self.ui.comboBox_18.currentText()
        if file_type == '':
            self.error_window("ERROR\nPlz choose file type!")
            return

        test_tup = (self.ui.comboBox.currentText(), self.ui.comboBox_2.currentText(),
                    self.ui.comboBox_3.currentText(), self.ui.comboBox_4.currentText())

        if not self.get_controller().is_test_exist(test_tup=test_tup):
            self.error_window("ERROR!\nTest not exist")
            return

        # test
        mean_tup = self.get_mean_tup()
        test_tup = (mean_tup[0], mean_tup[1], mean_tup[2], self.ui.comboBox_4.currentText())
        info = None
        if file_type == ccc.DataType.F_D.value:

            path = self.file_dialog(question='Select flight data file', path_default=r'.\file_input')
            if path == '':
                return
            info = self.get_controller().action_import_data_file(path=path, strategy=ccc.DataType.F_D,
                                                                 test_tup=test_tup, tank_config=None)

        elif file_type == ccc.DataType.S_D.value:
            # 至少需要tank的配置，否则无法确定传感器的位置参数
            tank_config = self.ui.comboBox_12.currentText()
            if tank_config == '':
                self.error_window("Tank configuration not chosen!")
                return

            path = self.file_dialog(question='Select sensor data file', path_default=r'.\file_input')
            if path == '':
                self.error_window("ERROR!\nFile not chosen!")
                return
            info = self.get_controller().action_import_data_file(path=path, strategy=ccc.DataType.S_D,
                                                                 test_tup=test_tup, tank_config=tank_config)
        self.warning_window(info)

        self.refresh_test_table_ac()

    def refresh_test_table_ac(self):
        self.edited_test_file_type('')

    def extraire_file(self):
        test_tup = (self.ui.comboBox.currentText(), self.ui.comboBox_2.currentText(),
                    self.ui.comboBox_3.currentText(), self.ui.comboBox_4.currentText())
        self.get_controller().action_extraire_file(test_tup=test_tup)

    def edited_test_file_type(self, txt):
        mean_tup = self.get_mean_tup()
        test_tup = (mean_tup[0], mean_tup[1], mean_tup[2],
                    self.ui.comboBox_4.currentText())

        if not self.get_controller().is_test_exist(test_tup=test_tup):
            self.tools_setup_table(table_widget_obj=self.ui.tableWidget_3,
                                   title=["Test not exists"])
            return

        if txt == '':
            self.tools_setup_table(table_widget_obj=self.ui.tableWidget_3,
                                   title=["Plz choose a type of file"])
            return

        if txt == ccc.DataType.CO.value:
            if self.ui.comboBox_12.currentText() != '':
                mat = self.get_controller().action_get_coating_type_by_tank_config(self.ui.comboBox_12.currentText())
                self.tools_setup_table(table_widget_obj=self.ui.tableWidget_3,
                                       title=[item.value for item in ccc.CoatingsState],
                                       mat=mat)

        elif txt == ccc.DataType.F_D.value:
            mat = self.get_controller().fill_test_state_table_ac(test_tup=test_tup)
            self.tools_setup_table(table_widget_obj=self.ui.tableWidget_3,
                                   title=self.flight_data_data_resume,
                                   mat=mat)

        elif txt == ccc.DataType.S_D.value:
            mat = self.get_controller().fill_test_state_table_sensor_data(test_tup=test_tup)
            self.tools_setup_table(table_widget_obj=self.ui.tableWidget_3,
                                   title=self.sensor_data_resume,
                                   mat=mat)


class ExploitationOfTestView(View):
    def __init__(self, controller_obj=None):
        super(ExploitationOfTestView, self).__init__(controller_obj=controller_obj)

        self.create_test_point_title = [item.value for item in ccc.TypeTestPointTable]
        self.list_of_test_point = [item.value for item in ccc.ListOfTestPoint]
        self.fill_param_table = [item.value for item in ccc.ParaTable]
        self.fill_CD_table = [item.value for item in ccc.CoatingDetergentTable]
        self.confidentiality_table = [item.value for item in ccc.ConfiOfTestPoint]

        self.message = QMessageBox()
        self.message.setText("Validate or not?")
        self.message.setWindowTitle("Warning!")
        self.message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Exploitation_of_tests.Ui_MainWindow()

    def refresh(self):
        pass

    def refresh_1_1(self):
        # Test identification group box
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_5)
        self.ui.comboBox_5.setEditable(False)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_6)
        self.ui.comboBox_6.setEditable(False)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_7)
        self.ui.comboBox_7.setEditable(False)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_9)
        self.ui.comboBox_9.setEditable(False)

        # P.E. info
        self.ui.lineEdit.setText('----/--/--')
        self.ui.lineEdit_2.setText('----/--/--')

        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_11)
        self.ui.comboBox_11.setEditable(False)

        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_14)
        self.ui.comboBox_14.setEditable(False)

        self.ui.label_50.setText('None')

        # Remark
        self.ui.lineEdit_3.setText('')

        # Value of parameter group box
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox)
        self.ui.comboBox.setEditable(False)
        self.ui.lineEdit_5.setText('')

        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_3)
        self.ui.comboBox_3.setEditable(False)

        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_2, title=self.fill_param_table)

        # Coatings and detergents group box
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_17)
        self.ui.comboBox_17.setEditable(False)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_19)
        self.ui.comboBox_19.setEditable(False)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_22)
        self.ui.comboBox_22.setEditable(False)
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_7, title=self.fill_CD_table)

    def handle_tab_bar_clicked(self, index):
        if index == 0:
            self.setup_tab_test_points()
            self.ui.tabWidget_2.setCurrentIndex(0)
        elif index == 1:
            self.setup_tab_int_values()
            self.ui.tabWidget_3.setCurrentIndex(0)

    def handle_tab_bar_clicked_2(self, index):
        if index == 0:
            self.setup_tab_2_test_points()
        elif index == 1:
            self.setup_tab_2_create_tp()

    def handle_tab_bar_clicked_3(self, index):
        if index == 0:
            self.setup_tab_int_values()
        elif index == 1:
            self.setup_tab_create_int()

    def setup_ui(self):
        # TabWidget setup
        self.ui.tabWidget.tabBarClicked.connect(self.handle_tab_bar_clicked)
        self.ui.tabWidget_2.tabBarClicked.connect(self.handle_tab_bar_clicked_2)
        self.ui.tabWidget_3.tabBarClicked.connect(self.handle_tab_bar_clicked_3)

        # GUI 1.1
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_2, func=self.edited_test_point_type_1_1)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_12, func=self.edited_test_point_num_1_1)

        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_5, func=self.edited_test_means_type)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_6, func=self.edited_test_means_name)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_7, func=self.edited_serial_number)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_9, func=self.edited_test_number)

        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_17, func=self.edited_coating_or_detergent)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_19, func=self.edited_type_of_element)

        self.tools_setup_combobox(combobox_obj=self.ui.comboBox, func=self.edited_param_com)

        self.ui.pushButton_16.clicked.connect(self.clicked_create_test_point)
        self.ui.pushButton_17.clicked.connect(self.clicked_update_pe_info)
        self.ui.pushButton_4.clicked.connect(self.clicked_add_file)
        self.ui.pushButton_3.clicked.connect(self.clicked_update_value)
        self.ui.pushButton_8.clicked.connect(self.clicked_update_coating_detergent)

        self.ui.pushButton.clicked.connect(self.clicked_db_trans_1_1)
        self.ui.pushButton_2.clicked.connect(self.clicked_roll_back_1_1)

        self.tools_setup_table(table_widget_obj=self.ui.tableWidget,
                               title=self.list_of_test_point,
                               clicked_fun=self.clicked_test_point_table)

        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_2,
                               title=self.fill_param_table,
                               clicked_fun=self.clicked_test_point_param_table)

        # GUI 1.2
        self.ui.comboBox_18.currentTextChanged.connect(self.edited_type_of_test_point_1_2)
        self.ui.pushButton_7.clicked.connect(self.clicked_create_type_test_point)

        # GUI 1.2 tcl
        self.ui.pushButton_6.clicked.connect(self.button_clicked_db_transfer)
        self.ui.pushButton_5.clicked.connect(self.button_clicked_cancel)

        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_3,
                               clicked_fun=self.clicked_table_type_tp,
                               double_clicked_fun=self.double_clicked_type_tp)

        self.setup_tab_2_test_points()

    """两个父级tab"""

    def setup_tab_test_points(self):
        pass

    def setup_tab_int_values(self):
        pass

    """tab1.1"""

    def setup_tab_2_test_points(self):
        # Test point group box
        lis = self.get_controller().action_get_test_point_type()
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_2, items_init=lis)
        self.ui.comboBox_2.setEditable(False)

        self.tools_setup_table(table_widget_obj=self.ui.tableWidget, title=self.list_of_test_point)

        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_12)
        self.ui.comboBox_12.setEditable(False)

        # Test identification group box
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_5)
        self.ui.comboBox_5.setEditable(False)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_6)
        self.ui.comboBox_6.setEditable(False)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_7)
        self.ui.comboBox_7.setEditable(False)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_9)
        self.ui.comboBox_9.setEditable(False)

        # P.E. info
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_12)
        self.ui.comboBox_12.setEditable(False)

        self.ui.lineEdit.setText('----/--/--')
        self.ui.lineEdit_2.setText('----/--/--')

        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_14)
        self.ui.comboBox_14.setEditable(False)

        self.ui.label_50.setText('None')

        # Remark
        self.ui.lineEdit_3.setText('')

        # Value of parameter group box
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox)
        self.ui.comboBox.setEditable(False)
        self.ui.lineEdit_5.setText('')

        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_3)
        self.ui.comboBox_3.setEditable(False)

        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_2, title=self.fill_param_table)

        # Coatings and detergents group box
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_17)
        self.ui.comboBox_17.setEditable(False)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_19)
        self.ui.comboBox_19.setEditable(False)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_22)
        self.ui.comboBox_22.setEditable(False)
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_7, title=self.fill_CD_table)

    def edited_test_point_type_1_1(self, txt):
        num_lis, mat = self.get_controller().action_filled_type_tp(txt)
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget, title=self.list_of_test_point, mat=mat)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_12, items_init=num_lis)

    def edited_test_point_num_1_1(self, txt):
        # 检查是否存在这个test point
        ret = self.get_controller().action_is_exist_tp((self.ui.comboBox_2.currentText(),
                                                        txt))
        if not ret:
            self.refresh_1_1()
        else:
            # combo_box填充
            ret = self.get_controller().action_test_means_type()
            self.tools_setup_combobox(combobox_obj=self.ui.comboBox_5, items_init=ret)
            self.ui.comboBox_5.setEditable(False)

            # state
            self.tools_setup_combobox(combobox_obj=self.ui.comboBox_11, items_init=['False', 'True'])
            self.ui.comboBox_11.setEditable(False)

            # confidentiality
            self.tools_setup_combobox(combobox_obj=self.ui.comboBox_14, items_init=self.confidentiality_table)
            self.ui.comboBox_14.setEditable(False)

            # 主键填值
            tup = self.get_controller().action_test_point_is_filled((self.ui.comboBox_2.currentText(),
                                                                     txt))
            # self.tools_setup_combobox(combobox_obj=self.ui.comboBox_5)
            self.ui.comboBox_5.setCurrentText(tup[0])
            # self.tools_setup_combobox(combobox_obj=self.ui.comboBox_6)
            self.ui.comboBox_6.setCurrentText(tup[1])
            # self.tools_setup_combobox(combobox_obj=self.ui.comboBox_7)
            self.ui.comboBox_7.setCurrentText(tup[2])
            # self.tools_setup_combobox(combobox_obj=self.ui.comboBox_9)
            self.ui.comboBox_9.setCurrentText(tup[3])
            self.ui.comboBox_11.setCurrentText(tup[4])

            # P.E. info
            self.ui.lineEdit.setText(tup[5])
            self.ui.lineEdit_2.setText(tup[6])
            self.ui.comboBox_14.setCurrentText(tup[7])
            self.ui.label_50.setText(tup[8])

            # Remark
            self.ui.lineEdit_3.setText(tup[9])

            # Value of parameter group box
            param_lis, mat = self.get_controller().action_test_point_param(tp_tup=(self.ui.comboBox_2.currentText(),
                                                                                   self.ui.comboBox_12.currentText()))
            self.tools_setup_combobox(combobox_obj=self.ui.comboBox, items_init=param_lis)
            self.ui.comboBox.setEditable(False)

            self.ui.lineEdit_5.setText('')
            self.tools_setup_combobox(combobox_obj=self.ui.comboBox_3)
            self.ui.comboBox_3.setEditable(False)

            self.tools_setup_table(table_widget_obj=self.ui.tableWidget_2, title=self.fill_param_table, mat=mat)

            # Coatings and detergents group box
            self.tools_setup_combobox(combobox_obj=self.ui.comboBox_17,
                                      items_init=[ccc.TabState.COATING.value, ccc.TabState.DETERGENT.value])
            self.ui.comboBox_17.setEditable(False)
            self.tools_setup_combobox(combobox_obj=self.ui.comboBox_19)
            self.ui.comboBox_19.setEditable(False)
            self.tools_setup_combobox(combobox_obj=self.ui.comboBox_22)
            self.ui.comboBox_22.setEditable(False)

            mat = self.get_controller().action_test_point_cd(tp_tup=(self.ui.comboBox_2.currentText(),
                                                                     self.ui.comboBox_12.currentText()))
            self.tools_setup_table(table_widget_obj=self.ui.tableWidget_7, title=self.fill_CD_table, mat=mat)

    def edited_test_means_type(self, txt):
        ret = self.get_controller().action_fill_combobox_test_mean_type(txt)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_6, items_init=ret)
        self.ui.comboBox_6.setEditable(False)

    def edited_test_means_name(self, txt):
        ret = self.get_controller().action_fill_serial(self.ui.comboBox_5.currentText(),
                                                       txt)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_7, items_init=ret)
        self.ui.comboBox_7.setEditable(False)

    def edited_serial_number(self, txt):
        ret = self.get_controller().action_get_test_number((self.ui.comboBox_5.currentText(),
                                                            self.ui.comboBox_6.currentText(),
                                                            txt))
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_9, items_init=ret)
        self.ui.comboBox_9.setEditable(False)

    def edited_test_number(self, txt):
        pass

    def edited_coating_or_detergent(self, txt):
        cd = self.ui.comboBox_17.currentText()
        if cd == '':
            return
        if txt == ccc.TabState.COATING.value:
            txt = ccc.TabState.COATING
        elif txt == ccc.TabState.DETERGENT.value:
            txt = ccc.TabState.DETERGENT
        else:
            return
        ret = self.get_controller().action_c_d_type(c_or_d=txt)

        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_19, items_init=ret)
        self.ui.comboBox_19.setEditable(False)

        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_22)
        self.ui.comboBox_22.setEditable(False)

    def edited_type_of_element(self, txt):
        pattern = self.ui.comboBox_17.currentText()
        if pattern == ccc.TabState.COATING.value:
            pattern = ccc.TabState.COATING
        elif pattern == ccc.TabState.DETERGENT.value:
            pattern = ccc.TabState.DETERGENT
        else:
            return

        e_type = txt
        if e_type == '':
            return

        ret = self.get_controller().action_c_d_num(e_type=e_type, c_or_d=pattern)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_22, items_init=ret)
        self.ui.comboBox_22.setEditable(False)

    def edited_param_com(self, txt):
        if txt == '':
            return
        self.ui.lineEdit_5.setText('')

        type_tp = self.ui.comboBox_2.currentText()
        num_tp = self.ui.comboBox_12.currentText()

        tp_tup = type_tp, num_tp
        if tp_tup[0] == '' or tp_tup[1] == '':
            return

        # 获取unity列表
        ret = self.get_controller().action_get_unity_by_param(txt, tp_tup)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_3, items_init=ret)
        self.ui.comboBox_3.setEditable(False)

    def clicked_create_test_point(self):
        type_tp = self.ui.comboBox_2.currentText()
        num_tp = self.ui.comboBox_12.currentText()
        tp_tup = type_tp, num_tp
        for item in tp_tup:
            if item == '':
                self.warning_window("ERROR\nP.E. INFO IS NULL")
                return

        info, state = self.get_controller().action_create_tp(tp_tup=tp_tup)
        self.warning_window(info)

        if state == 0:
            self.edited_test_point_type_1_1(self.ui.comboBox_2.currentText())

    def clicked_update_pe_info(self):
        tp_tup = self.ui.comboBox_2.currentText(), self.ui.comboBox_12.currentText()
        if tp_tup[0] == '' or tp_tup[1] == '':
            self.warning_window("ERROR\nP.E. is null")
            return

        ret = self.get_controller().action_is_exist_tp(tp_tup=tp_tup)
        if not ret:
            self.warning_window("ERROR\nP.E. not exist")
            return

        tp_info = (self.ui.comboBox_5.currentText(),
                   self.ui.comboBox_6.currentText(),
                   self.ui.comboBox_7.currentText(),
                   self.ui.comboBox_9.currentText(),
                   self.ui.comboBox_11.currentText(),
                   self.ui.lineEdit.text(),
                   self.ui.lineEdit_2.text(),
                   self.ui.comboBox_14.currentText(),
                   self.ui.lineEdit_3.text())
        info, state = self.get_controller().action_update_tp_info(tp_tup, tp_info)
        self.warning_window(info)

        self.edited_test_point_type_1_1(tp_tup[0])
        self.edited_test_point_num_1_1(tp_tup[1])

    def clicked_add_file(self):
        pass

    def clicked_update_value(self):
        param = self.ui.comboBox.currentText()
        unity = self.ui.comboBox_3.currentText()
        if param == '':
            self.warning_window("ERROR\nPARAM IS NULL")
            return

        tp_tup = self.ui.comboBox_2.currentText(), self.ui.comboBox_12.currentText()
        info, state = self.get_controller().action_update_value((param, self.ui.lineEdit_5.text(), unity), tp_tup)
        if state != 0:
            self.warning_window(info)
            return

        self.edited_test_point_num_1_1(self.ui.comboBox_12.currentText())

    def clicked_update_coating_detergent(self):
        tup = (self.ui.comboBox_17.currentText(),
               self.ui.comboBox_19.currentText(),
               self.ui.comboBox_22.currentText())
        for item in tup:
            if item == '':
                self.warning_window("ERROR\nELEMENT INFO NULL")
        info, state = self.get_controller().action_update_coating_detergent(tup=tup,
                                                                            tp_tup=(self.ui.comboBox_2.currentText(),
                                                                                    self.ui.comboBox_12.currentText()))
        self.warning_window(info)
        if state == 0:
            self.edited_test_point_num_1_1(self.ui.comboBox_12.currentText())

    def clicked_test_point_table(self, i, j):
        test_point_issue = self.ui.tableWidget.item(i, 6).text()
        self.ui.comboBox_12.setCurrentText(test_point_issue)
        self.edited_test_point_num_1_1(test_point_issue)

    def clicked_test_point_param_table(self, i, j):
        param = self.ui.tableWidget_2.item(i, 0).text()
        value = self.ui.tableWidget_2.item(i, 1).text()
        unity = self.ui.tableWidget_2.item(i, 2).text()
        self.ui.comboBox.setCurrentText(param)
        self.ui.comboBox_3.setCurrentText(unity)
        self.ui.lineEdit_5.setText(value)

    def clicked_db_trans_1_1(self):
        super().button_clicked_db_transfer()
        self.setup_tab_2_test_points()

    def clicked_roll_back_1_1(self):
        super().button_clicked_cancel()
        self.setup_tab_2_test_points()

    """tab1.2"""

    def setup_tab_2_create_tp(self):
        ret = self.get_controller().action_get_test_point_type()
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_18, items_init=ret)
        self.ui.comboBox_18.setEditable(False)

        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_3,
                               title=self.create_test_point_title,
                               mat=None)

        param, unity = self.get_controller().action_get_type_param()
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_15, items_init=param)
        self.tools_setup_combobox(combobox_obj=self.ui.comboBox_16, items_init=unity)

        self.ui.label_20.setText(ccc.TestPointState.NULL.value)
        self.ui.label_31.setText('None')

    """tab2.1"""

    def setup_tab_2_int_value(self):
        pass

    """tab2.2"""

    def setup_tab_create_int(self):
        pass

    def edited_type_of_test_point_1_2(self, txt):
        if txt == '':
            self.tools_setup_table(table_widget_obj=self.ui.tableWidget_3,
                                   title=self.create_test_point_title,
                                   mat=None)
        else:
            mat = self.get_controller().action_filled_type_test_point(txt)
            self.tools_setup_table(table_widget_obj=self.ui.tableWidget_3,
                                   title=self.create_test_point_title,
                                   mat=mat)

            # update state and user of this type of test point
            state, user = self.get_controller().action_get_type_state_and_user(txt)
            self.ui.label_20.setText(state)
            self.ui.label_31.setText(user)

    def clicked_create_type_test_point(self):
        type_tp = self.ui.comboBox_18.currentText()
        if type_tp == '':
            self.warning_window("ERROR\nType test point not filled")
            return

        param_tup = self.ui.comboBox_15.currentText(), self.ui.comboBox_16.currentText()
        if param_tup[0] == '':
            self.warning_window("ERROR\nParam type is null")
            return

        info, state = self.get_controller().action_create_new_param(type_tp, param_tup)
        self.warning_window(info)

        mat = self.get_controller().action_filled_type_test_point(txt=type_tp)
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_3,
                               title=self.create_test_point_title,
                               mat=mat)

    def clicked_table_type_tp(self, i, j):
        type_param = self.ui.tableWidget_3.item(i, 0).text()
        unity = self.ui.tableWidget_3.item(i, 1).text()
        self.ui.comboBox_15.setCurrentText(type_param)
        self.ui.comboBox_16.setCurrentText(unity)

    def double_clicked_type_tp(self, i, j):
        type_param = self.ui.tableWidget_3.item(i, 0).text()
        unity = self.ui.tableWidget_3.item(i, 1).text()
        self.get_controller().action_delete_param(self.ui.comboBox_18.currentText(), (type_param, unity))
        self.edited_type_of_test_point_1_2(self.ui.comboBox_18.currentText())

    def button_clicked_db_transfer(self):
        if self.ui.comboBox_18.currentText() == '':
            self.warning_window("ERROR\nType_test_point is NULL")
            return
        type_tp = self.ui.comboBox_18.currentText()
        is_validated = self.get_controller().action_is_type_test_point_validated(type_tp)
        if not is_validated:
            res = self.message.exec_()
            if res == 1024:
                self.get_controller().action_validate_type_tp(type_tp=type_tp)
                self.warning_window("SUCCESS\nELEMENT IS ALREADY VALIDATED AND YOUR TRANSACTION IS COMMITTED!")
            else:
                self.warning_window("TRANSACTION COMMITTED")
            super().button_clicked_db_transfer()
            self.setup_tab_2_create_tp()
        else:
            self.warning_window("ATTENTION!\n" + type_tp + " IS ALREADY VALIDATED")
            super().button_clicked_db_transfer()
            self.warning_window("TRANSACTION COMMITTED!")

    def button_clicked_cancel(self):
        super().button_clicked_cancel()
        self.warning_window("ROLL BACK")
        self.setup_tab_2_create_tp()


if __name__ == "__main__":
    pass
