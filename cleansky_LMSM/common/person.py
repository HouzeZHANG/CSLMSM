"""
use attribute fetch to realize our permission control
"""
from abc import ABC, abstractmethod


class Person:
    def __init__(self, user_info=None):
        """
        user_info becomes with request of SQL
        """
        self.__user_info = user_info

    def get_name(self):
        return self.__user_info[0][1]

    def get_uid(self):
        return self.__user_info[0][0]

    def get_role(self):
        return self.__user_info[0][10]


class Visitor(Person):
    def permission_login(self):
        print("login permission checked")


class Reader(Visitor):
    def permission_access_menu(self):
        print("access_menu permission checked")

    def permission_get_orga(self):
        print("get_orga permission checked")

    def permission_open_management(self):
        print("access_management permission checked")

class Creator(Reader):
    pass


class Valideur(Creator):
    pass


class Administrator(Valideur):
    """
    The administrator controls the data access rights of his employees through the user assignment interface
    """
    pass


class Manager(Administrator):
    """
    Managers have all the authority, and they can give administrators the necessary authority.
    """

    def create_user(self):
        """
        mentioned page 5
        Only manager can use User Management GUI to create user...
        """
        pass


class CreatePerson(ABC):
    @staticmethod
    def create_person(user_info=None):
        pass


class PersonFactory(CreatePerson):
    @staticmethod
    def create_person_by_user_info(user_info=None):
        person_dict = {
            'person': Person(user_info=user_info),
            'visitor': Visitor(user_info=user_info),
            'reader': Reader(user_info=user_info),
            'creator': Creator(user_info=user_info),
            'valideur': Valideur(user_info=user_info),
            'administrator': Administrator(user_info=user_info),
            'manager': Manager(user_info=user_info),
            None: Visitor(user_info=user_info)
        }
        return person_dict[user_info[0][10]]

    @staticmethod
    def create_person_by_str(type_str):
        person_dict = {
            'person': Person(),
            'visitor': Visitor(),
            'reader': Reader(),
            'creator': Creator(),
            'valideur': Valideur(),
            'administrator': Administrator(),
            'manager': Manager(),
            None: Visitor()
        }
        return person_dict[type_str]


if __name__ == '__main__':
    manager = Manager()
    visitor = Visitor()
    print(manager)
    print(manager.__class__)
    print(manager.__class__.__name__)
    print(list(manager.__dict__.keys()))
    print(dir(manager))

    print(manager.__dir__())
    print(visitor.__dir__())
