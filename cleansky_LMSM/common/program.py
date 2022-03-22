import cleansky_LMSM.common.database as database
import cleansky_LMSM.common.controller as controller
import cleansky_LMSM.common.person as person


class Program:
    def __init__(self, db_object=database.PostgreDB(host='localhost', database='testdb',
                                                    user='dbuser', pd=123456, port='5432')):
        self.db_object = db_object
        self.db_object.connect()
        self.role = person.Person()
        self.my_controller = controller.LoginController(db_object=self.db_object,
                                                        my_role=self.role,
                                                        my_program=self)
        self.my_controller.run_view()

    def run_menu(self, role):
        # 更新program对象中的person对象
        self.role = role
        self.my_controller = controller.MenuController(db_object=self.db_object,
                                                       my_role=self.role,
                                                       my_program=self)
        self.my_controller.run_view()

    def run_management(self):
        self.my_controller = controller.ManagementController(db_object=self.db_object,
                                                             role=self.role,
                                                             my_program=self)
        self.my_controller.run_view()
