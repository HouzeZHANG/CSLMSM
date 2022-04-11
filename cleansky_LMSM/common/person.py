"""
use attribute fetch to realize our permission control
"""


class Person:
    def __init__(self, user_info=None, user_right=None):
        """
        user_info becomes with request of SQL
        """
        self.__user_info = user_info
        self.__user_right = user_right

    def set_user_right(self, user_right):
        self.__user_right = user_right

    def set_user_info(self, user_info):
        self.__user_info = user_info

    def get_name(self):
        return self.__user_info[0][1]

    def get_uid(self):
        return self.__user_info[0][0]

    def __repr__(self):
        return "user_name: " + self.get_name()

    def permission_login(self):
        pass

    def permission_access_menu(self):
        """函数级别的抽象"""
        pass

    def permission_open_management(self):
        pass
