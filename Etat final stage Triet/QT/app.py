import sys
sys.path.append('..\\QT\\form')
import manager
from manager import *
import login
from login import *
import stack
from stack import *

# class App(QMainWindow) :
#     def __init__(self) :
#         super().__init__()
#         self.setGeometry(250, 100, 900, 600)
#         self.startLogin()    
#     def startLogin(self) :
#         self.login = login(self)
#         self.setWindowTitle('Login Form')
#         self.setCentralWidget(self.login)
#         self.login.login_btn.installEventFilter(self)
#         self.show()
#     def startManager(self) :
#         self.Manager = Manager(self, self.uname, self.lst)
#         self.setWindowTitle('Management')
#         self.setCentralWidget(self.Manager)
#         self.Manager.installEventFilter(self)
#         self.show()
#     def eventFilter(self, obj, event) :
#         if obj == self.login.login_btn :
#             if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton : 
#                 uname = self.login.username.text()
#                 password = self.login.password.text()
#                 sql = """SELECT uname, password FROM account WHERE uname = %s AND password = CRYPT(%s, password);"""
#                 self.login.cur.execute(sql, (uname, password))
#                 self.login.conn.commit()
#                 rows = self.login.cur.fetchall()
#                 if len(rows) == 1 :
#                     sql = """SELECT ur.role, CASE WHEN ur.id_test_mean IS NOT NULL THEN CONCAT('test mean' ,'-', tm.type, '_', tm.name, '_', tm.number)
#                                                   WHEN ur.id_type_coating IS NOT NULL THEN CONCAT('coating', '-', tc.ref)
#                                                   WHEN ur.id_type_detergent IS NOT NULL THEN CONCAT('detergent', '-', td.ref)
#                                                   WHEN ur.id_type_tank IS NOT NULL THEN CONCAT('tank', '-', tt.ref)
#                                                   WHEN ur.id_type_sensor IS NOT NULL THEN CONCAT('sensor', '-',ts.ref)
#                                                   WHEN ur.id_type_ejector IS NOT NULL THEN CONCAT('ejector', '-',te.ref)
#                                                   WHEN ur.id_type_camera IS NOT NULL THEN CONCAT('camera', '-',tca.ref)
#                                                   WHEN ur.id_type_test_point IS NOT NULL THEN CONCAT('test point', '-',ttp.ref)
#                                                   WHEN id_type_intrinsic_value IS NOT NULL THEN CONCAT('intrinsic value', '-',tiv.ref) END AS object
#                              FROM account ac
#                              JOIN user_right ur ON ur.id_account = ac.id
#                              LEFT JOIN test_mean tm ON tm.id = ur.id_test_mean
#                              LEFT JOIN type_coating tc ON tc.id = ur.id_type_coating
#                              LEFT JOIN type_detergent td ON td.id = ur.id_type_detergent
#                              LEFT JOIN type_tank tt ON tt.id = ur.id_type_tank
#                              LEFT JOIN type_sensor ts ON ts.id = ur.id_type_sensor
#                              LEFT JOIN type_ejector te ON te.id = ur.id_type_ejector
#                              LEFT JOIN type_camera tca ON tca.id = ur.id_type_camera
#                              LEFT JOIN type_test_point ttp ON ttp.id = ur.id_type_test_point
#                              LEFT JOIN type_intrinsic_value tiv ON tiv.id = ur.id_type_intrinsic_value
#                              WHERE ac.uname = %s ;
#                         """
#                     self.login.cur.execute(sql, (uname,))
#                     self.login.conn.commit()
#                     rows = self.login.cur.fetchall()
#                     self.lst = []
#                     for row in rows :
#                         l = [row[0]]
#                         if row[1] is not None :
#                             for i in row[1].split('-') :
#                                 l.append(i)
#                         self.lst.append(l)
#                     self.uname = uname
#                     self.startManager()
#                 else :
#                     msg = QMessageBox()
#                     msg.setIcon(QMessageBox.Information)
#                     msg.setText("Your username or password is not correct ! \n Try again")
#                     msg.setWindowTitle("Login Fail")
#                     msg.setStandardButtons(QMessageBox.Ok)
#                     msg.exec_()
#                 return True
#             return False
#         return False
# if __name__ == "__main__" :
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())

class App(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setGeometry(150, 100, 1100, 600)
        self.startLogin()    
    def startLogin(self) :
        self.login = login(self)
        self.setWindowTitle('Login Form')
        self.setCentralWidget(self.login)
        self.login.login_btn.installEventFilter(self)
        self.show()
    def startStack(self) :
        self.stack = stack(self, self.uname, self.lst)
        self.setWindowTitle('List Working')
        self.setCentralWidget(self.stack)
        self.stack.installEventFilter(self)
        self.show()
    def eventFilter(self, obj, event) :
        if obj == self.login.login_btn :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton : 
                uname = self.login.username.text()
                password = self.login.password.text()
                sql = """SELECT uname, password FROM account WHERE uname = %s AND password = CRYPT(%s, password);"""
                self.login.cur.execute(sql, (uname, password))
                self.login.conn.commit()
                rows = self.login.cur.fetchall()
                if len(rows) == 1 :
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
                    self.login.cur.execute(sql, (uname,))
                    self.login.conn.commit()
                    rows = self.login.cur.fetchall()
                    self.lst = []
                    for row in rows :
                        l = [row[0]]
                        if row[1] is not None :
                            for i in row[1].split('-') :
                                l.append(i)
                        self.lst.append(l)
                    self.uname = uname
                    self.startStack()
                elif uname == "local" and password == "local" :
                    self.lst = []
                    self.uname = "local"
                    self.startStack()
                else :
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Your username or password is not correct ! \n Try again")
                    msg.setWindowTitle("Login Fail")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                return True
            return False
        return False


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())