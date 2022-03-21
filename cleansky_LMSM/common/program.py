import cleansky_LMSM.common.database as database
import cleansky_LMSM.common.controller as controller
import cleansky_LMSM.common.person as person
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QLineEdit


class Program:
    def __init__(self, db_object=database.PostgreDB(host='localhost', database='testdb',
                                                    user='dbuser', pd=123456, port='5432')):
        self.db_object = db_object
        self.role = person.Visitor()
        self.my_controller = controller.LoginController(db_object=self.db_object, my_role=self.role)
        self.my_controller.set_program(self)
        self.db_object.connect()

    def run_login(self):
        self.my_controller.run_view()

    def run_menu(self, role):
        self.role = role
        self.my_controller = controller.MenuController(db_object=self.db_object, role=self.role)
        self.my_controller.run_view()

    def run_management(self):
        self.my_controller = controller.ManagementController(db_object=self.db_object, role=self.role)
        self.my_controller.run_view()
