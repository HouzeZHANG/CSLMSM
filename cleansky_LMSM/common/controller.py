from abc import ABC

import cleansky_LMSM.common.database as database
import cleansky_LMSM.common.model as model
import cleansky_LMSM.common.person as person
import cleansky_LMSM.common.view as view


class Controller(ABC):
    def __init__(self, my_view, my_model, my_person=person.Visitor()):
        """default authority is LEVEL VISITOR"""
        self.__view = my_view
        self.__model = my_model
        self.__person = my_person
        self.__view.set_controller(self)
        self.__model.set_controller(self)

    def get_view(self):
        return self.__view

    def get_model(self):
        return self.__model

    def get_person(self):
        """
        When our user logs in, if he switches between different GUI interfaces,
        we ensure the identity consistency by self.__person
        """
        return self.__person

    def set_new_person(self, new_person):
        """
        Factory of person:
        Create new person object for the current controller
        By default, you log in as a visitor
        """
        self.__person = {
            'None': None,
            'Visitor': person.Visitor(),
            'Reader': person.Reader(),
            'Creator': person.Creator(),
            'Valideur': person.Valideur(),
            'Administrator': person.Administrator(),
            'Manager': person.Manager()
        }[new_person]

    def run_view(self):
        self.__view.run_view()


class LoginController(Controller):
    def __init__(self, db_object):
        super(LoginController, self).__init__(view.LoginView(), model.LoginModel(db_object=db_object))

    def action_login(self):
        """
        A method that starts with Permission usually means the start of a request
        (broadly, not just a database request) that is written to the log,
        which is implemented in the Person class

        Methods that begin with Model tend to imply an interaction between the controller and the model, where the
        controller reads the user ID and password from the GUI interface after confirming permissions to the Person
        class, and then transfers login information to the model class using the Model method
        """
        if 'permission_login' in self.get_person().__dir__():
            self.get_person().permission_login()
            temp_username = self.get_view().get_username()
            temp_password = self.get_view().get_password()
            sql_result = self.get_model().model_login(temp_username, temp_password)
            if not sql_result:
                # The user does not exist in the database
                self.get_view().login_fail()
            else:
                self.get_view().login_success(sql_result[0][1], sql_result[0][10])
        else:
            print("login permission denied")


class ManagementController(Controller):
    def __init__(self, db_object, role=person.Reader()):
        super(ManagementController, self).__init__(view.ManagementView(), model.ManagementModel(db_object=db_object))
        self.set_person(role)

    def action_fill_orga(self):
        if 'permission_get_orga' in self.get_person().__dir__():
            self.get_person().permission_get_orga()
            sql_result = self.get_model().model_get_orga()
            # 出问题了
            return None
        else:
            print("get_orga permission denied")


if __name__ == "__main__":
    # for unittest
    unittest_db = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
    unittest_db.connect()
    obj = LoginController(db_object=unittest_db)
    obj.run_view()

    # unittest for set_person

    # obj2 = ManagementController(db_object=unittest_db)
    # obj2.run_view()
