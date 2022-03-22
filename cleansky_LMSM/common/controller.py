import cleansky_LMSM.common.database as database
import cleansky_LMSM.common.model as model
import cleansky_LMSM.common.view as view


class Controller:
    def __init__(self, my_program, my_view, my_model, my_role):
        """default authority is LEVEL VISITOR"""
        self.__view = my_view
        self.__model = my_model
        self.__role = my_role
        self.__program = my_program
        self.__view.set_controller(self)
        self.__model.set_controller(self)

    def get_program(self):
        return self.__program

    def get_view(self):
        return self.__view

    def get_model(self):
        return self.__model

    def get_role(self):
        return self.__role

    def run_view(self):
        self.__view.run_view()


class TransactionInterface:
    # 鸭子类型
    def action_start_transaction(self):
        self.get_model().model_start_transaction()

    def action_roll_back(self):
        self.get_model().model_roll_back()

    def action_submit(self):
        self.get_model().model_submit()


class LoginController(Controller):
    def __init__(self, my_program, db_object, my_role):
        super(LoginController, self).__init__(my_program=my_program,
                                              my_view=view.LoginView(),
                                              my_model=model.LoginModel(db_object=db_object),
                                              my_role=my_role)

    def action_login(self):
        if 'permission_login' in self.get_role().__dir__():
            self.get_role().permission_login()
            temp_username = self.get_view().get_username()
            temp_password = self.get_view().get_password()
            user_info = self.get_model().model_login(temp_username, temp_password)
            if not user_info:
                # The user does not exist in the database
                self.get_view().login_fail()
            else:
                self.get_view().login_success()
                # 更具登录信息，创建person对象，更新role成员变量
                user_right = self.get_model().model_get_right(temp_username)
                self.get_role().set_user_info(user_info=user_info)
                self.get_role().set_user_right(user_right=user_right)
                if 'permission_access_menu' in self.get_role().__dir__():
                    self.get_role().permission_access_menu()
                    self.get_program().run_menu(self.get_role())
                else:
                    self.get_view().permission_denied()
        else:
            self.get_view().permission_denied()


class MenuController(Controller):
    def __init__(self, my_program, db_object, my_role):
        super(MenuController, self).__init__(my_program=my_program,
                                             my_view=view.MenuView(),
                                             my_model=model.MenuModel(db_object=db_object),
                                             my_role=my_role)

    def action_open_management(self):
        if 'permission_open_management' in self.get_role().__dir__():
            self.get_role().permission_open_management()
            self.get_view().access_management_success()
            self.get_program().run_management()
        else:
            self.get_view().permission_denied()


class ManagementController(Controller, TransactionInterface):
    def __init__(self, my_program, db_object, role):
        super(ManagementController, self).__init__(my_program=my_program,
                                                   my_view=view.ManagementView(),
                                                   my_model=model.ManagementModel(db_object=db_object),
                                                   my_role=role)
        self.get_model().model_start_transaction()

    def action_fill_organisation(self):
        sql_result = self.get_model().model_get_orga()
        ret_lis = []
        for item in sql_result:
            ret_lis.append(item[0])
        return ret_lis

    def action_fill_user_table(self):
        user_list = self.get_model().model_get_list_of_users()
        # 用来记录用户信息的二维矩阵
        ret_table = []
        for item in user_list:
            row = []
            for col in item:
                row.append(col)
            ret_table.append(row)
        return ret_table


if __name__ == '__main__':
    unittest_db = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
    unittest_db.connect()
