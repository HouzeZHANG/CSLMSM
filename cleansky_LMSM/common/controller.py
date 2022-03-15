from abc import ABC

import database
import model
import person
import view


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
        we need to ensure the identity consistency
        """
        return self.__person

    def set_person(self, new_person):
        """"""
        self.__person = new_person

    def run_view(self):
        self.__view.run_view()

    def start(self):
        self.run_view()


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
            self.set_person(self.get_model().model_login(temp_username, temp_password))
        else:
            print("login permission denied")


if __name__ == "__main__":
    # for unittest
    unittest_db = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
    unittest_db.connect()
    obj = LoginController(db_object=unittest_db)
    obj.run_view()
