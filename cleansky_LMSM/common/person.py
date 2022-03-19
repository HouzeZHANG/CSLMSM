"""
use attribute fetch to realize our permission control
"""


class Person:
    def __init__(self, name=None):
        self.__name = name

    def get_name(self):
        return self.__name


class Visitor(Person):
    def permission_login(self):
        print("login permission checked")


class Reader(Visitor):
    def permission_get_orga(self):
        print("get_orga permission checked")
    pass


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
