from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import psycopg2
import sys

import manager, test_mean_modify, tank_modify, coating_modify, detergent_modify
from manager import *
from test_mean_modify import *
from tank_modify import *
from coating_modify import *
from detergent_modify import *
class stack(QWidget) :
    def __init__(self, parent, uname, lst):
        super(stack, self).__init__(parent)
        self.connect()
        self.uname = uname
        self.lst = lst
        self.leftlist = QListWidget(self)
        self.leftlist.insertItem (0, 'Manager' )
        self.leftlist.insertItem (1, 'Create/Modify a test means (Aircraft/Windtunnel)' )
        self.leftlist.insertItem (2, 'Create/Modify tank' )
        self.leftlist.insertItem (3, 'Create a Coating')
        self.leftlist.insertItem (4, 'Create a Detergent')

        self.Manager = Manager(self, uname, lst)
        self.testMean = testMean(self, uname, lst)
        self.Tank = Tank(self, uname, lst)
        self.Coating = Coating(self, uname, lst)
        self.Detergent = Detergent(self, uname, lst)

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.Manager)
        self.Stack.addWidget(self.testMean)
        self.Stack.addWidget(self.Tank)
        self.Stack.addWidget(self.Coating)   
        self.Stack.addWidget(self.Detergent)

        self.leftlist.setGeometry(0, 0, 200, 600)
        self.Stack.setGeometry(200, 0, 900, 600)

        self.leftlist.currentRowChanged.connect(self.display)
        
        self.Manager.transfer_btn_2.clicked.connect(self.repaint)
            
    def display(self,i):
        self.Stack.setCurrentIndex(i)
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
        self.cur.execute(sql, (self.uname,))
        self.conn.commit()
        rows = self.cur.fetchall()
        self.lst = []
        for row in rows :
            l = [row[0]]
            if row[1] is not None :
                for i in row[1].split('-') :
                    l.append(i)
            self.lst.append(l)
        self.Manager = Manager(self, self.uname, self.lst)
        self.testMean = testMean(self, self.uname, self.lst)
        self.Tank = Tank(self, self.uname, self.lst)
        self.Coating = Coating(self, self.uname, self.lst)
        self.Detergent = Detergent(self, self.uname, self.lst)
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