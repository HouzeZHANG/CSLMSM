from abc import ABC

import cleansky_LMSM.common.database as database
import cleansky_LMSM.common.model as model
import cleansky_LMSM.common.person as person
import cleansky_LMSM.common.view as view


class Controller:
    def __init__(self, my_view, my_model, my_role=person.Visitor()):
        """default authority is LEVEL VISITOR"""
        self.__view = my_view
        self.__model = my_model
        self.__role = my_role
        self.__program = None
        self.__view.set_controller(self)
        self.__model.set_controller(self)

    def set_program(self, my_program):
        self.__program = my_program

    def get_program(self):
        return self.__program

    def get_view(self):
        return self.__view

    def get_model(self):
        return self.__model

    def get_role(self):
        """
        When our user logs in, if he switches between different GUI interfaces,
        we ensure the identity consistency by self.__person
        """
        return self.__role

    def set_role(self, new_role):
        self.__role = new_role

    def run_view(self):
        self.__view.run_view()


class LoginController(Controller):
    def __init__(self, db_object, my_role=person.Visitor()):
        super(LoginController, self).__init__(my_view=view.LoginView(),
                                              my_model=model.LoginModel(db_object=db_object))
        self.set_role(my_role)

    def action_login(self):
        """
        A method that starts with Permission usually means the start of a request
        (broadly, not just a database request) that is written to the log,
        which is implemented in the Person class

        Methods that begin with Model tend to imply an interaction between the controller and the model, where the
        controller reads the user ID and password from the GUI interface after confirming permissions to the Person
        class, and then transfers login information to the model class using the Model method
        """
        if 'permission_login' in self.get_role().__dir__():
            self.get_role().permission_login()
            temp_username = self.get_view().get_username()
            temp_password = self.get_view().get_password()
            sql_result = self.get_model().model_login(temp_username, temp_password)
            if not sql_result:
                # The user does not exist in the database
                self.get_view().login_fail()
            else:
                self.get_view().login_success()
                self.set_role(new_role=person.Visitor())
                self.get_program().run_menu(self.get_role())
        else:
            print("login permission denied")


class MenuController(Controller):
    def __init__(self, db_object, role=person.Reader()):
        super(MenuController, self).__init__(my_view=view.MenuView(), my_model=model.MenuModel(db_object=db_object))
        self.set_role(role)

    def action_open_management(self):
        if 'permission_open_management' in self.get_role().__dir__():
            pass
        pass


class ManagementController(Controller):
    def __init__(self, db_object, role=person.Reader()):
        super(ManagementController, self).__init__(my_view=view.ManagementView(),
                                                   my_model=model.ManagementModel(db_object=db_object))
        self.set_role(role)

    def action_fill_orga(self):
        if 'permission_get_orga' in self.get_role().__dir__():
            self.get_role().permission_get_orga()
            sql_result = self.get_model().model_get_orga()
            print(sql_result)
        else:
            print("get_orga permission denied")


if __name__ == '__main__':
    unittest_db = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
    unittest_db.connect()

    vi = MenuController(db_object=unittest_db)
    vi.run_view()