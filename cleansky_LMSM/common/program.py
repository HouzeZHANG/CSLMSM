import cleansky_LMSM.common.database as database
import cleansky_LMSM.common.controller as controller
import cleansky_LMSM.common.person as person
import logging


class Program:
    def __init__(self, db_object=database.PostgreDB(host='localhost', database='testdb',
                                                    user='dbuser', pd=123456, port='5432')):
        # logging.basicConfig(filename='program.log', level=logging.DEBUG)
        self.my_controller = None
        self.db_object = db_object
        self.db_object.connect()
        self.role = None
        self.run_login()

    def run_login(self):
        # 重置身份
        self.role = person.Person()
        self.my_controller = controller.LoginController(db_object=self.db_object,
                                                        my_program=self)
        self.my_controller.run_view()

    def run_menu(self, obj=None):
        # 更新program对象中的person对象
        # del obj
        self.my_controller = controller.MenuController(db_object=self.db_object,
                                                       my_program=self)
        self.my_controller.run_view()

    def run_management(self):
        self.my_controller = controller.ManagementController(db_object=self.db_object,
                                                             my_program=self)
        self.my_controller.run_view()

    def run_items_to_be_tested(self):
        self.my_controller = controller.ItemsToBeTestedController(db_object=self.db_object,
                                                                  my_program=self)
        self.my_controller.run_view()

    def run_list_of_test_items(self):
        self.my_controller = controller.ListOfTestMeansController(db_object=self.db_object,
                                                                  my_program=self)
        self.my_controller.run_view()

    def run_test_execution(self):
        self.my_controller = controller.TestExecutionController(db_object=self.db_object,
                                                                my_program=self)
        self.my_controller.run_view()
