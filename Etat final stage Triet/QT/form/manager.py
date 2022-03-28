import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QDialog, QLabel, QComboBox, QLineEdit, QSplitter, QTreeView, QMessageBox, QCheckBox, QAbstractItemView, QHBoxLayout, QVBoxLayout, QFrame, QGridLayout
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
sys.path.append('..\\QT\\class')
import user
from user import *
import psycopg2 
from copy import deepcopy
class Manager(QWidget) :
    def __init__(self, parent, uname, lst):
        super(QWidget, self).__init__(parent)
        self.connect()
        self.setupUI()
        self.lst = lst
        self.uname_user = uname
        if 'manager' not in [i[0] for i in self.lst] :
            self.cancel_btn_1.setVisible(False)
            self.transfer_btn_1.setVisible(False)
            self.user_vali_btn.setVisible(False) 
  
    def setupUI(self) :
        self.init_user()
        ###############################################
        # Cancel, Temporary save, DB transfer Buttons #
        ###############################################
        self.cancel_btn_1 = QPushButton('Cancel')
        self.transfer_btn_1 = QPushButton('DB transfer')
        self.cancel_btn_2 = QPushButton('Cancel')
        self.transfer_btn_2 = QPushButton('DB transfer')
        ##############################################
        #  List of current user, moyen_essai, right  #
        ##############################################
        ###################################################    
        #         Create a Tab Widget (Note Book)         #
        ###################################################
        self.tabs = QTabWidget(self)
        self.tab1 = QWidget()
        self.tab1.resize(900, 600)
        self.tab2 = QWidget()
        self.tab2.resize(900, 600)
        #############################################
        #                Organisation               #
        #############################################
        splitter = QSplitter(Qt.Vertical, self.tab1)
        label = QLabel('Organisation')
        label.setAlignment(Qt.AlignCenter)
        self.orga = QComboBox()

        sql = """SELECT DISTINCT orga FROM account;"""
        self.cur.execute(sql)
        self.conn.commit()
        rows = self.cur.fetchall()
        orga = []
        for row in rows :
            orga.append(row[0])    
        edit = QLineEdit()
        self.orga.setLineEdit(edit)
        self.orga.addItems(orga)
        self.orga.setCurrentText('')
        self.orga.installEventFilter(self)
        splitter.addWidget(label)
        splitter.addWidget(self.orga)
        splitter.setGeometry(10, 10, 120, 40)
        #############################################
        #                  User Name                #
        #############################################
        splitter = QSplitter(Qt.Vertical, self.tab1)
        label = QLabel('User name')
        label.setAlignment(Qt.AlignCenter)
        self.uname = QComboBox()
        edit = QLineEdit()
        self.uname.setLineEdit(edit)
        self.uname.setCurrentText('')
        self.uname.installEventFilter(self)
        splitter.addWidget(label)
        splitter.addWidget(self.uname)
        splitter.setGeometry(162, 10, 120, 40)
        #############################################
        #                 First Name                #
        #############################################
        splitter = QSplitter(Qt.Vertical, self.tab1)
        label = QLabel('First name')
        label.setAlignment(Qt.AlignCenter)
        self.fname = QComboBox()
        edit = QLineEdit()
        self.fname.setLineEdit(edit)
        self.fname.setCurrentText('')
        self.fname.installEventFilter(self)
        splitter.addWidget(label)
        splitter.addWidget(self.fname)
        splitter.setGeometry(314, 10, 120, 40)
        #############################################
        #                  Last Name                #
        #############################################
        splitter = QSplitter(Qt.Vertical, self.tab1)
        label = QLabel('Last name')
        label.setAlignment(Qt.AlignCenter)
        self.lname = QComboBox()
        edit = QLineEdit()
        self.lname.setLineEdit(edit)
        self.lname.setCurrentText('')
        self.lname.installEventFilter(self)
        splitter.addWidget(label)
        splitter.addWidget(self.lname)
        splitter.setGeometry(10, 60, 120, 40)
        #############################################
        #                     Tel                   #
        #############################################
        splitter = QSplitter(Qt.Vertical, self.tab1)
        label = QLabel('Tel')
        label.setAlignment(Qt.AlignCenter)
        self.tel = QLineEdit()
        splitter.addWidget(label)
        splitter.addWidget(self.tel)
        splitter.setGeometry(162, 60, 120, 40)
        #############################################
        #                    Email                  #
        #############################################
        splitter = QSplitter(Qt.Vertical, self.tab1)
        label = QLabel()
        label = QLabel('Email')
        label.setAlignment(Qt.AlignCenter)
        self.email = QLineEdit()
        splitter.addWidget(label)
        splitter.addWidget(self.email)
        splitter.setGeometry(314, 60, 120, 40)
        #############################################
        #                 Password                  #
        #############################################
        splitter = QSplitter(Qt.Vertical, self.tab1)
        label = QLabel('Password')
        label.setAlignment(Qt.AlignCenter)
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        splitter.addWidget(label)
        splitter.addWidget(self.password)
        splitter.setGeometry(466, 10, 120, 40)
        #############################################
        #            Button New Password            #
        #############################################
        self.newpass_btn = QPushButton(self.tab1)
        self.newpass_btn.setGeometry(618, 30, 120, 20)
        self.newpass_btn.setText('New Password')
        self.newpass_btn.hide()
        #############################################
        #              Button Validate              #
        #############################################
        self.user_vali_btn = QPushButton(self.tab1)
        self.user_vali_btn.setGeometry(466, 80, 120, 20)
        self.user_vali_btn.setText('Validate')
        ##########################################
        #               User List                #
        ##########################################
        splitter = QSplitter(Qt.Vertical, self.tab1)
        label = QLabel('List of users')
        self.model_user = self.createUserModel(self)

        sql = """SELECT orga, uname, fname, lname, tel, email FROM account;"""
        self.cur.execute(sql)
        self.conn.commit()
        rows = self.cur.fetchall()    
        for row in rows :
            self.addUser(*(row[0:]))

        self.list_user_tree = QTreeView(self.tab1)
        self.list_user_tree.setModel(self.model_user)
        self.list_user_tree.setSortingEnabled(True)
        self.list_user_tree.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        self.list_user_tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(6) :
            self.list_user_tree.setColumnWidth(i, 880 / 6)
        splitter.addWidget(label)
        splitter.addWidget(self.list_user_tree)
        splitter.setGeometry(10, 110, 880, 250)
        ###########################################
        #              Button Remove              #
        ###########################################
        self.user_del_btn = QPushButton(self.tab1)
        self.user_del_btn.setGeometry(770, 80, 120, 20)
        self.user_del_btn.setText('Remove')
        self.user_del_btn.hide()
        ########################################
        #              Right List              #
        ########################################
        splitter = QSplitter(Qt.Vertical, self.tab1)
        label = QLabel('User right')
        self.model_right = self.createRightModel(self)
        self.list_right_tree = QTreeView(self.tab1)
        self.list_right_tree.setModel(self.model_right)
        self.list_right_tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        splitter.addWidget(label)
        splitter.addWidget(self.list_right_tree)
        splitter.setGeometry(10, 410, 300, 150)
        ########################################
        #              Admin list              #
        ########################################
        splitter = QSplitter(Qt.Vertical, self.tab1)
        label = QLabel('User right')
        self.model_admin = self.createAdminModel(self)
        sql = """SELECT ac.orga, ac.fname, ac.lname, (CASE 
                                    WHEN ur.id_test_mean IS NOT NULL THEN CONCAT(tm.name, '_', tm.number)
                                    WHEN ur.id_type_coating IS NOT NULL THEN tc.ref
                                    WHEN ur.id_type_detergent IS NOT NULL THEN td.ref
                                    WHEN ur.id_type_tank IS NOT NULL THEN tt.ref
                                    WHEN ur.id_type_sensor IS NOT NULL THEN ts.ref
                                    WHEN ur.id_type_ejector IS NOT NULL THEN te.ref
                                    WHEN ur.id_type_camera IS NOT NULL THEN tca.ref
                                    WHEN ur.id_type_test_point IS NOT NULL THEN ttp.ref
                                    WHEN id_type_intrinsic_value IS NOT NULL THEN tiv.ref END) AS object, ac.uname
                        FROM account ac
                        JOIN user_right ur ON ac.id = ur.id_account
                        LEFT JOIN test_mean tm ON tm.id = ur.id_test_mean
                        LEFT JOIN type_coating tc ON tc.id = ur.id_type_coating
                        LEFT JOIN type_detergent td ON td.id = ur.id_type_detergent
                        LEFT JOIN type_tank tt ON tt.id = ur.id_type_tank
                        LEFT JOIN type_sensor ts ON ts.id = ur.id_type_sensor
                        LEFT JOIN type_ejector te ON te.id = ur.id_type_ejector
                        LEFT JOIN type_camera tca ON tca.id = ur.id_type_camera
                        LEFT JOIN type_test_point ttp ON ttp.id = ur.id_type_test_point
                        LEFT JOIN type_intrinsic_value tiv ON tiv.id = ur.id_type_intrinsic_value
                        
                        WHERE LOWER(ur.role) = 'admin' 
                """
        self.cur.execute(sql)
        self.conn.commit()
        rows = self.cur.fetchall()
        for row in rows :
            self.addAdmin(*(row[0:]))
        self.list_admin_tree = QTreeView(self.tab1)
        self.list_admin_tree.setModel(self.model_admin)
        self.list_admin_tree.setColumnHidden(4, True)
        self.list_admin_tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        splitter.addWidget(label)
        splitter.addWidget(self.list_admin_tree)
        splitter.setGeometry(400, 410, 400, 150)
        ########################################################
        # Cancel, Temporary save, DB transfer Buttons for tab1 #
        ########################################################
        frame1 = QFrame(self.tab1)
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.cancel_btn_1)
        hlayout.addWidget(self.transfer_btn_1)
        frame1.setFrameStyle(0)
        frame1.setLayout(hlayout)
        frame1.setGeometry(240, 370, 400, 40)

        """ @addTab:
                add tab1 : User Management
        """
        self.tabs.addTab(self.tab1, 'User Management')
        ######################################################################################
        #                                 Create test mean                                   #
        ######################################################################################
        splitter = QSplitter(Qt.Vertical, self.tab2)
        label1 = QLabel('Test means identification')
        frame1 = QFrame()
        hlayout = QHBoxLayout()
        ##################################################################
        #                       test mean type                           #
        ##################################################################
        splitter1 = QSplitter(Qt.Vertical)
        label = QLabel('Test means type')
        self.test_mean_type = QComboBox()
        edit = QLineEdit()
        
        sql = """SELECT DISTINCT type FROM test_mean;"""
        self.cur.execute(sql)
        self.conn.commit()
        test_mean_type = []
        rows = self.cur.fetchall()
        for row in rows :
            test_mean_type.append(row[0])
        self.test_mean_type.setLineEdit(edit)

        self.test_mean_type.addItems(test_mean_type)
        self.test_mean_type.setCurrentText('')
        self.test_mean_type.installEventFilter(self)
        splitter1.addWidget(label)
        splitter1.addWidget(self.test_mean_type)
        hlayout.addWidget(splitter1)
        ##################################################################
        #                       test mean name                           #
        ##################################################################
        splitter2 = QSplitter(Qt.Vertical)
        label = QLabel('Test means name')
        self.test_mean_name = QComboBox()
        edit = QLineEdit()
        self.test_mean_name.setLineEdit(edit)
        self.test_mean_name.installEventFilter(self)
        splitter2.addWidget(label)
        splitter2.addWidget(self.test_mean_name)
        hlayout.addWidget(splitter2)
        ####################################################################
        #                       test mean number                           #
        ####################################################################
        splitter3 = QSplitter(Qt.Vertical)
        label = QLabel('Serial number')
        self.test_mean_num = QComboBox()
        edit = QLineEdit()
        self.test_mean_num.setLineEdit(edit)
        self.test_mean_num.installEventFilter(self)
        splitter3.addWidget(label)
        splitter3.addWidget(self.test_mean_num)
        hlayout.addWidget(splitter3)

        frame1.setLayout(hlayout)
        frame1.setFrameStyle(1)
        splitter.addWidget(label1)
        splitter.addWidget(frame1)
        splitter.setGeometry(10, 10, 400, 80)

        ######################################################################################
        #                          Create Coating, detergent and insect                      #
        ######################################################################################
        splitter = QSplitter(Qt.Vertical, self.tab2)
        label1 = QLabel('Create a Coating, a detergent, an insect')
        frame1 = QFrame()
        hlayout = QHBoxLayout()
        ##################################################################
        #                           Coating type                         #
        ##################################################################
        splitter1 = QSplitter(Qt.Vertical)
        label = QLabel('Coating name')
        self.coating_type = QComboBox()
        edit = QLineEdit()
        sql = """SELECT ref FROM type_coating;"""
        type_coating = []
        self.cur.execute(sql)
        self.conn.commit()
        rows = self.cur.fetchall()
        for row in rows :
            type_coating.append(row[0])
        self.coating_type.setLineEdit(edit)
        self.coating_type.addItems(type_coating)
        self.coating_type.setCurrentText('')
        self.coating_type.installEventFilter(self)
        splitter1.addWidget(label)
        splitter1.addWidget(self.coating_type)
        hlayout.addWidget(splitter1)
        ##################################################################
        #                          Detergent type                        #
        ##################################################################
        splitter2 = QSplitter(Qt.Vertical)
        label = QLabel('Detergent name')
        self.detergent_type = QComboBox()
        edit = QLineEdit()
        sql = """SELECT ref FROM type_detergent;"""
        type_detergent = []
        self.cur.execute(sql)
        self.conn.commit()
        rows = self.cur.fetchall()
        for row in rows :
            type_detergent.append(row[0])
        self.detergent_type.setLineEdit(edit)
        self.detergent_type.addItems(type_detergent)
        self.detergent_type.setLineEdit(edit)
        self.detergent_type.setCurrentText('')
        self.detergent_type.installEventFilter(self)
        splitter2.addWidget(label)
        splitter2.addWidget(self.detergent_type)
        hlayout.addWidget(splitter2)
        ####################################################################
        #                             Insect                               #
        ####################################################################
        splitter3 = QSplitter(Qt.Vertical)
        label = QLabel('Insect')
        self.insect = QComboBox()
        choose = ['Yes', 'No']
        self.insect.addItems(choose)
        splitter3.addWidget(label)
        splitter3.addWidget(self.insect)
        hlayout.addWidget(splitter3)

        frame1.setLayout(hlayout)
        frame1.setFrameStyle(1)
        splitter.addWidget(label1)
        splitter.addWidget(frame1)
        splitter.setGeometry(10, 100, 400, 80)

        ######################################################################################
        #                                 Create Instrumentation                             #
        ######################################################################################
        splitter = QSplitter(Qt.Vertical, self.tab2)
        label1 = QLabel('Create a Coating, a detergent, an insect')
        frame1 = QFrame()
        gridlayout = QGridLayout()
        ##################################################################
        #                            Tank type                           #
        ##################################################################
        splitter1 = QSplitter(Qt.Vertical)
        label = QLabel('Tank reference')
        self.tank_type = QComboBox()
        edit = QLineEdit()
        sql = """SELECT ref FROM type_tank;"""
        type_tank = []
        self.cur.execute(sql)
        self.conn.commit()
        rows = self.cur.fetchall()
        for row in rows :
            type_tank.append(row[0])
        self.tank_type.setLineEdit(edit)
        self.tank_type.addItems(type_tank)
        self.tank_type.setCurrentText('')
        self.tank_type.installEventFilter(self)
        splitter1.addWidget(label)
        splitter1.addWidget(self.tank_type)
        gridlayout.addWidget(splitter1, 0, 0)
        ##################################################################
        #                           Sensor type                          #
        ##################################################################
        splitter2 = QSplitter(Qt.Vertical)
        label = QLabel('Sensor type')
        self.sensor_type = QComboBox()
        edit = QLineEdit()
        sql = """SELECT ref FROM type_sensor;"""
        type_sensor = []
        self.cur.execute(sql)
        self.conn.commit()
        rows = self.cur.fetchall()
        for row in rows :
            type_sensor.append(row[0])
        self.sensor_type.addItems(type_sensor)
        self.sensor_type.setLineEdit(edit)
        self.sensor_type.setCurrentText('')
        self.sensor_type.installEventFilter(self)
        splitter2.addWidget(label)
        splitter2.addWidget(self.sensor_type)
        gridlayout.addWidget(splitter2, 0, 1)
        ####################################################################
        #                       Acquisition system                         #
        ####################################################################
        splitter3 = QSplitter(Qt.Vertical)
        label = QLabel('Acquisition system')
        self.acquisition = QComboBox()
        choose = ['Yes', 'No']
        self.acquisition.addItems(choose)
        splitter3.addWidget(label)
        splitter3.addWidget(self.acquisition)
        gridlayout.addWidget(splitter3, 0, 2)
        ####################################################################
        #                     Insect injector reference                    #
        ####################################################################
        splitter3 = QSplitter(Qt.Vertical)
        label = QLabel('Insect injector reference')
        self.ejector_type = QComboBox()
        edit = QLineEdit()
        sql = """SELECT ref FROM type_ejector;"""
        type_ejector = []
        self.cur.execute(sql)
        self.conn.commit()
        rows = self.cur.fetchall()
        for row in rows :
            type_ejector.append(row[0])
        self.ejector_type.addItems(type_ejector)
        self.ejector_type.setLineEdit(edit)
        self.ejector_type.setCurrentText('')
        self.ejector_type.installEventFilter(self)
        splitter3.addWidget(label)
        splitter3.addWidget(self.ejector_type)
        gridlayout.addWidget(splitter3, 1, 0)
        
        ####################################################################
        #                          Camera reference                        #
        ####################################################################
        splitter3 = QSplitter(Qt.Vertical)
        label = QLabel('Camera reference')
        self.camera_type = QComboBox()
        edit = QLineEdit()
        sql = """SELECT ref FROM type_camera;"""
        type_camera = []
        self.cur.execute(sql)
        self.conn.commit()
        rows = self.cur.fetchall()
        for row in rows :
            type_camera.append(row[0])
        self.camera_type.addItems(type_camera)
        self.camera_type.setLineEdit(edit)
        self.camera_type.setCurrentText('')
        self.camera_type.installEventFilter(self)
        splitter3.addWidget(label)
        splitter3.addWidget(self.camera_type)
        gridlayout.addWidget(splitter3, 1, 1)

        frame1.setLayout(gridlayout)
        frame1.setFrameStyle(1)
        splitter.addWidget(label1)
        splitter.addWidget(frame1)
        splitter.setGeometry(10, 190, 400, 120)

        ######################################################################################
        #                               Create exploitation data                             #
        ######################################################################################
        splitter = QSplitter(Qt.Vertical, self.tab2)
        label1 = QLabel('Create exploitation data')
        frame1 = QFrame()
        hlayout = QHBoxLayout()
        ##################################################################
        #                        Test point type                         #
        ##################################################################
        splitter1 = QSplitter(Qt.Vertical)
        label = QLabel('Name of test point type')
        self.test_point_type = QComboBox()
        edit = QLineEdit()
        sql = """SELECT ref FROM type_test_point;"""
        type_test_point = []
        self.cur.execute(sql)
        self.conn.commit()
        rows = self.cur.fetchall()
        for row in rows :
            type_test_point.append(row[0])
        self.test_point_type.addItems(type_test_point)
        self.test_point_type.setLineEdit(edit)
        self.test_point_type.setCurrentText('')
        self.test_point_type.installEventFilter(self)
        splitter1.addWidget(label)
        splitter1.addWidget(self.test_point_type)
        hlayout.addWidget(splitter1)
        ##################################################################
        #                      Intrinsic value type                      #
        ##################################################################
        splitter2 = QSplitter(Qt.Vertical)
        label = QLabel('Name of intrinsic value type')
        self.intrinsic_value_type = QComboBox()
        edit = QLineEdit()
        sql = """SELECT ref FROM type_intrinsic_value;"""
        type_intrinsic_value = []
        self.cur.execute(sql)
        self.conn.commit()
        rows = self.cur.fetchall()
        for row in rows :
            type_intrinsic_value.append(row[0])
        self.intrinsic_value_type.addItems(type_intrinsic_value)
        self.intrinsic_value_type.setLineEdit(edit)
        self.intrinsic_value_type.setCurrentText('')
        self.intrinsic_value_type.installEventFilter(self)
        splitter2.addWidget(label)
        splitter2.addWidget(self.intrinsic_value_type)
        hlayout.addWidget(splitter2)

        frame1.setLayout(hlayout)
        frame1.setFrameStyle(1)
        splitter.addWidget(label1)
        splitter.addWidget(frame1)
        splitter.setGeometry(10, 320, 400, 80)
        
        #########################################################################
        #           widgets "User rights" of tabs 'User's allocations'          #
        #########################################################################
        splitter = QSplitter(Qt.Vertical, self.tab2)
        label1 = QLabel('User rights')
        frame1 = QFrame()
        #########################################################################
        #           authorized users list of tabs 'User's allocations'          #
        #########################################################################
        splitter1 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('Authorized users')
        self.list_author_tree = QTreeView()
        self.model_author = self.createAuthorModel(self)
        self.list_author_tree.setModel(self.model_author)
        self.list_author_tree.setColumnHidden(5, True)
        self.list_author_tree.setEditTriggers(QAbstractItemView.NoEditTriggers)

        splitter1.addWidget(label)
        splitter1.addWidget(self.list_author_tree)
        splitter1.setGeometry(10, 10, 180, 460)
        ###############################################################
        #           rights list of tabs 'User's allocations'          #
        ###############################################################
        splitter2 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('Rights')
        label.setAlignment(Qt.AlignCenter)
        self.right = QComboBox()
        edit = QLineEdit()
        rights = ['admin', 'validate', 'create', 'guest']
        self.right.setLineEdit(edit)
        self.right.addItems(rights)
        self.right.setCurrentText('')
        splitter2.addWidget(label)
        splitter2.addWidget(self.right)
        splitter2.setGeometry(190, 215, 90, 40)
        ####################################################################
        #           other users list of tabs 'User's allocations'          #
        ####################################################################
        splitter3 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('Other user')
        self.list_other_tree = QTreeView()
        self.model_other = self.createOtherModel(self)
        self.list_other_tree.setModel(self.model_other)
        self.list_other_tree.setColumnHidden(4, True)
        self.list_other_tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        splitter3.addWidget(label)
        splitter3.addWidget(self.list_other_tree)
        splitter3.setGeometry(280, 10, 180, 460)
        #########################################################################
        #         button validate right of tabs 'User's allocations'            #
        #########################################################################
        self.right_vali_btn = QPushButton('Validate', frame1)
        self.right_vali_btn.setGeometry(190, 260, 90, 20)

        frame1.setFrameStyle(1)
        splitter.addWidget(label1)
        splitter.addWidget(frame1)
        splitter.setGeometry(420, 10, 470, 500)
        ########################################################
        # Cancel, Temporary save, DB transfer Buttons for tab2 #
        ########################################################
        frame2 = QFrame(self.tab2)
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.cancel_btn_2)
        hlayout.addWidget(self.transfer_btn_2)
        frame2.setFrameStyle(1)
        frame2.setLayout(hlayout)
        frame2.setGeometry(10, 420, 400, 40)

        """ @addTab :
                add tab2 :  User's allocation
        """
        self.tabs.addTab(self.tab2, 'Users\' allocation')
        self.tabs.setGeometry(0, 0, 900, 600)
        #####################################################
        # function of each button of tabs 'User Management' #
        #####################################################
        self.user_vali_btn.clicked.connect(self.validate_user)
        self.list_user_tree.clicked.connect(self.view_user)
        self.user_del_btn.clicked.connect(self.delUser)
        self.newpass_btn.clicked.connect(self.reset_password)
        self.cancel_btn_1.clicked.connect(self.cancel)
        self.transfer_btn_1.clicked.connect(self.transfer)
        ###########################################################################
        #           function of each button of tabs 'User's allocations'          #
        ###########################################################################
        self.right_vali_btn.clicked.connect(self.validate_right)
        self.list_author_tree.doubleClicked.connect(self.return_other)        
        self.cancel_btn_2.clicked.connect(self.cancel)
        self.transfer_btn_2.clicked.connect(self.transfer)

    def validate_user(self) :
        orga = self.orga.currentText()
        uname = self.uname.currentText()
        fname = self.fname.currentText()
        lname = self.lname.currentText()
        tel = self.tel.text()
        email = self.email.text()
        password = self.password.text()

        if orga not in [self.orga.itemText(i) for i in range(self.orga.count())] :
            self.orga.addItem(orga)    
        if uname not in [self.uname.itemText(i) for i in range(self.uname.count())] :
            self.uname.addItem(uname)
        if fname not in [self.fname.itemText(i) for i in range(self.fname.count())] :
            self.fname.addItem(fname)
        if lname not in [self.lname.itemText(i) for i in range(self.lname.count())] :
            self.lname.addItem(lname)
        if (orga != '' and uname != '' and fname != '' and lname != '' and tel != '' and email != '' and password != '') :
            self.addUser(orga, uname, fname, lname, tel, email)
        else :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("You need to fill all the information above")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        self.orga.setCurrentText('')
        self.uname.setCurrentText('')
        self.fname.setCurrentText('')
        self.lname.setCurrentText('')
        self.tel.setText('')
        self.email.setText('')
        self.password.setText('')

        u = user(uname, fname, lname, orga, tel, email, password)
        self.list_user_create.addUser(u)
        

    def mousePressEvent(self, event):
        if self.list_user_tree.selectedIndexes() != [] :
            self.list_user_tree.clearSelection()
            self.orga.setCurrentText('')
            self.uname.setCurrentText('')
            self.fname.setCurrentText('')
            self.lname.setCurrentText('')
            self.tel.setText('')
            self.email.setText('')
            self.password.setText('')
            self.user_del_btn.hide()
            if 'manager' in [i[0] for i in self.lst] :
                self.user_vali_btn.show()
            self.newpass_btn.hide()
            self.model_right.removeRows(0, self.model_right.rowCount())



    def createUserModel(self, parent) :
        model = QStandardItemModel(0, 6, parent)
        model.setHeaderData(0, Qt.Horizontal, 'Organisation')
        model.setHeaderData(1, Qt.Horizontal, 'User name')
        model.setHeaderData(2, Qt.Horizontal, 'First name')
        model.setHeaderData(3, Qt.Horizontal, 'Last name')
        model.setHeaderData(4, Qt.Horizontal, 'Tel')
        model.setHeaderData(5, Qt.Horizontal, 'Email')
        return model
    
    def addUser(self, orga, uname, fname, lname, tel, email) :
        self.model_user.insertRow(self.model_user.rowCount())
        row = self.model_user.rowCount() - 1
        self.model_user.setData(self.model_user.index(row, 0), orga)
        self.model_user.setData(self.model_user.index(row, 1), uname)
        self.model_user.setData(self.model_user.index(row, 2), fname)
        self.model_user.setData(self.model_user.index(row, 3), lname)
        self.model_user.setData(self.model_user.index(row, 4), tel)
        self.model_user.setData(self.model_user.index(row, 5), email)

    def delUser(self) :
        select_row = self.list_user_tree.selectedIndexes()[0].row()

        ##################################################################
        value = self.model_user.data(self.model_user.index(select_row, 1))
        ##################################################################
        self.model_user.removeRow(select_row)

        self.orga.setCurrentText('')
        self.uname.setCurrentText('')
        self.fname.setCurrentText('')
        self.lname.setCurrentText('')
        self.tel.setText('')
        self.email.setText('')
        self.user_del_btn.hide()
        self.model_right.removeRows(0, self.model_right.rowCount())
        for i in range(self.model_admin.rowCount()) :
            find_uname = self.model_admin.data(self.model_admin.index(i, 4))
            if value == find_uname :
                self.model_admin.removeRow(i)
        for i in range(self.model_author.rowCount()) :
            find_uname = self.model_author.data(self.model_author.index(i, 5))
            if value == find_uname :
                self.model_author.removeRow(i)
        for i in range(self.model_other.rowCount()) :
            find_uname = self.model_other.data(self.model_other.index(i, 4))
            if value == find_uname :
                self.model_other.removeRow(i)
        if self.list_user_create.findUser(value) is not None :
            self.list_user_create.delUser(self.list_user_create.findUser(value))
        if self.list_user_current.findUser(value) is not None :
            self.list_user_delete.addUser(self.list_user_current.findUser(value))
        
        # sql = """DELETE FROM account WHERE uname = %s"""
        # self.cur.execute(sql, (value,))
        # self.conn.commit()
    def view_user(self) :
        if self.list_user_tree.selectedIndexes()[0] :
            select_row = self.list_user_tree.selectedIndexes()[0].row()
            orga = self.model_user.data(self.model_user.index(select_row, 0))
            uname = self.model_user.data(self.model_user.index(select_row, 1))
            fname = self.model_user.data(self.model_user.index(select_row, 2))
            lname = self.model_user.data(self.model_user.index(select_row, 3))
            tel = self.model_user.data(self.model_user.index(select_row, 4))
            email = self.model_user.data(self.model_user.index(select_row, 5))
            self.orga.setCurrentText(orga)
            self.uname.setCurrentText(uname)
            self.fname.setCurrentText(fname)
            self.lname.setCurrentText(lname)
            self.tel.setText(tel)
            self.email.setText(email)
            if 'manager' in [i[0] for i in self.lst] :
                self.user_del_btn.show()
                self.newpass_btn.show()
            self.user_vali_btn.hide()
            self.model_right.removeRows(0, self.model_right.rowCount())

            sql = """SELECT ur.role, (CASE 
                                        WHEN ur.id_test_mean IS NOT NULL THEN CONCAT(tm.name, '_', tm.number)
                                        WHEN ur.id_type_coating IS NOT NULL THEN tc.ref
                                        WHEN ur.id_type_detergent IS NOT NULL THEN td.ref
                                        WHEN ur.id_type_tank IS NOT NULL THEN tt.ref
                                        WHEN ur.id_type_sensor IS NOT NULL THEN ts.ref
                                        WHEN ur.id_type_ejector IS NOT NULL THEN te.ref
                                        WHEN ur.id_type_camera IS NOT NULL THEN tca.ref
                                        WHEN ur.id_type_test_point IS NOT NULL THEN ttp.ref
                                        WHEN id_type_intrinsic_value IS NOT NULL THEN tiv.ref END) AS object
                    FROM account ac
                    JOIN user_right ur ON ac.id = ur.id_account
                    LEFT JOIN test_mean tm ON tm.id = ur.id_test_mean
                    LEFT JOIN type_coating tc ON tc.id = ur.id_type_coating
                    LEFT JOIN type_detergent td ON td.id = ur.id_type_detergent
                    LEFT JOIN type_tank tt ON tt.id = ur.id_type_tank
                    LEFT JOIN type_sensor ts ON ts.id = ur.id_type_sensor
                    LEFT JOIN type_ejector te ON te.id = ur.id_type_ejector
                    LEFT JOIN type_camera tca ON tca.id = ur.id_type_camera
                    LEFT JOIN type_test_point ttp ON ttp.id = ur.id_type_test_point
                    LEFT JOIN type_intrinsic_value tiv ON tiv.id = ur.id_type_intrinsic_value
                    
                    WHERE ac.uname = %s
            """
            self.cur.execute(sql, (uname,))
            self.conn.commit()

            rows = self.cur.fetchall()
            for row in rows :
                self.addRight(*(row[0:]))



    def createRightModel(self, parent) :
        model = QStandardItemModel(0, 2, parent)
        model.setHeaderData(0, Qt.Horizontal, 'Right')
        model.setHeaderData(1, Qt.Horizontal, 'Attribut')
        return model

    def addRight(self, role, attribut) :
        self.model_right.insertRow(self.model_right.rowCount())
        row = self.model_right.rowCount() - 1
        self.model_right.setData(self.model_right.index(row, 0), role)
        self.model_right.setData(self.model_right.index(row, 1), attribut)


    def delRight(self) :
        self.model_right.removeRows(0, self.model_right.rowCount())

    def createAdminModel(self, parent) :
        model = QStandardItemModel(0, 5, parent)
        model.setHeaderData(0, Qt.Horizontal, 'Organisation')
        model.setHeaderData(1, Qt.Horizontal, 'First name')
        model.setHeaderData(2, Qt.Horizontal, 'Last name')
        model.setHeaderData(3, Qt.Horizontal, 'Admin')
        model.setHeaderData(4, Qt.Horizontal, 'User name')
        return model

    def addAdmin(self, orga, fname, lname, admin, uname) :
        self.model_admin.insertRow(self.model_admin.rowCount())
        row = self.model_admin.rowCount() - 1
        self.model_admin.setData(self.model_admin.index(row, 0), orga)
        self.model_admin.setData(self.model_admin.index(row, 1), fname)
        self.model_admin.setData(self.model_admin.index(row, 2), lname)
        self.model_admin.setData(self.model_admin.index(row, 3), admin)
        self.model_admin.setData(self.model_admin.index(row, 4), uname)   

    def createAttributModel(self, parent) :
        model = QStandardItemModel(0, 3, parent)
        model.setHeaderData(0, Qt.Horizontal, 'Attribute')
        model.setHeaderData(1, Qt.Horizontal, 'Value')
        model.setHeaderData(2, Qt.Horizontal, 'Unity')
        return model

    def addAttribut(self, att, val, unity) :
        self.model_attribut.insertRow(self.model_attribut.rowCount())
        row = self.model_attribut.rowCount() - 1
        self.model_attribut.setData(self.model_attribut.index(row, 0), att)
        self.model_attribut.setData(self.model_attribut.index(row, 1), val)
        self.model_attribut.setData(self.model_attribut.index(row, 2), unity)

    def createAuthorModel(self, parent) :
        model = QStandardItemModel(0, 6, parent)
        model.setHeaderData(0, Qt.Horizontal, 'First name')
        model.setHeaderData(1, Qt.Horizontal, 'Last name')
        model.setHeaderData(2, Qt.Horizontal, 'Organisation')
        model.setHeaderData(3, Qt.Horizontal, 'Tel')
        model.setHeaderData(4, Qt.Horizontal, 'Right')
        model.setHeaderData(5, Qt.Horizontal, 'User name')
        return model

    def addAuthor(self, fname, lname, orga, tel, right, uname) :
        self.model_author.insertRow(self.model_author.rowCount())
        row = self.model_author.rowCount() - 1
        self.model_author.setData(self.model_author.index(row, 0), fname)
        self.model_author.setData(self.model_author.index(row, 1), lname)
        self.model_author.setData(self.model_author.index(row, 2), orga)
        self.model_author.setData(self.model_author.index(row, 3), tel)
        self.model_author.setData(self.model_author.index(row, 4), right)
        self.model_author.setData(self.model_author.index(row, 5), uname)

    def delAuthor(self, row) :
        self.model_author.removeRow(row)

    def createOtherModel(self, parent) :
        model = QStandardItemModel(0, 5, parent)
        model.setHeaderData(0, Qt.Horizontal, 'First name')
        model.setHeaderData(1, Qt.Horizontal, 'Last name')
        model.setHeaderData(2, Qt.Horizontal, 'Organisation')
        model.setHeaderData(3, Qt.Horizontal, 'Tel')
        model.setHeaderData(4, Qt.Horizontal, 'Username')
        return model
    
    def addOther(self, fname, lname, orga, tel, uname) :
        self.model_other.insertRow(self.model_other.rowCount())
        row = self.model_other.rowCount() - 1
        self.model_other.setData(self.model_other.index(row, 0), fname)
        self.model_other.setData(self.model_other.index(row, 1), lname)
        self.model_other.setData(self.model_other.index(row, 2), orga)
        self.model_other.setData(self.model_other.index(row, 3), tel)
        self.model_other.setData(self.model_other.index(row, 4), uname)
    
    def delOther(self, row) :        
        self.model_other.removeRow(row)


    def createParamModel(self, parent) :
        model = QStandardItemModel(0, 2, parent)
        model.setHeaderData(0, Qt.Horizontal, 'Parameter')
        model.setHeaderData(1, Qt.Horizontal, 'Unity')
        return model
    
    def addParam(self, param, unity) :
        self.model_param.insertRow(self.model_param.rowCount())
        row = self.model_param.rowCount() - 1
        self.model_param.setData(self.model_param.index(row, 0), param)
        self.model_param.setData(self.model_param.index(row, 1), unity)

    def reset_password(self) :
        try :
            uname = self.uname.currentText()
            password = self.password.text()
            # sql = """UPDATE account
            #          SET password = CRYPT(%s, gen_salt('bf', 8))
            #          WHERE uname = %s;"""
            # self.cur.execute(sql, (password, uname))
            # self.conn.commit()
            if self.list_user_current.findUser(uname) is not None :
                self.list_user_update.addUser(self.list_user_current.findUser(uname))
                self.list_user_update.findUser(uname).changePassword(password)
            if self.list_user_create.findUser(uname) is not None :
                self.list_user_create.findUser(uname).changePassword(password)
        except :
            print('error')


    def validate_right(self) : 
        test_mean_type = self.test_mean_type.currentText()

        test_mean_name = self.test_mean_name.currentText()

        test_mean_num = self.test_mean_num.currentText()

        type_coating = self.coating_type.currentText()

        type_detergent = self.detergent_type.currentText()

        type_tank = self.tank_type.currentText()

        type_sensor = self.sensor_type.currentText()

        type_ejector = self.ejector_type.currentText()

        type_camera = self.camera_type.currentText()

        type_test_point = self.test_point_type.currentText()

        type_intrinsic_value = self.intrinsic_value_type.currentText()
        if 'admin' not in [i[0] for i in self.lst] and 'manager' not in [i[0] for i in self.lst]:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("You are not allowed to do this")
            msg.setWindowTitle("validate Fail")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        if  (~test_mean_type.isspace() and test_mean_type != '') and  (~test_mean_name.isspace() and test_mean_name != '')  and  (~test_mean_num.isspace() and test_mean_num != '') :
            if '_'.join([test_mean_type, test_mean_name, test_mean_num]) not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'test mean'] and 'manager' not in [i[0] for i in self.lst]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        if (~type_coating.isspace() and type_coating != '') :
            if type_coating not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'coating'] and 'manager' not in [i[0] for i in self.lst]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        if (~type_detergent.isspace() and type_detergent != '') :
            if type_detergent not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'detergent'] and 'manager' not in [i[0] for i in self.lst] :
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        if (~type_tank.isspace() and type_tank != '') :
            if type_tank not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'tank'] and 'manager' not in [i[0] for i in self.lst]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        if (~type_sensor.isspace() and type_sensor != '') :
            if type_sensor not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'sensor'] and 'manager' not in [i[0] for i in self.lst]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        if (~type_ejector.isspace() and type_ejector != '') :
            if type_ejector not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'ejector'] and 'manager' not in [i[0] for i in self.lst]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        if (~type_camera.isspace() and type_camera != '') :
            if type_camera not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'camera'] and 'manager' not in [i[0] for i in self.lst]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        if (~type_test_point.isspace() and type_test_point != '') :
            if type_test_point not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'test point'] and 'manager' not in [i[0] for i in self.lst]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        if (~type_intrinsic_value.isspace() and type_intrinsic_value != '') :
            if type_intrinsic_value not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'intrinsic value'] and 'manager' not in [i[0] for i in self.lst]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        if (self.list_other_tree.selectedIndexes() != []) :
            if self.right.currentText() == 'admin' :
                for row in range(self.model_author.rowCount()) :
                    if self.model_author.data(self.model_author.index(row, 4)) == 'admin' :
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setText("This object is already had an admin! \n Try again")
                        msg.setWindowTitle("Login Fail")
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.exec_()
                        return
            select_other = self.list_other_tree.selectedIndexes()[0].row()
            fname = self.model_other.data(self.model_other.index(select_other, 0))
            lname = self.model_other.data(self.model_other.index(select_other, 1))
            orga = self.model_other.data(self.model_other.index(select_other, 2))
            tel = self.model_other.data(self.model_other.index(select_other, 3))
            uname = self.model_other.data(self.model_other.index(select_other, 4))
            right = self.right.currentText()
            self.addAuthor(fname, lname, orga, tel, right, uname)
            self.delOther(select_other)
            test_mean_type = self.test_mean_type.currentText()
            if (test_mean_type not in [self.test_mean_type.itemText(i) for i in range(self.test_mean_type.count())]) :
                self.test_mean_type.addItem(test_mean_type)
            
    def eventFilter(self, obj, event) :
        if (self.tabs.currentIndex() == 0) :
            ######################################
            # Event on Combobox of organisation  #
            ######################################
            if obj == self.orga :
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    self.orga.showPopup()
                    self.orga.view().viewport().installEventFilter(self)
                    return True
                if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return) :
                    orga = self.orga.currentText()
                    if not orga.isspace() and orga != '' :
                        uname = []
                        sql = """SELECT uname FROM account WHERE orga = %s;"""
                        self.cur.execute(sql, (orga,))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            uname.append(row[0])
                        self.uname.clear()
                        self.uname.addItems(uname)
                        self.uname.setCurrentText('')
                        self.fname.setCurrentText('')
                        self.fname.clear()
                        self.lname.setCurrentText('')
                        self.lname.clear()
                        self.tel.setText('')
                        self.email.setText('')
                    self.uname.setFocus()
                    return True
                return False
            if obj == self.orga.view().viewport() :
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    index = self.orga.view().currentIndex().row()
                    orga = self.orga.itemText(index)
                    uname = []
                    sql = """SELECT uname FROM account WHERE orga = %s;"""
                    self.cur.execute(sql, (orga,))
                    self.conn.commit()

                    rows = self.cur.fetchall()
                    for row in rows :
                        uname.append(row[0])
                    self.uname.clear()
                    self.uname.addItems(uname)
                    self.uname.setCurrentText('')
                    self.fname.setCurrentText('')
                    self.lname.setCurrentText('')
                    self.tel.setText('')
                    self.email.setText('')
                    self.uname.setFocus()
                    uname = self.uname.currentText()
                    if (uname.isspace() or uname == ''):
                        sql = """SELECT DISTINCT fname FROM account WHERE orga = %s;"""
                        self.cur.execute(sql, (orga, ))
                        self.conn.commit()
                        fname = []
                        rows = self.cur.fetchall()
                        for row in rows :
                            fname.append(row[0])
                        self.fname.clear()
                        self.fname.addItems(fname)
                        self.fname.setCurrentText('')
                    return True
                return False
            ######################################
            #    Event on Combobox of username   #
            ######################################
            if obj == self.uname :
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    self.uname.showPopup()
                    self.uname.view().viewport().installEventFilter(self)
                    return True
                if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return) :
                    orga = self.orga.currentText()
                    uname = self.uname.currentText()
                    if not orga.isspace() and orga != '' and not uname.isspace() and uname != '':
                        sql_ac = """SELECT fname, lname, tel, email FROM account WHERE uname = %s;"""
                        sql_role = """SELECT ur.role, (CASE 
                                    WHEN ur.id_test_mean IS NOT NULL THEN CONCAT(tm.name, '_', tm.number)
                                    WHEN ur.id_type_coating IS NOT NULL THEN tc.ref
                                    WHEN ur.id_type_detergent IS NOT NULL THEN td.ref
                                    WHEN ur.id_type_tank IS NOT NULL THEN tt.ref
                                    WHEN ur.id_type_sensor IS NOT NULL THEN ts.ref
                                    WHEN ur.id_type_ejector IS NOT NULL THEN te.ref
                                    WHEN ur.id_type_camera IS NOT NULL THEN tca.ref
                                    WHEN ur.id_type_test_point IS NOT NULL THEN ttp.ref
                                    WHEN id_type_intrinsic_value IS NOT NULL THEN tiv.ref END) AS object
                                FROM account ac
                                JOIN user_right ur ON ac.id = ur.id_account
                                LEFT JOIN test_mean tm ON tm.id = ur.id_test_mean
                                LEFT JOIN type_coating tc ON tc.id = ur.id_type_coating
                                LEFT JOIN type_detergent td ON td.id = ur.id_type_detergent
                                LEFT JOIN type_tank tt ON tt.id = ur.id_type_tank
                                LEFT JOIN type_sensor ts ON ts.id = ur.id_type_sensor
                                LEFT JOIN type_ejector te ON te.id = ur.id_type_ejector
                                LEFT JOIN type_camera tca ON tca.id = ur.id_type_camera
                                LEFT JOIN type_test_point ttp ON ttp.id = ur.id_type_test_point
                                LEFT JOIN type_intrinsic_value tiv ON tiv.id = ur.id_type_intrinsic_value
                                
                                WHERE ac.uname = %s
                        """
                        self.cur.execute(sql_ac, (uname,))
                        self.conn.commit()
                        row = self.cur.fetchone()
                        if row is not None :
                            self.fname.setCurrentText(row[0])
                            self.lname.setCurrentText(row[1])
                            self.tel.setText(row[2])
                            self.email.setText(row[3])
                        else : 
                            self.fname.clear()
                            self.lname.clear()
                            self.fname.setCurrentText('')
                            self.lname.setCurrentText('')
                            self.tel.setText('')
                            self.email.setText('')
                        self.delRight()
                        self.cur.execute(sql_role, (uname,))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addRight(*(row[0:]))  
                    if not orga.isspace() and orga != '' and (uname.isspace() or uname == ''):
                        sql = """SELECT DISTINCT fname FROM account WHERE orga = %s;"""
                        self.cur.execute(sql, (orga, ))
                        self.conn.commit()
                        fname = []
                        rows = self.cur.fetchall()
                        for row in rows :
                            fname.append(row[0])
                        self.fname.clear()
                        self.fname.addItems(fname)
                    self.fname.setFocus()
                    return True
                return False

            if obj == self.uname.view().viewport() :
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    index = self.uname.view().currentIndex().row()
                    uname = self.uname.itemText(index)
                    if not uname.isspace() and uname != '' :
                        sql_ac = """SELECT fname, lname, tel, email FROM account WHERE uname = %s;"""
                        sql_role = """SELECT ur.role, (CASE 
                                    WHEN ur.id_test_mean IS NOT NULL THEN CONCAT(tm.name, '_', tm.number)
                                    WHEN ur.id_type_coating IS NOT NULL THEN tc.ref
                                    WHEN ur.id_type_detergent IS NOT NULL THEN td.ref
                                    WHEN ur.id_type_tank IS NOT NULL THEN tt.ref
                                    WHEN ur.id_type_sensor IS NOT NULL THEN ts.ref
                                    WHEN ur.id_type_ejector IS NOT NULL THEN te.ref
                                    WHEN ur.id_type_camera IS NOT NULL THEN tca.ref
                                    WHEN ur.id_type_test_point IS NOT NULL THEN ttp.ref
                                    WHEN id_type_intrinsic_value IS NOT NULL THEN tiv.ref END) AS object
                                FROM account ac
                                JOIN user_right ur ON ac.id = ur.id_account
                                LEFT JOIN test_mean tm ON tm.id = ur.id_test_mean
                                LEFT JOIN type_coating tc ON tc.id = ur.id_type_coating
                                LEFT JOIN type_detergent td ON td.id = ur.id_type_detergent
                                LEFT JOIN type_tank tt ON tt.id = ur.id_type_tank
                                LEFT JOIN type_sensor ts ON ts.id = ur.id_type_sensor
                                LEFT JOIN type_ejector te ON te.id = ur.id_type_ejector
                                LEFT JOIN type_camera tca ON tca.id = ur.id_type_camera
                                LEFT JOIN type_test_point ttp ON ttp.id = ur.id_type_test_point
                                LEFT JOIN type_intrinsic_value tiv ON tiv.id = ur.id_type_intrinsic_value
                                
                                WHERE ac.uname = %s
                        """
                        self.cur.execute(sql_ac, (uname,))
                        self.conn.commit()
                        row = self.cur.fetchone()
                        self.fname.setCurrentText(row[0])
                        self.lname.setCurrentText(row[1])
                        self.tel.setText(row[2])
                        self.email.setText(row[3])
                        
                        self.delRight()
                        self.cur.execute(sql_role, (uname,))
                        self.conn.commit()
                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addRight(*(row[0:]))
                    if (uname.isspace() or uname == ''):
                        sql = """SELECT DISTINCT fname FROM account WHERE orga = %s;"""
                        self.cur.execute(sql, (orga, ))
                        self.conn.commit()
                        fname = []
                        rows = self.cur.fetchall()
                        for row in rows :
                            fname.append(row[0])
                        self.fname.clear()
                        self.fname.addItems(fname)   
                    return True
                return False   

            if obj == self.fname :
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    self.fname.showPopup()
                    self.fname.view().viewport().installEventFilter(self)
                    return True
                if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return) :
                    fname = self.fname.currentText()
                    orga = self.orga.currentText()
                    uname = self.uname.currentText()
                    if uname.isspace() or uname == '' :
                        sql = """SELECT DISTINCT lname FROM account WHERE orga = %s AND fname = %s;"""
                        self.cur.execute(sql, (orga, fname))
                        self.conn.commit()
                        lname = []
                        rows = self.cur.fetchall()
                        for row in rows :
                            lname.append(row[0])
                        self.lname.clear()
                        self.lname.addItems(lname)
                    self.lname.setFocus()
                    return True
                return False
            if obj == self.fname.view().viewport():
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    index = self.fname.view().currentIndex().row()
                    fname = self.fname.itemText(index)
                    uname = self.uname.currentText()
                    orga = self.orga.currentText()
                    if uname.isspace() or uname == '' :
                        sql = """SELECT DISTINCT lname FROM account WHERE orga = %s AND fname = %s;"""
                        self.cur.execute(sql, (orga, fname))
                        self.conn.commit()
                        lname = []
                        rows = self.cur.fetchall()
                        for row in rows :
                            lname.append(row[0])
                        self.lname.clear()
                        self.lname.addItems(lname)
                    return True
                return False
            if obj == self.lname :
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    self.lname.showPopup()
                    self.lname.view().viewport().installEventFilter(self)
                    return True
                if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return) :
                    lname = self.lname.currentText()
                    fname = self.fname.currentText()
                    orga = self.orga.currentText()
                    uname = self.uname.currentText()
                    if uname.isspace() or uname == '' :
                        sql = """SELECT uname FROM account WHERE orga = %s AND fname = %s AND lname = %s;"""
                        self.cur.execute(sql, (orga, fname, lname))
                        self.conn.commit()

                        lst = []
                        rows = self.cur.fetchall()
                        for row in rows :
                            lst.append(row[0])
                        self.uname.clear()
                        self.uname.addItems(lst)                        
                        self.uname.setFocus()
                    else :
                        self.tel.setFocus()
                    return True
                return False
            if obj == self.lname.view().viewport():
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    index = self.lname.view().currentIndex().row()
                    lname = self.lname.itemText(index)
                    fname = self.fname.currentText()
                    uname = self.uname.currentText()
                    orga = self.orga.currentText()
                    if uname.isspace() or uname == '' :
                        sql = """SELECT uname FROM account WHERE orga = %s AND fname = %s AND lname = %s;"""
                        self.cur.execute(sql, (orga, fname, lname))
                        self.conn.commit()
                        lst = []
                        rows = self.cur.fetchall()
                        for row in rows :
                            lst.append(row[0])
                        self.uname.clear()
                        self.uname.addItems(lst)
                    return True
                return False
        if (self.tabs.currentIndex() == 1) :
            ######################################
            # Event on Combobox of Type of AC/WT #
            ######################################
            if obj == self.test_mean_type : 
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    self.test_mean_type.showPopup()
                    self.test_mean_type.view().viewport().installEventFilter(self)
                    return True        
                if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Tab :    
                    gen = self.test_mean_type.currentText()
                    if not gen.isspace() and gen != '' :
                        test_mean_name = []
                        sql = """SELECT DISTINCT name FROM test_mean WHERE type = %s;"""
                        self.cur.execute(sql, (gen,))
                        self.conn.commit()
                        rows = self.cur.fetchall()
                        for row in rows :
                            test_mean_name.append(row[0])
                        self.test_mean_name.clear()
                        self.test_mean_name.addItems(test_mean_name)
                    self.test_mean_name.setFocus()
                    self.coating_type.setCurrentText('')
                    self.detergent_type.setCurrentText('')
                    self.tank_type.setCurrentText('')
                    self.sensor_type.setCurrentText('')
                    self.ejector_type.setCurrentText('')
                    self.camera_type.setCurrentText('')
                    self.test_point_type.setCurrentText('')
                    self.intrinsic_value_type.setCurrentText('')
                    return True
                return False
        
            if obj == self.test_mean_type.view().viewport() :
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    index = self.test_mean_type.view().currentIndex().row()
                    gen = self.test_mean_type.itemText(index)
                    test_mean_type = []
                    sql = """SELECT DISTINCT name FROM test_mean WHERE type = %s;"""
                    self.cur.execute(sql, (gen, ))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    for row in rows :
                        test_mean_type.append(row[0])
                    self.test_mean_name.clear()
                    self.test_mean_name.addItems(test_mean_type)
                    self.test_mean_name.setFocus()
                    self.test_mean_type.view().viewport().removeEventFilter(self)
                    self.coating_type.setCurrentText('')
                    self.detergent_type.setCurrentText('')
                    self.tank_type.setCurrentText('')
                    self.sensor_type.setCurrentText('')
                    self.ejector_type.setCurrentText('')
                    self.camera_type.setCurrentText('')
                    self.test_point_type.setCurrentText('')
                    self.intrinsic_value_type.setCurrentText('')
                    return True
                return False
            ######################################
            # Event on Combobox of Name of AC/WT #
            ######################################
            if obj == self.test_mean_name :      
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    self.test_mean_name.showPopup()
                    self.test_mean_name.view().viewport().installEventFilter(self)
                    return True   
                if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Tab :         
                    gen = self.test_mean_type.currentText()
                    nom = self.test_mean_name.currentText()
                    if not gen.isspace() and gen != '' and not nom.isspace() and nom != '':
                        test_mean_num = []
                        sql = """SELECT number FROM test_mean WHERE type = %s AND name = %s;"""
                        self.cur.execute(sql, (gen, nom))
                        self.conn.commit()
                        rows = self.cur.fetchall()
                        for row in rows :
                            test_mean_num.append(str(row[0]))
                        self.test_mean_num.clear()
                        self.test_mean_num.addItems(test_mean_num)
                    self.test_mean_num.setFocus()
                    return True   
                return False

            if obj == self.test_mean_name.view().viewport() :
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    index = self.test_mean_name.view().currentIndex().row()
                    nom = self.test_mean_name.itemText(index)
                    gen = self.test_mean_type.currentText()
                    test_mean_num = []
                    sql = """SELECT number FROM test_mean WHERE type = %s AND name = %s;"""
                    self.cur.execute(sql, (gen, nom))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    for row in rows :
                        test_mean_num.append(str(row[0]))
                    self.test_mean_num.clear()
                    self.test_mean_num.addItems(test_mean_num)
                    self.test_mean_num.setFocus()
                    self.test_mean_name.view().viewport().removeEventFilter(self)
                    return True
                return False


            if obj == self.test_mean_num :        
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    self.test_mean_num.showPopup()
                    self.test_mean_num.view().viewport().installEventFilter(self)
                    return True
                if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):      
                    num = self.test_mean_num.currentText()
                    nom = self.test_mean_name.currentText()
                    gen = self.test_mean_type.currentText()
                    if ~gen.isspace() and gen != '' and ~nom.isspace() and nom != '' and ~num.isspace() and num != '':
                        if gen not in [self.test_mean_type.itemText(i) for i in range(self.test_mean_type.count())] :
                            self.test_mean_type.addItem(gen)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN test_mean tm ON tm.id = ur.id_test_mean
                                    WHERE tm.type = %s AND tm.name = %s AND tm.number = %s or ur.role = 'manager')
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (gen, nom, num))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 
                        
                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN test_mean tm ON tm.id = ur.id_test_mean
                                    WHERE tm.type = %s AND tm.name = %s AND tm.number = %s;
                        """
                        self.cur.execute(sql, (gen, nom, num))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False

            if obj == self.test_mean_num.view().viewport() :
                index = self.test_mean_num.view().currentIndex().row()
                num = self.test_mean_num.itemText(index)
                nom = self.test_mean_name.currentText()
                gen = self.test_mean_type.currentText()
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    if ~gen.isspace() and gen != '' and ~nom.isspace() and nom != '' and ~num.isspace() and num != '':
                        if gen not in [self.test_mean_type.itemText(i) for i in range(self.test_mean_type.count())] :
                            self.test_mean_type.addItem(gen)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN test_mean tm ON tm.id = ur.id_test_mean
                                    WHERE tm.type = %s AND tm.name = %s AND tm.number = %s or ur.role = 'manager')
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (gen, nom, num))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 

                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN test_mean tm ON tm.id = ur.id_test_mean
                                    WHERE tm.type = %s AND tm.name = %s AND tm.number = %s;
                        """
                        self.cur.execute(sql, (gen, nom, num))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False
            if obj == self.coating_type :     
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    self.coating_type.showPopup()
                    self.coating_type.view().viewport().installEventFilter(self)
                    return True
                if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):      
                    type_coating = self.coating_type.currentText()
                    if ~type_coating.isspace() and type_coating != '':
                        self.test_mean_type.setCurrentText('')
                        self.test_mean_name.setCurrentText('')
                        self.test_mean_num.setCurrentText('')
                        self.detergent_type.setCurrentText('')
                        self.tank_type.setCurrentText('')
                        self.sensor_type.setCurrentText('')
                        self.ejector_type.setCurrentText('')
                        self.camera_type.setCurrentText('')
                        self.test_point_type.setCurrentText('')
                        self.intrinsic_value_type.setCurrentText('')   
                        if type_coating not in [self.coating_type.itemText(i) for i in range(self.coating_type.count())] :
                            self.coating_type.addItem(type_coating)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN type_coating tc ON tc.id = ur.id_type_coating
                                    WHERE tc.ref = %s or ur.role = 'manager')
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (type_coating, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 
                        
                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN type_coating tc ON tc.id = ur.id_type_coating
                                    WHERE tc.ref = %s;
                        """
                        self.cur.execute(sql, (type_coating, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False 
            if obj == self.coating_type.view().viewport() :
                index = self.coating_type.view().currentIndex().row()
                type_coating = self.coating_type.itemText(index)
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    if ~type_coating.isspace() and type_coating != '':
                        self.test_mean_type.setCurrentText('')
                        self.test_mean_name.setCurrentText('')
                        self.test_mean_num.setCurrentText('')
                        self.detergent_type.setCurrentText('')
                        self.tank_type.setCurrentText('')
                        self.sensor_type.setCurrentText('')
                        self.ejector_type.setCurrentText('')
                        self.camera_type.setCurrentText('')
                        self.test_point_type.setCurrentText('')
                        self.intrinsic_value_type.setCurrentText('')   
                        if type_coating not in [self.coating_type.itemText(i) for i in range(self.coating_type.count())] :
                            self.coating_type.addItem(type_coating)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN type_coating tc ON tc.id = ur.id_type_coating
                                    WHERE tc.ref = %s or ur.role = 'manager')
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (type_coating, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 
                        
                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN type_coating tc ON tc.id = ur.id_type_coating
                                    WHERE tc.ref = %s;
                        """
                        self.cur.execute(sql, (type_coating, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False 
            if obj == self.detergent_type :       
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    self.detergent_type.showPopup()
                    self.detergent_type.view().viewport().installEventFilter(self)
                    return True
                if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):      
                    type_detergent = self.detergent_type.currentText()
                    self.test_mean_type.setCurrentText('')
                    self.test_mean_name.setCurrentText('')
                    self.test_mean_num.setCurrentText('')
                    self.coating_type.setCurrentText('')
                    self.tank_type.setCurrentText('')
                    self.sensor_type.setCurrentText('')
                    self.ejector_type.setCurrentText('')
                    self.camera_type.setCurrentText('')
                    self.test_point_type.setCurrentText('')
                    self.intrinsic_value_type.setCurrentText('') 
                    if ~type_detergent.isspace() and type_detergent != '':
                        if type_detergent not in [self.detergent_type.itemText(i) for i in range(self.detergent_type.count())] :
                            self.detergent_type.addItem(type_detergent)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN type_detergent td ON td.id = ur.id_type_detergent
                                    WHERE td.ref = %s or ur.role = 'manager')
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (type_detergent, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 
                        
                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN type_detergent td ON td.id = ur.id_type_detergent
                                    WHERE td.ref = %s;
                        """
                        self.cur.execute(sql, (type_detergent, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False
            if obj == self.detergent_type.view().viewport() :
                index = self.detergent_type.view().currentIndex().row()
                type_detergent = self.detergent_type.itemText(index)
                self.test_mean_type.setCurrentText('')
                self.test_mean_name.setCurrentText('')
                self.test_mean_num.setCurrentText('')
                self.coating_type.setCurrentText('')
                self.tank_type.setCurrentText('')
                self.sensor_type.setCurrentText('')
                self.ejector_type.setCurrentText('')
                self.camera_type.setCurrentText('')
                self.test_point_type.setCurrentText('')
                self.intrinsic_value_type.setCurrentText('') 
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    if ~type_detergent.isspace() and type_detergent != '':
                        if type_detergent not in [self.detergent_type.itemText(i) for i in range(self.detergent_type.count())] :
                            self.detergent_type.addItem(type_detergent)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN type_detergent td ON td.id = ur.id_type_detergent
                                    WHERE td.ref = %s or ur.role = 'manager')
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (type_detergent, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 
                        
                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN type_detergent td ON td.id = ur.id_type_detergent
                                    WHERE td.ref = %s;
                        """
                        self.cur.execute(sql, (type_detergent, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False
            if obj == self.tank_type :       
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    self.tank_type.showPopup()
                    self.tank_type.view().viewport().installEventFilter(self)
                    return True
                if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):      
                    type_tank = self.tank_type.currentText()
                    self.test_mean_type.setCurrentText('')
                    self.test_mean_name.setCurrentText('')
                    self.test_mean_num.setCurrentText('')
                    self.coating_type.setCurrentText('')
                    self.detergent_type.setCurrentText('')
                    self.sensor_type.setCurrentText('')
                    self.ejector_type.setCurrentText('')
                    self.camera_type.setCurrentText('')
                    self.test_point_type.setCurrentText('')
                    self.intrinsic_value_type.setCurrentText('') 
                    if ~type_tank.isspace() and type_tank != '':
                        if type_tank not in [self.tank_type.itemText(i) for i in range(self.tank_type.count())] :
                            self.tank_type.addItem(type_tank)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN type_tank tt ON tt.id = ur.id_type_tank
                                    WHERE tt.ref = %s or ur.role = 'manager')
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (type_tank, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 
                        
                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN type_tank tt ON tt.id = ur.id_type_tank
                                    WHERE tt.ref = %s;
                        """
                        self.cur.execute(sql, (type_tank, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False
            if obj == self.tank_type.view().viewport() :
                index = self.tank_type.view().currentIndex().row()
                type_tank = self.tank_type.itemText(index)
                self.test_mean_type.setCurrentText('')
                self.test_mean_name.setCurrentText('')
                self.test_mean_num.setCurrentText('')
                self.coating_type.setCurrentText('')
                self.detergent_type.setCurrentText('')
                self.sensor_type.setCurrentText('')
                self.ejector_type.setCurrentText('')
                self.camera_type.setCurrentText('')
                self.test_point_type.setCurrentText('')
                self.intrinsic_value_type.setCurrentText('') 
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    if ~type_tank.isspace() and type_tank != '':
                        if type_tank not in [self.tank_type.itemText(i) for i in range(self.tank_type.count())] :
                            self.tank_type.addItem(type_tank)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN type_tank tt ON tt.id = ur.id_type_tank
                                    WHERE tt.ref = %s or ur.role = 'manager')
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (type_tank, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 
                        
                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN type_tank tt ON tt.id = ur.id_type_tank
                                    WHERE tt.ref = %s;
                        """
                        self.cur.execute(sql, (type_tank, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False
            if obj == self.sensor_type :       
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    self.sensor_type.showPopup()
                    self.sensor_type.view().viewport().installEventFilter(self)
                    return True
                if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):      
                    type_sensor = self.sensor_type.currentText()
                    self.test_mean_type.setCurrentText('')
                    self.test_mean_name.setCurrentText('')
                    self.test_mean_num.setCurrentText('')
                    self.coating_type.setCurrentText('')
                    self.detergent_type.setCurrentText('')
                    self.tank_type.setCurrentText('')
                    self.ejector_type.setCurrentText('')
                    self.camera_type.setCurrentText('')
                    self.test_point_type.setCurrentText('')
                    self.intrinsic_value_type.setCurrentText('') 
                    if ~type_sensor.isspace() and type_sensor != '':
                        if type_sensor not in [self.sensor_type.itemText(i) for i in range(self.sensor_type.count())] :
                            self.sensor_type.addItem(type_sensor)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN type_sensor ts ON ts.id = ur.id_type_sensor
                                    WHERE ts.ref = %s or ur.role = 'manager')
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (type_sensor, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 
                        
                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN type_sensor ts ON ts.id = ur.id_type_sensor
                                    WHERE ts.ref = %s;
                        """
                        self.cur.execute(sql, (type_sensor, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False
            if obj == self.sensor_type.view().viewport() :
                index = self.sensor_type.view().currentIndex().row()
                type_sensor = self.sensor_type.itemText(index)
                self.test_mean_type.setCurrentText('')
                self.test_mean_name.setCurrentText('')
                self.test_mean_num.setCurrentText('')
                self.coating_type.setCurrentText('')
                self.detergent_type.setCurrentText('')
                self.tank_type.setCurrentText('')
                self.ejector_type.setCurrentText('')
                self.camera_type.setCurrentText('')
                self.test_point_type.setCurrentText('')
                self.intrinsic_value_type.setCurrentText('') 
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    if ~type_sensor.isspace() and type_sensor != '':
                        if type_sensor not in [self.sensor_type.itemText(i) for i in range(self.sensor_type.count())] :
                            self.sensor_type.addItem(type_sensor)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN type_sensor ts ON ts.id = ur.id_type_sensor
                                    WHERE ts.ref = %s or ur.role = 'manager')
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (type_sensor, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 
                        
                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN type_sensor ts ON ts.id = ur.id_type_sensor
                                    WHERE ts.ref = %s;
                        """
                        self.cur.execute(sql, (type_sensor, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False
            if obj == self.ejector_type :       
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    self.ejector_type.showPopup()
                    self.ejector_type.view().viewport().installEventFilter(self)
                    return True
                if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):      
                    type_ejector= self.ejector_type.currentText()
                    self.test_mean_type.setCurrentText('')
                    self.test_mean_name.setCurrentText('')
                    self.test_mean_num.setCurrentText('')
                    self.coating_type.setCurrentText('')
                    self.detergent_type.setCurrentText('')
                    self.tank_type.setCurrentText('')
                    self.sensor_type.setCurrentText('')
                    self.camera_type.setCurrentText('')
                    self.test_point_type.setCurrentText('')
                    self.intrinsic_value_type.setCurrentText('') 
                    if ~type_ejector.isspace() and type_ejector!= '':
                        if type_ejector not in [self.ejector_type.itemText(i) for i in range(self.ejector_type.count())] :
                            self.ejector_type.addItem(type_ejector)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN type_ejector te ON te.id = ur.id_type_sensor
                                    WHERE te.ref = %s or ur.role = 'manager')
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (type_ejector, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 
                        
                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN type_ejector te ON te.id = ur.id_type_sensor
                                    WHERE te.ref = %s;
                        """
                        self.cur.execute(sql, (type_ejector, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False
            if obj == self.ejector_type.view().viewport() :
                index = self.ejector_type.view().currentIndex().row()
                type_ejector= self.ejector_type.itemText(index)
                self.test_mean_type.setCurrentText('')
                self.test_mean_name.setCurrentText('')
                self.test_mean_num.setCurrentText('')
                self.coating_type.setCurrentText('')
                self.detergent_type.setCurrentText('')
                self.tank_type.setCurrentText('')
                self.sensor_type.setCurrentText('')
                self.camera_type.setCurrentText('')
                self.test_point_type.setCurrentText('')
                self.intrinsic_value_type.setCurrentText('') 
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    if ~type_ejector.isspace() and type_ejector!= '':
                        if type_ejector not in [self.ejector_type.itemText(i) for i in range(self.ejector_type.count())] :
                            self.ejector_type.addItem(type_ejector)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN type_ejector te ON te.id = ur.id_type_sensor
                                    WHERE te.ref = %s OR ur.role = 'manager')
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (type_ejector, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 
                        
                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN type_ejector te ON te.id = ur.id_type_sensor
                                    WHERE te.ref = %s;
                        """
                        self.cur.execute(sql, (type_ejector, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False
            if obj == self.camera_type :       
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    self.camera_type.showPopup()
                    self.camera_type.view().viewport().installEventFilter(self)
                    return True
                if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):      
                    type_camera = self.camera_type.currentText()
                    self.test_mean_type.setCurrentText('')
                    self.test_mean_name.setCurrentText('')
                    self.test_mean_num.setCurrentText('')
                    self.coating_type.setCurrentText('')
                    self.detergent_type.setCurrentText('')
                    self.tank_type.setCurrentText('')
                    self.sensor_type.setCurrentText('')
                    self.ejector_type.setCurrentText('')
                    self.test_point_type.setCurrentText('')
                    self.intrinsic_value_type.setCurrentText('') 
                    if ~type_camera.isspace() and type_camera!= '':
                        if type_camera not in [self.camera_type.itemText(i) for i in range(self.camera_type.count())] :
                            self.camera_type.addItem(type_camera)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN type_camera tc ON tc.id = ur.id_type_sensor
                                    WHERE tc.ref = %s)
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (type_camera, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 
                        
                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN type_camera tc ON tc.id = ur.id_type_sensor
                                    WHERE tc.ref = %s;
                        """
                        self.cur.execute(sql, (type_camera, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False
            if obj == self.camera_type.view().viewport() :
                index = self.camera_type.view().currentIndex().row()
                type_camera = self.camera_type.itemText(index)
                self.test_mean_type.setCurrentText('')
                self.test_mean_name.setCurrentText('')
                self.test_mean_num.setCurrentText('')
                self.coating_type.setCurrentText('')
                self.detergent_type.setCurrentText('')
                self.tank_type.setCurrentText('')
                self.sensor_type.setCurrentText('')
                self.ejector_type.setCurrentText('')
                self.test_point_type.setCurrentText('')
                self.intrinsic_value_type.setCurrentText('') 
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    if ~type_camera.isspace() and type_camera!= '':
                        if type_camera not in [self.camera_type.itemText(i) for i in range(self.camera_type.count())] :
                            self.camera_type.addItem(type_camera)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN type_camera tc ON tc.id = ur.id_type_sensor
                                    WHERE tc.ref = %s)
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (type_camera, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 
                        
                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN type_camera tc ON tc.id = ur.id_type_sensor
                                    WHERE tc.ref = %s;
                        """
                        self.cur.execute(sql, (type_camera, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False
            if obj == self.test_point_type :       
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    self.test_point_type.showPopup()
                    self.test_point_type.view().viewport().installEventFilter(self)
                    return True
                if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):      
                    type_test_point= self.test_point_type.currentText()
                    self.test_mean_type.setCurrentText('')
                    self.test_mean_name.setCurrentText('')
                    self.test_mean_num.setCurrentText('')
                    self.coating_type.setCurrentText('')
                    self.detergent_type.setCurrentText('')
                    self.tank_type.setCurrentText('')
                    self.sensor_type.setCurrentText('')
                    self.ejector_type.setCurrentText('')
                    self.camera_type.setCurrentText('')
                    self.intrinsic_value_type.setCurrentText('') 
                    if ~type_test_point.isspace() and type_test_point!= '':
                        if type_test_point not in [self.test_point_type.itemText(i) for i in range(self.test_point_type.count())] :
                            self.test_point_type.addItem(type_test_point)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN type_test_point ttp ON ttp.id = ur.id_type_sensor
                                    WHERE ttp.ref = %s)
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (type_test_point, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 
                        
                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN type_test_point ttp ON ttp.id = ur.id_type_sensor
                                    WHERE ttp.ref = %s;
                        """
                        self.cur.execute(sql, (type_test_point, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False
            if obj == self.test_point_type.view().viewport() :
                index = self.test_point_type.view().currentIndex().row()
                type_ejector= self.test_point_type.itemText(index)
                self.test_mean_type.setCurrentText('')
                self.test_mean_name.setCurrentText('')
                self.test_mean_num.setCurrentText('')
                self.coating_type.setCurrentText('')
                self.detergent_type.setCurrentText('')
                self.tank_type.setCurrentText('')
                self.sensor_type.setCurrentText('')
                self.ejector_type.setCurrentText('')
                self.camera_type.setCurrentText('')
                self.intrinsic_value_type.setCurrentText('') 
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    if ~type_test_point.isspace() and type_test_point!= '':
                        if type_test_point not in [self.test_point_type.itemText(i) for i in range(self.test_point_type.count())] :
                            self.test_point_type.addItem(type_test_point)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN type_test_point ttp ON ttp.id = ur.id_type_sensor
                                    WHERE ttp.ref = %s)
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (type_test_point, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 
                        
                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN type_test_point ttp ON ttp.id = ur.id_type_sensor
                                    WHERE ttp.ref = %s;
                        """
                        self.cur.execute(sql, (type_test_point, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False
            if obj == self.intrinsic_value_type :       
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    self.intrinsic_value_type.showPopup()
                    self.intrinsic_value_type.view().viewport().installEventFilter(self)
                    return True
                if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):      
                    type_intrinsic_value= self.intrinsic_value_type.currentText()
                    self.test_mean_type.setCurrentText('')
                    self.test_mean_name.setCurrentText('')
                    self.test_mean_num.setCurrentText('')
                    self.coating_type.setCurrentText('')
                    self.detergent_type.setCurrentText('')
                    self.tank_type.setCurrentText('')
                    self.sensor_type.setCurrentText('')
                    self.ejector_type.setCurrentText('')
                    self.camera_type.setCurrentText('')
                    self.test_point_type.setCurrentText('') 
                    if ~type_intrinsic_value.isspace() and type_intrinsic_value!= '':
                        if type_intrinsic_value not in [self.intrinsic_value_type.itemText(i) for i in range(self.intrinsic_value_type.count())] :
                            self.intrinsic_value_type.addItem(type_intrinsic_value)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN type_intricsic_value tiv ON tiv.id = ur.id_type_sensor
                                    WHERE tiv.ref = %s)
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (type_intrinsic_value, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 
                        
                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN type_intricsic_value tiv ON tiv.id = ur.id_type_sensor
                                    WHERE tiv.ref = %s;
                        """
                        self.cur.execute(sql, (type_intrinsic_value, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False
            if obj == self.intrinsic_value_type.view().viewport() :
                index = self.intrinsic_value_type.view().currentIndex().row()
                type_intrinsic_value= self.intrinsic_value_type.itemText(index)
                self.test_mean_type.setCurrentText('')
                self.test_mean_name.setCurrentText('')
                self.test_mean_num.setCurrentText('')
                self.coating_type.setCurrentText('')
                self.detergent_type.setCurrentText('')
                self.tank_type.setCurrentText('')
                self.sensor_type.setCurrentText('')
                self.intrinsic_value_type.setCurrentText('')
                self.intrinsic_value_type.setCurrentText('')
                self.intrinsic_value_type.setCurrentText('') 
                if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                    if ~type_intrinsic_value.isspace() and type_intrinsic_value!= '':
                        if type_intrinsic_value not in [self.intrinsic_value_type.itemText(i) for i in range(self.intrinsic_value_type.count())] :
                            self.intrinsic_value_type.addItem(type_intrinsic_value)
                        sql = """WITH d AS (SELECT ac.id
                                    FROM account ac
                                    LEFT JOIN user_right ur ON ac.id = ur.id_account
                                    LEFT JOIN type_intricsic_value tiv ON tiv.id = ur.id_type_sensor
                                    WHERE tiv.ref = %s)
                                    SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                    FROM account ac 
                                    LEFT JOIN d ON ac.id = d.id
                                    WHERE d.id IS NULL;
                        """
                        self.cur.execute(sql, (type_intrinsic_value, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_other.removeRows(0, self.model_other.rowCount())

                        for row in rows :
                            self.addOther(*(row[0:])) 
                        
                        self.model_author.removeRows(0, self.model_author.rowCount())
                        sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                                    FROM account ac
                                    JOIN user_right ur ON ac.id = ur.id_account
                                    JOIN type_intricsic_value tiv ON tiv.id = ur.id_type_sensor
                                    WHERE tiv.ref = %s;
                        """
                        self.cur.execute(sql, (type_intrinsic_value, ))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addAuthor(*(row[0:]))
                    return True
                return False
        return False
    
    def return_other(self) :
        test_mean_type = self.test_mean_type.currentText()

        test_mean_name = self.test_mean_name.currentText()

        test_mean_num = self.test_mean_num.currentText()

        type_coating = self.coating_type.currentText()

        type_detergent = self.detergent_type.currentText()

        type_tank = self.tank_type.currentText()

        type_sensor = self.sensor_type.currentText()

        type_ejector = self.ejector_type.currentText()

        type_camera = self.camera_type.currentText()

        type_test_point = self.test_point_type.currentText()

        type_intrinsic_value = self.intrinsic_value_type.currentText()
        if 'admin' not in [i[0] for i in self.lst] and 'manager' not in [i[0] for i in self.lst]:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("You are not allowed to do this")
            msg.setWindowTitle("validate Fail")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        if  (~test_mean_type.isspace() and test_mean_type != '') and  (~test_mean_name.isspace() and test_mean_name != '')  and  (~test_mean_num.isspace() and test_mean_num != '') :
            if '_'.join([test_mean_type, test_mean_name, test_mean_num]) not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'test mean'] and 'manager' not in [i[0] for i in self.lst]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        if (~type_coating.isspace() and type_coating != '') :
            if type_coating not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'coating'] and 'manager' not in [i[0] for i in self.lst]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        if (~type_detergent.isspace() and type_detergent != '') :
            if type_detergent not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'detergent'] and 'manager' not in [i[0] for i in self.lst] :
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        if (~type_tank.isspace() and type_tank != '') :
            if type_tank not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'tank'] and 'manager' not in [i[0] for i in self.lst]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        if (~type_sensor.isspace() and type_sensor != '') :
            if type_sensor not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'sensor'] and 'manager' not in [i[0] for i in self.lst]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        if (~type_ejector.isspace() and type_ejector != '') :
            if type_ejector not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'ejector'] and 'manager' not in [i[0] for i in self.lst]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        if (~type_camera.isspace() and type_camera != '') :
            if type_camera not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'camera'] and 'manager' not in [i[0] for i in self.lst]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        if (~type_test_point.isspace() and type_test_point != '') :
            if type_test_point not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'test point'] and 'manager' not in [i[0] for i in self.lst]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        if (~type_intrinsic_value.isspace() and type_intrinsic_value != '') :
            if type_intrinsic_value not in [i[2] for i in self.lst if i[0] == 'admin' and i[1] == 'intrinsic value'] and 'manager' not in [i[0] for i in self.lst]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You are not allowed to do this")
                msg.setWindowTitle("Validate Fail")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
        select_author = self.list_author_tree.selectedIndexes()[0].row()
        fname = self.model_author.data(self.model_author.index(select_author, 0))
        lname = self.model_author.data(self.model_author.index(select_author, 1))
        orga = self.model_author.data(self.model_author.index(select_author, 2))
        tel = self.model_author.data(self.model_author.index(select_author, 3))
        uname = self.model_author.data(self.model_author.index(select_author, 5))
        self.delAuthor(select_author)
        self.addOther(fname, lname, orga, tel, uname)
        

    def cancel(self) :
        if (self.tabs.currentIndex() == 0) :
            self.init_user()
            self.model_user.removeRows(0, self.model_user.rowCount())
            sql = """SELECT orga, uname, fname, lname, tel, email FROM account;"""
            self.cur.execute(sql)
            self.conn.commit()
            rows = self.cur.fetchall()    
            for row in rows :
                self.addUser(*(row[0:]))
        else :
            self.model_other.removeRows(0, self.model_other.rowCount())
            self.model_author.removeRows(0, self.model_author.rowCount())
            test_mean_num = self.test_mean_num.currentText()
            test_mean_name = self.test_mean_name.currentText()
            test_mean_type = self.test_mean_type.currentText()
            type_coating = self.coating_type.currentText()
            type_detergent = self.detergent_type.currentText()
            type_tank = self.tank_type.currentText()
            type_sensor = self.sensor_type.currentText()
            type_ejector = self.ejector_type.currentText()
            type_camera = self.camera_type.currentText()
            type_test_point = self.test_point_type.currentText()
            type_intrinsic_value = self.intrinsic_value_type.currentText()
            if ~test_mean_type.isspace() and test_mean_type != '' and ~test_mean_name.isspace() and test_mean_name != '' and ~test_mean_num.isspace() and test_mean_num != '':
                sql = """WITH d AS (SELECT ac.id
                            FROM account ac
                            LEFT JOIN user_right ur ON ac.id = ur.id_account
                            LEFT JOIN test_mean tm ON tm.id = ur.id_test_mean
                            WHERE tm.type = %s AND tm.name = %s AND tm.number = %s or ur.role = 'manager')
                            SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                            FROM account ac 
                            LEFT JOIN d ON ac.id = d.id
                            WHERE d.id IS NULL;
                """
                self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num))
                self.conn.commit()

                rows = self.cur.fetchall()
                
                for row in rows :
                    self.addOther(*(row[0:])) 
                
                sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                            FROM account ac
                            JOIN user_right ur ON ac.id = ur.id_account
                            JOIN test_mean tm ON tm.id = ur.id_test_mean
                            WHERE tm.type = %s AND tm.name = %s AND tm.number = %s;
                """
                self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num))
                self.conn.commit()

                rows = self.cur.fetchall()
                for row in rows :
                    self.addAuthor(*(row[0:]))

            if ~type_coating.isspace() and type_coating != '':
                sql = """WITH d AS (SELECT ac.id
                                                FROM account ac
                                                LEFT JOIN user_right ur ON ac.id = ur.id_account
                                                LEFT JOIN type_coating tc ON tc.id = ur.id_type_coating
                                                WHERE tc.ref = %s or ur.role = 'manager')
                                                SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                                                FROM account ac 
                                                LEFT JOIN d ON ac.id = d.id
                                                WHERE d.id IS NULL;
                                    """
                self.cur.execute(sql, (type_coating, ))
                self.conn.commit()

                rows = self.cur.fetchall()
                

                for row in rows :
                    self.addOther(*(row[0:])) 
                
                sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                            FROM account ac
                            JOIN user_right ur ON ac.id = ur.id_account
                            JOIN type_coating tc ON tc.id = ur.id_type_coating
                            WHERE tc.ref = %s;
                """
                self.cur.execute(sql, (type_coating, ))
                self.conn.commit()

                rows = self.cur.fetchall()
                for row in rows :
                    self.addAuthor(*(row[0:]))
            if ~type_detergent.isspace() and type_detergent != '':                                    
                sql = """WITH d AS (SELECT ac.id
                            FROM account ac
                            LEFT JOIN user_right ur ON ac.id = ur.id_account
                            LEFT JOIN type_detergent td ON td.id = ur.id_type_detergent
                            WHERE td.ref = %s or ur.role = 'manager')
                            SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                            FROM account ac 
                            LEFT JOIN d ON ac.id = d.id
                            WHERE d.id IS NULL;
                """
                self.cur.execute(sql, (type_detergent, ))
                self.conn.commit()

                rows = self.cur.fetchall()
                
                self.model_other.removeRows(0, self.model_other.rowCount())

                for row in rows :
                    self.addOther(*(row[0:])) 
                
                self.model_author.removeRows(0, self.model_author.rowCount())
                sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                            FROM account ac
                            JOIN user_right ur ON ac.id = ur.id_account
                            JOIN type_detergent td ON td.id = ur.id_type_detergent
                            WHERE td.ref = %s;
                """
                self.cur.execute(sql, (type_detergent, ))
                self.conn.commit()

                rows = self.cur.fetchall()
                for row in rows :
                    self.addAuthor(*(row[0:]))
            if ~type_tank.isspace() and type_tank != '':
                sql = """WITH d AS (SELECT ac.id
                            FROM account ac
                            LEFT JOIN user_right ur ON ac.id = ur.id_account
                            LEFT JOIN type_tank tt ON tt.id = ur.id_type_tank
                            WHERE tt.ref = %s or ur.role = 'manager')
                            SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                            FROM account ac 
                            LEFT JOIN d ON ac.id = d.id
                            WHERE d.id IS NULL;
                """
                self.cur.execute(sql, (type_tank, ))
                self.conn.commit()

                rows = self.cur.fetchall()
                
                self.model_other.removeRows(0, self.model_other.rowCount())

                for row in rows :
                    self.addOther(*(row[0:])) 
                
                self.model_author.removeRows(0, self.model_author.rowCount())
                sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                            FROM account ac
                            JOIN user_right ur ON ac.id = ur.id_account
                            JOIN type_tank tt ON tt.id = ur.id_type_tank
                            WHERE tt.ref = %s;
                """
                self.cur.execute(sql, (type_tank, ))
                self.conn.commit()

                rows = self.cur.fetchall()
                for row in rows :
                    self.addAuthor(*(row[0:]))
            if ~type_sensor.isspace() and type_sensor != '':                       
                sql = """WITH d AS (SELECT ac.id
                            FROM account ac
                            LEFT JOIN user_right ur ON ac.id = ur.id_account
                            LEFT JOIN type_sensor ts ON ts.id = ur.id_type_sensor
                            WHERE ts.ref = %s or ur.role = 'manager')
                            SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                            FROM account ac 
                            LEFT JOIN d ON ac.id = d.id
                            WHERE d.id IS NULL;
                """
                self.cur.execute(sql, (type_sensor, ))
                self.conn.commit()

                rows = self.cur.fetchall()
                
                self.model_other.removeRows(0, self.model_other.rowCount())

                for row in rows :
                    self.addOther(*(row[0:])) 
                
                self.model_author.removeRows(0, self.model_author.rowCount())
                sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                            FROM account ac
                            JOIN user_right ur ON ac.id = ur.id_account
                            JOIN type_sensor ts ON ts.id = ur.id_type_sensor
                            WHERE ts.ref = %s;
                """
                self.cur.execute(sql, (type_sensor, ))
                self.conn.commit()

                rows = self.cur.fetchall()
                for row in rows :
                    self.addAuthor(*(row[0:]))   
            if ~type_ejector.isspace() and type_ejector!= '':                               
                sql = """WITH d AS (SELECT ac.id
                            FROM account ac
                            LEFT JOIN user_right ur ON ac.id = ur.id_account
                            LEFT JOIN type_ejector te ON te.id = ur.id_type_sensor
                            WHERE te.ref = %s or ur.role = 'manager')
                            SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                            FROM account ac 
                            LEFT JOIN d ON ac.id = d.id
                            WHERE d.id IS NULL;
                """
                self.cur.execute(sql, (type_ejector, ))
                self.conn.commit()

                rows = self.cur.fetchall()
                
                self.model_other.removeRows(0, self.model_other.rowCount())

                for row in rows :
                    self.addOther(*(row[0:])) 
                
                self.model_author.removeRows(0, self.model_author.rowCount())
                sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                            FROM account ac
                            JOIN user_right ur ON ac.id = ur.id_account
                            JOIN type_ejector te ON te.id = ur.id_type_sensor
                            WHERE te.ref = %s;
                """
                self.cur.execute(sql, (type_ejector, ))
                self.conn.commit()

                rows = self.cur.fetchall()
                for row in rows :
                    self.addAuthor(*(row[0:]))
            if ~type_camera.isspace() and type_camera!= '':           
                sql = """WITH d AS (SELECT ac.id
                            FROM account ac
                            LEFT JOIN user_right ur ON ac.id = ur.id_account
                            LEFT JOIN type_camera tc ON tc.id = ur.id_type_sensor
                            WHERE tc.ref = %s)
                            SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                            FROM account ac 
                            LEFT JOIN d ON ac.id = d.id
                            WHERE d.id IS NULL;
                """
                self.cur.execute(sql, (type_camera, ))
                self.conn.commit()

                rows = self.cur.fetchall()
                
                self.model_other.removeRows(0, self.model_other.rowCount())

                for row in rows :
                    self.addOther(*(row[0:])) 
                
                self.model_author.removeRows(0, self.model_author.rowCount())
                sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                            FROM account ac
                            JOIN user_right ur ON ac.id = ur.id_account
                            JOIN type_camera tc ON tc.id = ur.id_type_sensor
                            WHERE tc.ref = %s;
                """
                self.cur.execute(sql, (type_camera, ))
                self.conn.commit()

                rows = self.cur.fetchall()
                for row in rows :
                    self.addAuthor(*(row[0:]))           
            if ~type_test_point.isspace() and type_test_point!= '':                       
                sql = """WITH d AS (SELECT ac.id
                            FROM account ac
                            LEFT JOIN user_right ur ON ac.id = ur.id_account
                            LEFT JOIN type_test_point ttp ON ttp.id = ur.id_type_sensor
                            WHERE ttp.ref = %s)
                            SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                            FROM account ac 
                            LEFT JOIN d ON ac.id = d.id
                            WHERE d.id IS NULL;
                """
                self.cur.execute(sql, (type_test_point, ))
                self.conn.commit()

                rows = self.cur.fetchall()
                
                self.model_other.removeRows(0, self.model_other.rowCount())

                for row in rows :
                    self.addOther(*(row[0:])) 
                
                self.model_author.removeRows(0, self.model_author.rowCount())
                sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                            FROM account ac
                            JOIN user_right ur ON ac.id = ur.id_account
                            JOIN type_test_point ttp ON ttp.id = ur.id_type_sensor
                            WHERE ttp.ref = %s;
                """
                self.cur.execute(sql, (type_test_point, ))
                self.conn.commit()

                rows = self.cur.fetchall()
                for row in rows :
                    self.addAuthor(*(row[0:]))
            if ~type_intrinsic_value.isspace() and type_intrinsic_value!= '':
                sql = """WITH d AS (SELECT ac.id
                            FROM account ac
                            LEFT JOIN user_right ur ON ac.id = ur.id_account
                            LEFT JOIN type_intricsic_value tiv ON tiv.id = ur.id_type_sensor
                            WHERE tiv.ref = %s)
                            SELECT ac.fname, ac.lname, ac.orga, ac.tel, ac.uname
                            FROM account ac 
                            LEFT JOIN d ON ac.id = d.id
                            WHERE d.id IS NULL;
                """
                self.cur.execute(sql, (type_intrinsic_value, ))
                self.conn.commit()

                rows = self.cur.fetchall()
                
                self.model_other.removeRows(0, self.model_other.rowCount())

                for row in rows :
                    self.addOther(*(row[0:])) 
                
                self.model_author.removeRows(0, self.model_author.rowCount())
                sql = """SELECT ac.fname, ac.lname, ac.orga, ac.tel, ur.role, ac.uname
                            FROM account ac
                            JOIN user_right ur ON ac.id = ur.id_account
                            JOIN type_intricsic_value tiv ON tiv.id = ur.id_type_sensor
                            WHERE tiv.ref = %s;
                """
                self.cur.execute(sql, (type_intrinsic_value, ))
                self.conn.commit()

                rows = self.cur.fetchall()
                for row in rows :
                    self.addAuthor(*(row[0:]))

    def transfer(self) :
        if (self.tabs.currentIndex() == 0) :
            sql = """INSERT INTO account(uname, orga, fname, lname, tel, email, password) VALUES (%s, %s, %s, %s, %s , %s, CRYPT(%s, gen_salt('bf', 8)));"""
            sql_del = """DELETE FROM account WHERE uname = %s;"""
            sql_update = """UPDATE account
                               SET password = CRYPT(%s, gen_salt('bf', 8))
                               WHERE uname = %s;"""
            try :                   
                for i in self.list_user_create :
                    self.cur.execute(sql, (i.uname, i.orga, i.fname, i.lname, i.tel, i.email, i.password))
                    print('created user')
                    print(i.uname)
                    self.conn.commit()
                for i in self.list_user_delete :
                    self.cur.execute(sql_del, (i.uname,))
                    print('deleted user')
                    print(i.uname)
                    self.conn.commit()
                for i in self.list_user_update :
                    self.cur.execute(sql_update, (i.password, i.uname))
                    print('updated user')
                    print(i.uname)
                    self.conn.commit()
            except :
                print('fail')
                self.conn.rollback()
            self.init_user()
        if (self.tabs.currentIndex() == 1) :
            try :
                test_mean_type = self.test_mean_type.currentText()
                test_mean_name = self.test_mean_name.currentText()
                test_mean_num = self.test_mean_num.currentText()

                type_coating = self.coating_type.currentText()

                type_detergent = self.detergent_type.currentText()

                insect = 't' if self.insect.currentText() == 'Yes' else 'f'

                acquisition = 't' if self.acquisition.currentText() == 'Yes' else 'f'

                type_tank = self.tank_type.currentText()

                type_sensor = self.sensor_type.currentText()

                type_ejector = self.ejector_type.currentText()

                type_camera = self.camera_type.currentText()

                type_test_point = self.test_point_type.currentText()

                type_intrinsic_value = self.intrinsic_value_type.currentText()

                if  (~test_mean_type.isspace() and test_mean_type != '') and  (~test_mean_name.isspace() and test_mean_name != '')  and  (~test_mean_num.isspace() and test_mean_num != '') :   
                    sql = """SELECT * FROM test_mean WHERE type = %s AND name = %s AND number = %s;""" 
                    self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    if len(rows) != 1 :
                        if 'manager' in [i[0] for i in self.lst] :  
                            sql = """INSERT INTO test_mean(type, name, number) VALUES (%s, %s, %s);"""
                            self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num))
                            self.conn.commit()
                        else :
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)
                            msg.setText("You are not allowed to do this")
                            msg.setWindowTitle("Validate Fail")
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.exec_()
                            return
                    for i in range(self.model_author.rowCount()) :
                        uname = self.model_author.data(self.model_author.index(i, 5))
                        right = self.model_author.data(self.model_author.index(i, 4))
                        sql = """SELECT * FROM user_right ur JOIN account ac ON ac.id = ur.id_account JOIN test_mean tm ON tm.id = ur.id_test_mean WHERE ac.uname = %s AND tm.type = %s AND tm.name = %s AND tm.number = %s;"""
                        self.cur.execute(sql, (uname, test_mean_type, test_mean_name, test_mean_num))
                        self.conn.commit()            
                        d = self.cur.fetchall()
                        if (len(d) == 1) :
                            sql = """UPDATE user_right ur
                                     SET role = %s
                                     WHERE ur.id_account = (SELECT id FROM account WHERE uname = %s) AND ur.id_test_mean = (SELECT tm.id FROM test_mean tm WHERE tm.type = %s AND tm.name = %s AND tm.number = %s);"""
                            self.cur.execute(sql, (right, uname, test_mean_type, test_mean_name, test_mean_num))
                            self.conn.commit()
                        else :
                            sql = """INSERT INTO user_right(id_account, role, id_test_mean, insect, acqui_system) VALUES ((SELECT id FROM account WHERE uname = %s), %s, (SELECT id FROM test_mean WHERE type = %s AND name = %s AND number = %s), %s, %s);"""
                            self.cur.execute(sql, (uname, right, test_mean_type, test_mean_name, test_mean_num, insect, acquisition))
                            self.conn.commit()
                    for i in range(self.model_other.rowCount()) :
                        uname = self.model_other.data(self.model_other.index(i, 4))
                        sql = """DELETE FROM user_right where id_account = (SELECT id FROM account WHERE uname = %s) AND id_test_mean = (SELECT id FROM test_mean WHERE type = %s AND name = %s AND number = %s);"""
                        self.cur.execute(sql, (uname, test_mean_type, test_mean_name, test_mean_num))
                        self.conn.commit()
                    self.test_mean_type.setCurrentText('')
                    self.test_mean_name.setCurrentText('')
                    self.test_mean_num.setCurrentText('')
                if (~type_coating.isspace() and type_coating != '') :
                    print(type_coating)
                    sql = """SELECT * FROM type_coating WHERE ref = %s;""" 
                    self.cur.execute(sql, (type_coating,))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    print(len(rows))
                    if len(rows) != 1 :
                        if 'manager' in [i[0] for i in self.lst] :
                            sql = """INSERT INTO type_coating(ref) VALUES (%s);"""
                            self.cur.execute(sql, (type_coating,))
                            self.conn.commit()
                        else :
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)
                            msg.setText("You are not allowed to do this")
                            msg.setWindowTitle("Validate Fail")
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.exec_()
                            return
                    for i in range(self.model_author.rowCount()) :
                        uname = self.model_author.data(self.model_author.index(i, 5))
                        right = self.model_author.data(self.model_author.index(i, 4))
                        sql = """SELECT * FROM user_right ur JOIN account ac ON ac.id = ur.id_account JOIN type_coating tc ON tc.id = ur.id_type_coating WHERE ac.uname = %s AND tc.ref = %s"""
                        self.cur.execute(sql, (uname, type_coating))
                        self.conn.commit()
                        d = self.cur.fetchall()
                        if (len(d) == 1) :
                            sql = """UPDATE user_right ur 
                                        SET role = %s
                                        WHERE ur.id_account = (SELECT id FROM account WHERE uname = %s) AND ur.id_type_coating = (SELECT id FROM type_coating  WHERE ref = %s);"""
                            self.cur.execute(sql, (right, uname, type_coating))
                            self.conn.commit()
                        else :
                            sql = """INSERT INTO user_right(id_account, role, id_type_coating, insect, acqui_system) VALUES ((SELECT id FROM account WHERE uname = %s), %s, (SELECT id FROM type_coating WHERE ref = %s), %s, %s);"""
                            self.cur.execute(sql, (uname, right, type_coating, insect, acquisition))
                            self.conn.commit()
                    for i in range(self.model_other.rowCount()) :
                        uname = self.model_other.data(self.model_other.index(i, 4))
                        sql = """DELETE FROM user_right where id_account = (SELECT id FROM account WHERE uname = %s) AND id_type_coating = (SELECT id FROM type_coating WHERE ref = %s);"""
                        self.cur.execute(sql, (uname, type_coating))
                        self.conn.commit()
                    self.coating_type.setCurrentText('')
                if (~type_detergent.isspace() and type_detergent != '') :
                    sql = """SELECT * FROM type_detergent WHERE ref = %s;""" 
                    self.cur.execute(sql, (type_detergent,))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    if len(rows) != 1 :
                        if 'manager' in [i[0] for i in self.lst] :
                            sql = """INSERT INTO type_detergent(ref) VALUES (%s);"""
                            self.cur.execute(sql, (type_detergent,))
                            self.conn.commit()
                        else :
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)
                            msg.setText("You are not allowed to do this")
                            msg.setWindowTitle("Validate Fail")
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.exec_()
                            return
                    for i in range(self.model_author.rowCount()) :
                        uname = self.model_author.data(self.model_author.index(i, 5))
                        right = self.model_author.data(self.model_author.index(i, 4))
                        sql = """SELECT * FROM user_right ur JOIN account ac ON ac.id = ur.id_account JOIN type_detergent tc ON tc.id = ur.id_type_detergent WHERE ac.uname = %s AND tc.ref = %s"""
                        self.cur.execute(sql, (uname, type_detergent))
                        self.conn.commit()
                        d = self.cur.fetchall()
                        if (len(d) == 1) :
                            sql = """UPDATE user_right ur
                                        SET role = %s
                                        WHERE ur.id_account = (SELECT id FROM account WHERE uname = %s) AND ur.id_type_detergent = (SELECT id FROM type_detergent  WHERE ref = %s);"""
                            self.cur.execute(sql, (right, uname, type_detergent))
                            self.conn.commit()
                        else :
                            sql = """INSERT INTO user_right(id_account, role, id_type_detergent, insect, acqui_system) VALUES ((SELECT id FROM account WHERE uname = %s), %s, (SELECT id FROM type_detergent WHERE ref = %s), %s, %s);"""
                            self.cur.execute(sql, (uname, right, type_detergent, insect, acquisition))
                            self.conn.commit()
                    for i in range(self.model_other.rowCount()) :
                        uname = self.model_other.data(self.model_other.index(i, 4))
                        sql = """DELETE FROM user_right where id_account = (SELECT id FROM account WHERE uname = %s) AND id_type_detergent = (SELECT id FROM type_detergent WHERE ref = %s);"""
                        self.cur.execute(sql, (uname, type_detergent))
                        self.conn.commit()
                    self.detergent_type.setCurrentText('')
                if (~type_tank.isspace() and type_tank != '') :
                    sql = """SELECT * FROM type_tank WHERE ref = %s;""" 
                    self.cur.execute(sql, (type_tank,))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    if len(rows) != 1 :
                        if 'manager' in [i[0] for i in self.lst] :
                            sql = """INSERT INTO type_tank(ref) VALUES (%s);"""
                            self.cur.execute(sql, (type_tank,))
                            self.conn.commit()
                        else :
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)
                            msg.setText("You are not allowed to do this")
                            msg.setWindowTitle("Validate Fail")
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.exec_()
                            return
                    for i in range(self.model_author.rowCount()) :
                        uname = self.model_author.data(self.model_author.index(i, 5))
                        right = self.model_author.data(self.model_author.index(i, 4))
                        sql = """SELECT * FROM user_right ur JOIN account ac ON ac.id = ur.id_account JOIN type_tank tc ON tc.id = ur.id_type_tank WHERE ac.uname = %s AND tc.ref = %s"""
                        self.cur.execute(sql, (uname, type_tank))
                        self.conn.commit()
                        d = self.cur.fetchall()
                        if (len(d) == 1) :
                            sql = """UPDATE user_right ur
                                        SET role = %s
                                        WHERE ur.id_account = (SELECT id FROM account WHERE uname = %s) AND ur.id_type_tank = (SELECT id FROM type_tank  WHERE ref = %s);"""
                            self.cur.execute(sql, (right, uname, type_tank))
                            self.conn.commit()
                        else :
                            sql = """INSERT INTO user_right(id_account, role, id_type_tank, insect, acqui_system) VALUES ((SELECT id FROM account WHERE uname = %s), %s, (SELECT id FROM type_tank WHERE ref = %s), %s, %s);"""
                            self.cur.execute(sql, (uname, right, type_tank, insect, acquisition))
                            self.conn.commit()
                    for i in range(self.model_other.rowCount()) :
                        uname = self.model_other.data(self.model_other.index(i, 4))
                        sql = """DELETE FROM user_right where id_account = (SELECT id FROM account WHERE uname = %s) AND id_type_tank = (SELECT id FROM type_tank WHERE ref = %s);"""
                        self.cur.execute(sql, (uname, type_tank))
                        self.conn.commit()
                    self.tank_type.setCurrentText('')
                if (~type_sensor.isspace() and type_sensor != '') :
                    sql = """SELECT * FROM type_sensor WHERE ref = %s;""" 
                    self.cur.execute(sql, (type_sensor,))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    if len(rows) != 1 :
                        if 'manager' in [i[0] for i in self.lst] :
                            sql = """INSERT INTO type_sensor(ref) VALUES (%s);"""
                            self.cur.execute(sql, (type_sensor,))
                            self.conn.commit()
                        else :
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)
                            msg.setText("You are not allowed to do this")
                            msg.setWindowTitle("Validate Fail")
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.exec_()
                            return
                    for i in range(self.model_author.rowCount()) :
                        uname = self.model_author.data(self.model_author.index(i, 5))
                        right = self.model_author.data(self.model_author.index(i, 4))
                        sql = """SELECT * FROM user_right ur JOIN account ac ON ac.id = ur.id_account JOIN type_sensor tc ON tc.id = ur.id_type_sensor WHERE ac.uname = %s AND tc.ref = %s"""
                        self.cur.execute(sql, (uname, type_sensor))
                        self.conn.commit()
                        d = self.cur.fetchall()
                        if (len(d) == 1) :
                            sql = """UPDATE user_right ur
                                        SET role = %s
                                        WHERE ur.id_account = (SELECT id FROM account WHERE uname = %s) AND ur.id_type_sensor = (SELECT id FROM type_sensor  WHERE ref = %s);"""
                            self.cur.execute(sql, (right, uname, type_sensor))
                            self.conn.commit()
                        else :
                            sql = """INSERT INTO user_right(id_account, role, id_type_sensor, insect, acqui_system) VALUES ((SELECT id FROM account WHERE uname = %s), %s, (SELECT id FROM type_sensor WHERE ref = %s), %s, %s);"""
                            self.cur.execute(sql, (uname, right, type_sensor, insect, acquisition))
                            self.conn.commit()
                    for i in range(self.model_other.rowCount()) :
                        uname = self.model_other.data(self.model_other.index(i, 4))
                        sql = """DELETE FROM user_right where id_account = (SELECT id FROM account WHERE uname = %s) AND id_type_sensor = (SELECT id FROM type_sensor WHERE ref = %s);"""
                        self.cur.execute(sql, (uname, type_sensor))
                        self.conn.commit()
                    self.sensor_type.setCurrentText('')

                if (~type_ejector.isspace() and type_ejector != '') :
                    sql = """SELECT * FROM type_ejector WHERE ref = %s;""" 
                    self.cur.execute(sql, (type_ejector,))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    if len(rows) != 1 :
                        if 'manager' in [i[0] for i in self.lst] :
                            sql = """INSERT INTO type_ejector(ref) VALUES (%s);"""
                            self.cur.execute(sql, (type_ejector,))
                            self.conn.commit()
                        else :
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)
                            msg.setText("You are not allowed to do this")
                            msg.setWindowTitle("Validate Fail")
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.exec_()
                            return
                    for i in range(self.model_author.rowCount()) :
                        uname = self.model_author.data(self.model_author.index(i, 5))
                        right = self.model_author.data(self.model_author.index(i, 4))
                        sql = """SELECT * FROM user_right ur JOIN account ac ON ac.id = ur.id_account JOIN type_ejector tc ON tc.id = ur.id_type_ejector WHERE ac.uname = %s AND tc.ref = %s"""
                        self.cur.execute(sql, (uname, type_ejector))
                        self.conn.commit()
                        d = self.cur.fetchall()
                        if (len(d) == 1) :
                            sql = """UPDATE user_right ur
                                        SET role = %s
                                        WHERE ur.id_account = (SELECT id FROM account WHERE uname = %s) AND ur.id_type_ejector = (SELECT id FROM type_ejector  WHERE ref = %s);"""
                            self.cur.execute(sql, (right, uname, type_ejector))
                            self.conn.commit()
                        else :
                            sql = """INSERT INTO user_right(id_account, role, id_type_ejector, insect, acqui_system) VALUES ((SELECT id FROM account WHERE uname = %s), %s, (SELECT id FROM type_ejector WHERE ref = %s), %s, %s);"""
                            self.cur.execute(sql, (uname, right, type_ejector, insect, acquisition))
                            self.conn.commit()
                    for i in range(self.model_other.rowCount()) :
                        uname = self.model_other.data(self.model_other.index(i, 4))
                        sql = """DELETE FROM user_right where id_account = (SELECT id FROM account WHERE uname = %s) AND id_type_ejector = (SELECT id FROM type_ejector WHERE ref = %s);"""
                        self.cur.execute(sql, (uname, type_ejector))
                        self.conn.commit()
                    self.ejector_type.setCurrentText('')

                if (~type_camera.isspace() and type_camera != '') :
                    sql = """SELECT * FROM type_camera WHERE ref = %s;""" 
                    self.cur.execute(sql, (type_camera,))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    if len(rows) != 1 :
                        if 'manager' in [i[0] for i in self.lst] :
                            sql = """INSERT INTO type_camera(ref) VALUES (%s);"""
                            self.cur.execute(sql, (type_camera,))
                            self.conn.commit()
                        else :
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)
                            msg.setText("You are not allowed to do this")
                            msg.setWindowTitle("Validate Fail")
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.exec_()
                            return
                    for i in range(self.model_author.rowCount()) :
                        uname = self.model_author.data(self.model_author.index(i, 5))
                        right = self.model_author.data(self.model_author.index(i, 4))
                        sql = """SELECT * FROM user_right ur JOIN account ac ON ac.id = ur.id_account JOIN type_camera tc ON tc.id = ur.id_type_camera WHERE ac.uname = %s AND tc.ref = %s"""
                        self.cur.execute(sql, (uname, type_camera))
                        self.conn.commit()
                        d = self.cur.fetchall()
                        if (len(d) == 1) :
                            sql = """UPDATE user_right ur
                                        SET role = %s
                                        WHERE ur.id_account = (SELECT id FROM account WHERE uname = %s) AND ur.id_type_camera = (SELECT id FROM type_camera  WHERE ref = %s);"""
                            self.cur.execute(sql, (right, uname, type_camera))
                            self.conn.commit()
                        else :
                            sql = """INSERT INTO user_right(id_account, role, id_type_camera, insect, acqui_system) VALUES ((SELECT id FROM account WHERE uname = %s), %s, (SELECT id FROM type_camera WHERE ref = %s), %s, %s);"""
                            self.cur.execute(sql, (uname, right, type_camera, insect, acquisition))
                            self.conn.commit()
                    for i in range(self.model_other.rowCount()) :
                        uname = self.model_other.data(self.model_other.index(i, 4))
                        sql = """DELETE FROM user_right where id_account = (SELECT id FROM account WHERE uname = %s) AND id_type_camera = (SELECT id FROM type_camera WHERE ref = %s);"""
                        self.cur.execute(sql, (uname, type_camera))
                        self.conn.commit()
                    self.camera_type.setCurrentText('')
                if (~type_test_point.isspace() and type_test_point != '') :
                    sql = """SELECT * FROM type_test_point WHERE ref = %s;""" 
                    self.cur.execute(sql, (type_test_point,))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    if len(rows) != 1 :
                        if 'manager' in [i[0] for i in self.lst] :
                            sql = """INSERT INTO type_test_point(ref) VALUES (%s);"""
                            self.cur.execute(sql, (type_test_point,))
                            self.conn.commit()
                        else :
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)
                            msg.setText("You are not allowed to do this")
                            msg.setWindowTitle("Validate Fail")
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.exec_()
                            return
                    for i in range(self.model_author.rowCount()) :
                        uname = self.model_author.data(self.model_author.index(i, 5))
                        right = self.model_author.data(self.model_author.index(i, 4))
                        sql = """SELECT * FROM user_right ur JOIN account ac ON ac.id = ur.id_account JOIN type_test_point tc ON tc.id = ur.id_type_test_point WHERE ac.uname = %s AND tc.ref = %s"""
                        self.cur.execute(sql, (uname, type_test_point))
                        self.conn.commit()
                        d = self.cur.fetchall()
                        if (len(d) == 1) :
                            sql = """UPDATE user_right ur
                                        SET role = %s
                                        WHERE ur.id_account = (SELECT id FROM account WHERE uname = %s) AND ur.id_type_test_point = (SELECT id FROM type_test_point  WHERE ref = %s);"""
                            self.cur.execute(sql, (right, uname, type_test_point))
                            self.conn.commit()
                        else :
                            sql = """INSERT INTO user_right(id_account, role, id_type_test_point, insect, acqui_system) VALUES ((SELECT id FROM account WHERE uname = %s), %s, (SELECT id FROM type_test_point WHERE ref = %s), %s, %s);"""
                            self.cur.execute(sql, (uname, right, type_test_point, insect, acquisition))
                            self.conn.commit()
                    for i in range(self.model_other.rowCount()) :
                        uname = self.model_other.data(self.model_other.index(i, 4))
                        sql = """DELETE FROM user_right where id_account = (SELECT id FROM account WHERE uname = %s) AND id_type_test_point = (SELECT id FROM type_test_point WHERE ref = %s);"""
                        self.cur.execute(sql, (uname, type_test_point))
                        self.conn.commit()
                    self.test_point_type.setCurrentText('')
                if (~type_intrinsic_value.isspace() and type_intrinsic_value != '') :
                    sql = """SELECT * FROM type_intrinsic_value WHERE ref = %s;""" 
                    self.cur.execute(sql, (type_intrinsic_value,))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    if len(rows) != 1 :
                        if 'manager' in [i[0] for i in self.lst] :
                            sql = """INSERT INTO type_intrinsic_value(ref) VALUES (%s);"""
                            self.cur.execute(sql, (type_intrinsic_value,))
                            self.conn.commit()
                        else :
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)
                            msg.setText("You are not allowed to do this")
                            msg.setWindowTitle("Validate Fail")
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.exec_()
                            return
                    for i in range(self.model_author.rowCount()) :
                        uname = self.model_author.data(self.model_author.index(i, 5))
                        right = self.model_author.data(self.model_author.index(i, 4))
                        sql = """SELECT * FROM user_right ur JOIN account ac ON ac.id = ur.id_account JOIN type_intrinsic_value tc ON tc.id = ur.id_type_intrinsic_value WHERE ac.uname = %s AND tc.ref = %s"""
                        self.cur.execute(sql, (uname, type_intrinsic_value))
                        self.conn.commit()
                        d = self.cur.fetchall()
                        if (len(d) == 1) :
                            sql = """UPDATE user_right ur
                                        SET role = %s
                                        WHERE ur.id_account = (SELECT id FROM account WHERE uname = %s) AND ur.id_type_intrinsic_value = (SELECT id FROM type_intrinsic_value  WHERE ref = %s);"""
                            self.cur.execute(sql, (right, uname, type_intrinsic_value))
                            self.conn.commit()
                        else :
                            sql = """INSERT INTO user_right(id_account, role, id_type_intrinsic_value, insect, acqui_system) VALUES ((SELECT id FROM account WHERE uname = %s), %s, (SELECT id FROM type_intrinsic_value WHERE ref = %s), %s, %s);"""
                            self.cur.execute(sql, (uname, right, type_intrinsic_value, insect, acquisition))
                            self.conn.commit()
                    for i in range(self.model_other.rowCount()) :
                        uname = self.model_other.data(self.model_other.index(i, 4))
                        sql = """DELETE FROM user_right where id_account = (SELECT id FROM account WHERE uname = %s) AND id_type_intrinsic_value = (SELECT id FROM type_intrinsic_value WHERE ref = %s);"""
                        self.cur.execute(sql, (uname, type_intrinsic_value))
                        self.conn.commit()
                    self.intrinsic_value_type.setCurrentText('')
            except :
                self.conn.rollback()
                print('fail')
            try :
                self.model_admin.removeRows(0, self.model_admin.rowCount())
                sql = """SELECT ac.orga, ac.fname, ac.lname, (CASE 
                                WHEN ur.id_test_mean IS NOT NULL THEN CONCAT(tm.name, '_', tm.number)
                                WHEN ur.id_type_coating IS NOT NULL THEN tc.ref
                                WHEN ur.id_type_detergent IS NOT NULL THEN td.ref
                                WHEN ur.id_type_tank IS NOT NULL THEN tt.ref
                                WHEN ur.id_type_sensor IS NOT NULL THEN ts.ref
                                WHEN ur.id_type_ejector IS NOT NULL THEN te.ref
                                WHEN ur.id_type_camera IS NOT NULL THEN tca.ref
                                WHEN ur.id_type_test_point IS NOT NULL THEN ttp.ref
                                WHEN id_type_intrinsic_value IS NOT NULL THEN tiv.ref END) AS object, ac.uname
                    FROM account ac
                    JOIN user_right ur ON ac.id = ur.id_account
                    LEFT JOIN test_mean tm ON tm.id = ur.id_test_mean
                    LEFT JOIN type_coating tc ON tc.id = ur.id_type_coating
                    LEFT JOIN type_detergent td ON td.id = ur.id_type_detergent
                    LEFT JOIN type_tank tt ON tt.id = ur.id_type_tank
                    LEFT JOIN type_sensor ts ON ts.id = ur.id_type_sensor
                    LEFT JOIN type_ejector te ON te.id = ur.id_type_ejector
                    LEFT JOIN type_camera tca ON tca.id = ur.id_type_camera
                    LEFT JOIN type_test_point ttp ON ttp.id = ur.id_type_test_point
                    LEFT JOIN type_intrinsic_value tiv ON tiv.id = ur.id_type_intrinsic_value
                    
                    WHERE LOWER(ur.role) = 'admin' 
                """
                self.cur.execute(sql)
                self.conn.commit()
                rows = self.cur.fetchall()
                for row in rows :
                    self.addAdmin(*(row[0:]))
                    self.conn.commit()
                self.model_other.removeRows(0, self.model_other.rowCount())
                self.model_author.removeRows(0, self.model_author.rowCount())
            except :
                print('error')

            try : 
                sql = """SELECT ur.role, CASE WHEN ur.id_test_mean IS NOT NULL THEN CONCAT('test mean' ,'-', tm.type, '_', tm.name, '_', tm.number)
                                                  WHEN ur.id_type_coating IS NOT NULL THEN CONCAT('coating', '-', tc.ref)
                                                  WHEN ur.id_type_detergent IS NOT NULL THEN CONCAT('detergent', '-', td.ref)
                                                  WHEN ur.id_type_tank IS NOT NULL THEN CONCAT('tank', '-', tt.ref)
                                                  WHEN ur.id_type_sensor IS NOT NULL THEN CONCAT('sensor', '-',ts.ref)
                                                  WHEN ur.id_type_ejector IS NOT NULL THEN CONCAT('ejector', '-',te.ref)
                                                  WHEN ur.id_type_camera IS NOT NULL THEN CONCAT('camera', '-',tca.ref)
                                                  WHEN ur.id_type_test_point IS NOT NULL THEN CONCAT('test point', '-',ttp.ref)
                                                  WHEN id_type_intrinsic_value IS NOT NULL THEN CONCAT('intrinsic value', '-',tiv.ref) END AS object
                             FROM account ac
                             JOIN user_right ur ON ur.id_account = ac.id
                             LEFT JOIN test_mean tm ON tm.id = ur.id_test_mean
                             LEFT JOIN type_coating tc ON tc.id = ur.id_type_coating
                             LEFT JOIN type_detergent td ON td.id = ur.id_type_detergent
                             LEFT JOIN type_tank tt ON tt.id = ur.id_type_tank
                             LEFT JOIN type_sensor ts ON ts.id = ur.id_type_sensor
                             LEFT JOIN type_ejector te ON te.id = ur.id_type_ejector
                             LEFT JOIN type_camera tca ON tca.id = ur.id_type_camera
                             LEFT JOIN type_test_point ttp ON ttp.id = ur.id_type_test_point
                             LEFT JOIN type_intrinsic_value tiv ON tiv.id = ur.id_type_intrinsic_value
                             WHERE ac.uname = %s ;
                        """
                self.cur.execute(sql, (self.uname_user,))
                self.conn.commit()
                rows = self.cur.fetchall()
                self.lst = []
                for row in rows :
                    l = [row[0]]
                    if row[1] is not None :
                        for i in row[1].split('-') :
                            l.append(i)
                    self.lst.append(l)
            except :
                print('fail to fail')
            
            try : 
                sql = """SELECT DISTINCT type
                         FROM test_mean;
                """
                self.cur.execute(sql)
                self.conn.commit()
                rows = self.cur.fetchall()
                test_mean_type = []
                for row in rows :
                    test_mean_type.append(row[0])
                self.test_mean_type.clear()
                self.test_mean_type.addItems(test_mean_type)
                self.test_mean_type.setCurrentText('')
            except :
                print('can\'t')
    def init_user(self) :
        list_user = listUser()
        self.list_user_create = deepcopy(list_user)
        self.list_user_delete = deepcopy(list_user)
        self.list_user_current = deepcopy(list_user)
        self.list_user_update = deepcopy(list_user)
        sql = """SELECT uname, fname, lname, orga, tel, email, password
                 FROM account;
        """
        self.cur.execute(sql)
        self.conn.commit()
        rows = self.cur.fetchall()
        for row in rows :
            self.list_user_current.addUser(user(*(row[0:])))

    def connect(self) :
        try :
            host = "localhost"
            username = "iventre"
            dbname = "lmsm"
            password = "lmsm"
            self.conn = psycopg2.connect(host = host, user = username, dbname = dbname, password = password)
            self.cur = self.conn.cursor()
        except psycopg2.Error as err: 
            print(str(err))
