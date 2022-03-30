import cleansky_LMSM.common.database as database
import cleansky_LMSM.common.model as model
import cleansky_LMSM.common.view as view
import logging


class RightsGraph:
    def __init__(self):
        self.element_dict, self.person_dict, self.mat, self.sparse_mat = {}, {}, [], []
        # 用来记录全部用户的集合
        self.user_set = set()

    def update_graph(self, data):
        """
        稀疏矩阵元素 - (user_id, role_id, element_type(排除前两列的矩阵), element_id)
        """
        self.element_dict, self.person_dict, self.mat, self.sparse_mat = {}, {}, [], []

        self.mat = data
        for vet in self.mat:
            for item in vet[2:]:
                if item is not None:

                    self.sparse_mat.append((vet[0], vet[1], vet[2:].index(item), item))
                    self.user_set.add(vet[0])

                    if (vet[2:].index(item), item) in self.person_dict.keys():
                        self.person_dict[(vet[2:].index(item), item)].append((vet[0], vet[1]))
                    else:
                        self.person_dict[(vet[2:].index(item), item)] = [(vet[0], vet[1])]

                    if (vet[0],) in self.element_dict.keys():
                        self.element_dict[(vet[0],)].append((vet[1], vet[2:].index(item), item))
                    else:
                        self.element_dict[(vet[0],)] = [(vet[1], vet[2:].index(item), item)]

        logging.info("graph updated")
        self.print_sparse_mat()
        self.print_ele_dict()
        self.print_per_dict()

    def get_user_right(self, uid):
        """
        查找某个用户节点的所有的邻接element节点
        """
        return self.element_dict[(uid,)]

    def get_right_tables(self, tup):
        """
        输入： tup = (element_type_id, element_ref_id)
        查找某个元素节点的全部领接person节点
        这个接口的名字起的不好
        """
        return self.person_dict[tup]

    def get_total_info_of_node(self, model_object, tup):
        """
        return None or [element_type, element_id, role, uname]
        返回的是字符串数组
        """
        if tup in self.sparse_mat:
            uname = model_object.model_get_username_by_uid(uid=tup[0])[0][0]
            # 传入的是四元祖
            info = model_object.tools_get_elements_info(list(tup))
            return info + [uname]
        else:
            return None

    def get_certain_element_owner_set(self, tup):
        """传入的是元素tuple, 返回的是拥有这个元素的uid集合"""
        owner_set = set()
        if tup in self.person_dict.keys():
            for item in self.person_dict[tup]:
                owner_set.add(item[0])
        return owner_set

    def get_certian_element_others_set(self, tup):
        """
        传入元素元组，返回拥有者和其他人的集合
        """
        owner_set = self.get_certain_element_owner_set(tup)
        other_set = self.user_set - owner_set
        return other_set

    def print_matrix(self):
        print('mat = :')
        print(self.mat)

    def print_sparse_mat(self):
        print('sparse_mat = :(user_id, role_id, element_type(排除前两列的矩阵), element_id)')
        print(self.sparse_mat)

    def print_ele_dict(self):
        print('ele_dict = :{user_id--->(role_id, ele_type, ele_id)}')
        print(self.element_dict)

    def print_per_dict(self):
        print('per_dict = :{(ele_type, ele_id)--->(user_id, role)}')
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
        多元素返回结果，拼装成矩阵, 这个函数有过度设计的嫌疑。。。
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

    def tools_update_graph(self):
        mat = Controller.tools_tuple_to_matrix(self.get_model().model_get_all_rights())
        self.right_graph.update_graph(Controller.tools_delete_first_column(mat))


class TransactionInterface:
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
        temp_username = self.get_view().get_username()
        temp_password = self.get_view().get_password()
        user_info = self.get_model().model_login(temp_username, temp_password)
        if not user_info:
            self.get_view().login_fail()
        else:
            self.get_view().login_success()
            self.get_role().set_user_info(user_info=user_info)
            self.tools_update_graph()
            self.get_program().run_menu(self.get_role())


class MenuController(Controller):
    def __init__(self, my_program, db_object, my_role):
        super(MenuController, self).__init__(my_program=my_program,
                                             my_view=view.MenuView(),
                                             my_model=model.MenuModel(db_object=db_object),
                                             my_role=my_role)

    def action_open_management(self):
        self.get_view().close_window()
        self.get_program().run_management()


class ManagementController(Controller, TransactionInterface):
    def __init__(self, my_program, db_object, role):
        super(ManagementController, self).__init__(my_program=my_program,
                                                   my_view=view.ManagementView(),
                                                   my_model=model.ManagementModel(db_object=db_object),
                                                   my_role=role)
        self.get_model().model_start_transaction()

    def action_fill_organisation(self):
        sql_result = self.get_model().model_get_orga()
        return self.tools_tuple_to_list(sql_result)

    def action_fill_user_list(self, orga):
        lis = self.get_model().model_get_list_of_users_by_organisation(orga)
        return Controller.tools_tuple_to_list(lis)

    def action_fill_user_table(self):
        """元组列表不需要转换成矩阵。。。"""
        user_list = self.get_model().model_get_list_of_users()
        # ret_table = []
        # for item in user_list:
        #     row = []
        #     for col in item:
        #         row.append(col)
        #     ret_table.append(row)
        return user_list

    def action_fill_user_right_table(self, txt):
        sql_ret = self.get_model().model_get_user_id(uname=txt)
        if not sql_ret:
            return []
        test_role = self.get_model().model_user_have_role(uid=sql_ret[0][0])
        if test_role[0] == (6,):
            return []
        uid = sql_ret[0][0]
        print('uid = ' + str(uid))
        if uid == 1 or uid == 2:
            return []
        list_of_tup = Controller.right_graph.get_user_right(uid=uid)
        # tup --- (role_id, ele_type, ele_id)
        mat = []
        for item in list_of_tup:
            item = list(item)
            mat.append(self.get_model().tools_get_elements_info(item))
        return mat

    def action_fill_administrator_table(self):
        mat = []
        for tup in Controller.right_graph.sparse_mat:
            if tup[1] == 2:
                info = Controller.right_graph.get_total_info_of_node(self.get_model(), tup)
                if info is not None:
                    uname = info[3]
                    ele_info = info[0:2]
                    mat.append(ele_info + [uname])
        if not mat:
            return None
        else:
            return mat

    def action_validate_user(self, lis):
        """
        关于接口的调整，不需要下面这行代码，虽然这行代码很酷炫
        """
        # lis = [i if i != '' else None for i in lis]
        if not self.get_model().model_get_uid_by_uname(lis[0]):
            #     系统中不存在该用户
            self.get_model().model_create_new_user(uname=lis[0], orga=lis[1], fname=lis[2], lname=lis[3], tel=lis[4],
                                                   email=lis[5], password=lis[6])
            self.get_view().add_table_user_modify([lis[0], 'CREATE'])
        else:
            self.get_model().model_update_user(uname=lis[0], new_username=lis[0], organisation=lis[1],
                                               last_name=lis[3], tel=lis[4], first_name=lis[2],
                                               email=lis[5], password=lis[6])
            self.get_view().add_table_user_modify([lis[0], 'UPDATE'])
        self.tools_update_graph()
        self.get_view().refresh()

    def action_delete_user(self, uname):
        uid = self.get_model().model_get_uid_by_uname(uname)
        if uid:
            self.get_model().model_delete_user(uname)
            self.tools_update_graph()
            self.get_view().add_table_user_modify([uname, 'DELETE'])
            self.get_view().refresh()

    def action_fill_coating(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_coatings())

    def action_fill_detergent(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_detergent())

    def action_fill_insect(self):
        return ['YES', 'NO']

    def action_fill_means(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_means())

    def action_fill_tank(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_tank())

    def action_fill_sensor(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_sensor())

    def action_fill_acqui(self):
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

    def action_fill_combobox_test_mean(self, txt):
        data = self.get_model().model_get_means_name_by_means_type(txt)
        return self.tools_tuple_to_list(data)

    def action_fill_serial(self, mean_type, mean_name):
        data = self.get_model().model_get_means_number_by_means_name(mean_type, mean_name)
        return self.tools_tuple_to_list(data)

    def action_fill_user_right_list(self, table_number, ref_tup):
        """
        table_number取决于调用本函数的槽函数，对应于model类中定义的表字典
        ref_tup有可能是三元组，也有可能是单元组
        """
        if not self.get_model().model_get_ele_id_by_ref(table_number, ref_tup):
            # 不存在这种element
            print('不存在这种元素')
            return None, None
        else:
            print('存在这种元素')
            element_id = self.get_model().model_get_ele_id_by_ref(table_number, ref_tup)[0][0]
            print('元素id = ' + str(element_id))

            mat = []
            lis = []
            others_set = set()
            # 判断是否有人拥有这种元素
            if (table_number, element_id) in self.right_graph.person_dict.keys():
                list_of_owners = self.right_graph.person_dict[(table_number, element_id)]
                others_set = self.right_graph.get_certian_element_others_set((table_number, element_id))

                for item in list_of_owners:
                    # 遍历每一个拥有者节点，获得权限信息和用户名信息
                    role_str = self.get_model().model_get_role_ref(item[1])[0][0]
                    username = self.get_model().model_get_username_by_uid(item[0])[0][0]
                    mat.append([username, role_str])
            else:
                mat = None
                others_set = self.right_graph.user_set

            for item in iter(others_set):
                lis.append(self.get_model().model_get_username_by_uid(item)[0][0])

            print(mat)
            print(lis)
            return mat, lis


if __name__ == '__main__':
    unittest_db = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
    unittest_db.connect()
    print(Controller.tools_tuple_to_list([]))
