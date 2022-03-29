import cleansky_LMSM.common.database as database
import cleansky_LMSM.common.model as model
import cleansky_LMSM.common.view as view
import logging


class RightsGraph:
    def __init__(self):
        self.element_dict, self.person_dict, self.mat, self.sparse_mat = {}, {}, [], []

    def update_graph(self, data):
        """
        稀疏矩阵

        """
        self.mat = data
        print('原矩阵更新完成')
        self.print_matrix()

        for vet in self.mat:
            for item in vet[2:]:
                if item is not None:
                    self.sparse_mat.append((vet[0], vet[1], vet[2:].index(item), item))

                    if (vet[2:].index(item), item) in self.person_dict.keys():
                        self.person_dict[(vet[2:].index(item), item)].append((vet[1], vet[0]))
                    else:
                        self.person_dict[(vet[2:].index(item), item)] = (vet[1], vet[0])

                    if (vet[0],) in self.element_dict.keys():
                        self.element_dict[(vet[0],)].append((vet[1], vet[2:].index(item), item))
                    else:
                        self.element_dict[(vet[0],)] = (vet[1], vet[2:].index(item), item)

        logging.info("graph updated")

        print('稀疏矩阵更新完成')
        self.print_sparse_mat()
        print('角色字典更新完成')
        self.print_per_dict()
        print('元素字典更新完成')
        self.print_ele_dict()

    def get_element_info(self, uid):
        # 返回的是一个元组列表
        return self.element_dict[(uid,)]

    def get_right_tables(self, type_id, ele_id):
        return self.person_dict[(type_id, ele_id)]

    def print_matrix(self):
        for item in self.mat:
            print(item)

    def print_sparse_mat(self):
        print('(uid, role-id, element-type, element-id)')
        print(self.sparse_mat)

    def print_ele_dict(self):
        print('(uid, )-->[(role-id, element-type, element-id), ...]')
        print(self.element_dict)

    def print_per_dict(self):
        print('(element-type, element-id)-->[(role-id, uid), ...]')
        print(self.person_dict)


class Controller:
    right_graph = RightsGraph()

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

    @staticmethod
    def tools_tuple_to_list(list_tuple):
        """
        单元素返回结果，拼装成列表
        """
        ret = []
        for item in list_tuple:
            ret.append(list(item)[0])
        return ret

    @staticmethod
    def tools_tuple_to_matrix(list_tuple):
        """
        多元素返回结果，拼装成矩阵
        """
        ret = []
        for item in list_tuple:
            ret.append(list(item))
        return ret

    @staticmethod
    def tools_delete_first_column(mat):
        for item in mat:
            item.pop(0)
        return mat

    def close_window(self):
        self.get_view().main_window_close()


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
                    mat = Controller.tools_tuple_to_matrix(self.get_model().model_get_all_rights())
                    Controller.right_graph.update_graph(Controller.tools_delete_first_column(mat))
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
            self.close_window()
            self.get_program().run_management()
        else:
            self.get_view().permission_denied()

    def action_open_items_to_be_tested(self):
        if 'permission_open_itbt' in self.get_role().__dir__():
            self.get_role().permission_open_itbt()
            self.close_window()
            self.get_program().run_items_to_be_tested()
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

    def action_fill_username_combobox(self, txt):
        data = self.get_model().get_user_list_by_organisation(txt)
        print(data)
        if not data:
            return []
        return self.tools_tuple_to_list(data)

    def action_fill_user_right_table(self, username):
        uid = self.get_model().model_get_uid_by_username(username)
        if not uid:
            return None
        tup_list = self.right_graph.get_element_info(uid[0][0])
        mat = []
        #     这个元组列表的每一个元组都是一个element三元组
        for item in tup_list:
            role_name = self.get_model().model_get_role_name(item)[0][0]
            element_info = self.get_model().model_get_element_info_by_tuple(item)
            mat.append([role_name, element_info[0][0] + element_info[0][1]])
        print(mat)
        return mat

    def action_fill_table_admin(self):
        mat = []
        for item in Controller.right_graph.sparse_mat:
            if item[1] == 2:
                element_tup_list = self.get_model().model_get_element_info_by_tuple(item)
                element_matrix = self.tools_tuple_to_matrix(element_tup_list)
                element_str = element_matrix[0][0] + '_' + element_matrix[0][1]
                user_tup_list = self.get_model().model_get_user_info_by_tuple(item)
                mat.append([element_str, self.tools_tuple_to_list(user_tup_list)[0]])
        return mat

    def action_fill_coating(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_coatings())

    def action_fill_detergent(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_detergent())

    @staticmethod
    def action_fill_insect():
        return ['YES', 'NO']

    def action_fill_means(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_means())

    def action_fill_tank(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_tank())

    def action_fill_sensor(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_sensor())

    @staticmethod
    def action_fill_acqui():
        return ['YES', 'NO']

    def action_fill_ejector(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_ejector())

    def action_fill_camera(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_camera())

    def action_fill_teams(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_teams())

    def action_test_points(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_points())

    def action_fill_intrinsic(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_intrinsic())

    def action_fill_rights(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_rights())


class ItemsToBeTestedController(Controller, TransactionInterface):
    def __init__(self, my_program, db_object, role):
        super(ItemsToBeTestedController, self).__init__(my_program=my_program,
                                                        my_view=view.ItemsToBeTestedView(),
                                                        my_model=model.ItemsToBeTestedModel(db_object=db_object),
                                                        my_role=role)
        self.get_model().model_start_transaction()

    def action_fill_coating_name(self):
        data = self.get_model().model_get_coatings()
        return self.tools_tuple_to_list(data)


if __name__ == '__main__':
    unittest_db = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
    unittest_db.connect()
    print(Controller.tools_tuple_to_list([]))
