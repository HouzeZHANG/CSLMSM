from abc import ABC, abstractmethod

import cleansky_LMSM.common.database as database
import cleansky_LMSM.common.model as model
import cleansky_LMSM.common.view as view

import cleansky_LMSM.tools.tree as tree
import cleansky_LMSM.tools.type_checker as tc
import cleansky_LMSM.tools.graph as mg

import pandas as pd


class Controller(ABC):
    """
    Controller基类负责实现控制器所共有的接口
    """
    right_graph = mg.ElementRightGraph()

    def __init__(self, my_program, my_view, my_model, my_role):
        """
        """
        self.__view = my_view
        self.__model = my_model
        self.__role = my_role
        self.__program = my_program
        self.__view.set_controller(self)
        self.__model.set_controller(self)

    @abstractmethod
    def action_close_window(self):
        """Main_window的closeEvent事件会自动调用该函数"""
        pass

    def action_roll_back(self):
        self.get_model().model_roll_back()
        self.tools_update_graph()

    def action_submit(self):
        self.get_model().model_commit()
        self.tools_update_graph()

    def action_is_in_transaction(self):
        return self.get_model().is_in_transaction()

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
        """单元素返回结果，拼装成列表"""
        if not list_tuple:
            return []

        ret = []
        for item in list_tuple:
            ret.append(list(item)[0])
        return ret

    @staticmethod
    def tools_tuple_to_matrix(list_tuple):
        """
        多元素返回结果，拼装成矩阵, 这个函数有过度设计的嫌疑。。。
        """
        if not list_tuple:
            return []

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
        mat = Controller.tools_tuple_to_matrix(self.get_model().model_get_rights_for_graph())
        self.right_graph.update_graph(Controller.tools_delete_first_column(mat))


class LoginController(Controller):
    def __init__(self, my_program, db_object, my_role):
        super(LoginController, self).__init__(my_program=my_program,
                                              my_view=view.LoginView(),
                                              my_model=model.LoginModel(db_object=db_object),
                                              my_role=my_role)

    def action_close_window(self):
        pass

    def action_login(self):
        temp_username = self.get_view().get_username()
        temp_password = self.get_view().get_password()
        user_info = self.get_model().model_login(temp_username, temp_password)
        if not user_info:
            self.get_view().login_fail()
        else:
            self.get_view().main_window_close()
            self.get_role().set_user_info(user_info=user_info)
            self.tools_update_graph()
            self.get_program().run_menu()


class MenuController(Controller):
    def __init__(self, my_program, db_object, my_role):
        super(MenuController, self).__init__(my_program=my_program,
                                             my_view=view.MenuView(),
                                             my_model=model.MenuModel(db_object=db_object),
                                             my_role=my_role)
        # 告诉action_close_windows这个触发函数，到底是否需要显示login页面
        self.ret_to_login = True

    def action_close_window(self):
        """BUG：mainWindowClose也会调用closeEvent"""
        if self.ret_to_login:
            self.get_program().run_login()

    def action_open_management(self):
        self.ret_to_login = False
        self.get_view().main_window_close()
        self.get_program().run_management()

    def action_open_items_to_be_tested(self):
        self.ret_to_login = False
        self.get_view().main_window_close()
        self.get_program().run_items_to_be_tested()

    def action_open_list_of_test_means(self):
        self.ret_to_login = False
        self.get_view().main_window_close()
        self.get_program().run_list_of_test_items()


class ManagementController(Controller):
    def __init__(self, my_program, db_object, role):
        super(ManagementController, self).__init__(my_program=my_program,
                                                   my_view=view.ManagementView(),
                                                   my_model=model.ManagementModel(db_object=db_object),
                                                   my_role=role)

    def action_close_window(self):
        self.get_program().run_menu()

    def action_fill_user_info(self, username):
        user_list = self.get_model().model_get_list_of_users()
        if not user_list:
            return None

        for item in user_list:
            if item[1] == username:
                return item

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

    def action_fill_fname_lname(self, uname):
        fname = self.get_model().model_get_fname(uname)
        if fname:
            fname = self.tools_tuple_to_list(fname)

        lname = self.get_model().model_get_lname(uname)
        if lname:
            lname = self.tools_tuple_to_list(lname)

        print(fname)
        print(lname)

        return fname, lname

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

    def action_fill_simple_element(self, table_name):
        return Controller.tools_tuple_to_list(self.get_model().model_get_element_ref(table_name))

    def action_fill_coating(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_element_ref('type_coating'))

    def action_fill_detergent(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_element_ref('type_detergent'))

    def action_fill_means(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_means_type())

    def action_fill_tank(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_tank())

    def action_fill_sensor(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_sensor())

    @staticmethod
    def action_fill_acq():
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
        """用means type查找means name"""
        data = self.get_model().model_get_means_name_by_means_type(txt)
        return self.tools_tuple_to_list(data)

    def action_fill_serial(self, mean_type, mean_name):
        data = self.get_model().model_get_means_number_by_means_name(mean_type, mean_name)
        return self.tools_tuple_to_list(data)

    def action_fill_user_right_list(self, table_number, ref_tup):
        """
        table_number会由槽函数配置，对应于model类中定义的表字典，ref_tup有可能是三元组，也有可能是单元组
        others_set存储右列表的用户
        """
        lis, mat = [], []

        if not self.get_model().get_ele_id_by_ref(table_number, ref_tup):
            for item in iter(self.right_graph.user_set):
                lis.append(self.get_model().model_get_username_by_uid(item)[0][0])
            return None, lis

        element_id = self.get_model().get_ele_id_by_ref(table_number, ref_tup)[0][0]

        # 判断是否有人拥有这种元素
        if (table_number, element_id) in self.right_graph.person_dict.keys():
            list_of_owners = self.right_graph.person_dict[(table_number, element_id)]
            others_set = self.right_graph.get_certian_element_others_set((table_number, element_id))

            # 标记是否存在管理员
            admin_exist = False
            for item in list_of_owners:
                # 遍历每一个拥有者节点，获得权限信息和用户名信息
                role_str = self.get_model().model_get_role_ref(item[1])[0][0]
                username = self.get_model().model_get_username_by_uid(item[0])[0][0]
                if role_str == 'administrator':
                    admin_exist = True
                mat.append([username, role_str])
        else:
            mat = None
            others_set = self.right_graph.user_set
        for item in iter(others_set):
            lis.append(self.get_model().model_get_username_by_uid(item)[0][0])
        return mat, lis

    def change_role(self, element_type, ref_tup, person_name, role_str, state: int):
        """对元素权限的修改"""
        print('element_type: ' + str(element_type))
        print('element_info: ' + str(ref_tup))
        print('person_name: ')
        print(person_name)
        print('role_str: ' + role_str)
        print('state = ' + str(state))

        if not self.get_model().get_ele_id_by_ref(element_type, ref_tup):
            # 不存在这种element
            # 创建新元素，判断元素信息是否合法
            if element_type == 0:
                for item in ref_tup:
                    if item == '':
                        return
            else:
                if ref_tup[0] == '':
                    return
            self.get_model().model_create_new_element(element_type, ref_tup)

        uid = self.get_model().model_get_uid_by_uname(uname=person_name)[0][0]
        role_id = self.get_model().model_get_role_id(role_ref=role_str)[0][0]
        element_id = self.get_model().get_ele_id_by_ref(table_number=element_type, ref_tup=ref_tup)[0][0]

        if state == 0 and role_str == 'none':
            self.get_model().model_delete_user_right(uid=uid, element_type=element_type, element_id=element_id)

        if state == 0 and role_str != 'none':
            self.get_model().model_update_user_right(uid=uid, element_type=element_type, element_id=element_id,
                                                     role_id=role_id)

        if state == 1 and role_str != 'none':
            self.get_model().model_insert_user_right(uid=uid, element_type=element_type, element_id=element_id,
                                                     role_id=role_id)

        self.tools_update_graph()


class InsectState:
    """这是一个专门用来管理insect状态的类"""

    def __init__(self):
        self.state_dict = {}

    def add_state(self, name, state):
        self.state_dict[name] = state

    def get_state(self, name):
        """避免keyError"""
        if name not in self.state_dict.keys():
            return ''
        else:
            return self.state_dict[name]

    def refresh(self):
        """切换页面，db_transfer，cancel的时候refresh"""
        self.state_dict.clear()


class ItemsToBeTestedController(Controller):
    """
    策略设计模式
    """

    def __init__(self, my_program, db_object, role):
        super(ItemsToBeTestedController, self).__init__(my_program=my_program,
                                                        my_view=view.ItemsToBeTestedView(),
                                                        my_model=model.ItemsToBeTestedModel(db_object=db_object),
                                                        my_role=role)
        self.insect_state = InsectState()
        # 该变量用于指明当前页面在coating还是在detergent，三种状态（True，False，None），
        # True意味着Coating，False意味着detergent，None意味着Insect
        self.is_coating = True

        # 该成员变量用于使能editable与否
        self.flag_coating_enabled = True
        self.flag_detergent_enabled = True

    def action_close_window(self):
        self.get_program().run_menu()

    def print_state(self):
        print("\nis_coating = " + str(self.is_coating))
        print("coating_enabled = " + str(self.flag_coating_enabled))
        print("detergent_enabled = " + str(self.flag_detergent_enabled) + "\n")

    def action_get_element_type(self):
        """
        根据当前登录用户的身份查找属于他的coating元素，并展示在combobox中
        """
        uid = self.get_role().get_uid()
        if uid in self.right_graph.admin_set:
            # 如果是管理员，则显示全部coating类别
            type_strategy = 'type_coating' if self.is_coating else 'type_detergent'
            return self.tools_tuple_to_list(self.get_model().model_get_element_ref(type_strategy))
        if (uid,) not in self.right_graph.element_dict.keys():
            # 用户什么权限也没有，什么都不返回（在user_right中只有一行权限为6的记录，这时候用户是不会被添加到字典中的，只会存在在稀疏矩阵中）
            return []
        else:
            # 用户有对某一个设备的权限，其身份不为管理员，此时需要筛选出其对coating设备的记录
            lis = []
            for item in self.right_graph.element_dict[(uid,)]:
                # 策略模式
                column_number = 1 if self.is_coating else 2
                if item[1] == column_number and item[0] < 6:
                    # 如果item[0]这一项小于六，意味着至少有只读权限，所以添加到lis中
                    lis.append(item[2])
            if not lis:
                # 用户没有对任何coating的权限
                return lis
            else:
                ret = []
                for item in lis:
                    # 策略模式
                    table_name = 'type_coating' if self.is_coating else 'type_detergent'
                    ret.append(self.get_model().model_get_simple_ele(table_name=table_name, ele_id=item)[0][0])
                return ret

    def action_get_element_position(self, element_type):
        """
        根据元素类型表格填充position表格
        """
        table_number = 1 if self.is_coating else 2
        element_id = self.get_model().get_ele_id_by_ref(table_number, (element_type,))
        if not element_id:
            # 不存在这种coating type
            return []
        else:
            # 存在这种type
            element_id = element_id[0][0]
            uid = self.get_role().get_uid()
            element_type_id = 1 if self.is_coating else 2
            token = self.right_graph.get_token(uid, element_type_id, element_id)

            if token <= 4:
                self.get_view().question_for_validate(self.is_coating)
            else:
                self.get_view().direct_commit(self.is_coating)

            data = self.get_model().model_get_number(element_type, self.is_coating)
            if not data:
                return []
            else:
                return self.tools_tuple_to_list(data)

    # def action_get_coating_table(self, element_type, number_name):
    #     mat = self.get_model().model_get_coating_attributes(element_type, number_name)
    #     if not mat:
    #         mat = None
    #     return mat

    def disable_modify(self):
        if self.is_coating:
            if self.flag_coating_enabled:
                self.get_view().disable_modify()
        elif self.is_coating is False:
            if self.flag_detergent_enabled:
                self.get_view().disable_modify()

    def enable_modify(self):
        if self.is_coating:
            if not self.flag_coating_enabled:
                self.get_view().enable_modify()
        elif self.is_coating is False:
            if not self.flag_detergent_enabled:
                self.get_view().enable_modify()

    def action_config_by_type_number(self, element_type, number_name):
        # coating_type没填，直接返回
        self.get_view().refresh_value(self.is_coating)
        if element_type == '':
            self.disable_modify()
            return None, None, None

        # 权限图中必定存在一条边描述该用户和该设备的关系，找出权限
        uid = self.get_role().get_uid()
        element_type_id = 1 if self.is_coating else 2
        token = self.right_graph.get_token(uid, element_type_id, element_type_id)
        print("token= " + str(token))

        if token == 6:
            self.disable_modify()
            return None, None, None

        # 填充list
        mat = self.get_model().model_get_element_attributes(element_type, number_name, self.is_coating)
        if not mat:
            mat = None
        print("\nmat= ")
        print(mat)

        # 用type coating查找
        chara = self.get_model().model_get_element_char(element_type, self.is_coating)
        if chara:
            chara = self.tools_tuple_to_list(chara)

        unity = self.tools_tuple_to_list(self.get_model().model_get_unity())

        # 判断number是否存在
        # 如果数据被validate了，擦去db transfer， search， create
        is_validate = self.get_model().is_validate(element_type, number_name, self.is_coating)
        if is_validate:
            # 存在这种元素
            print("存在这种元素")
            is_validate = is_validate[0][0]
            if is_validate or token == 5:
                # validated 或者用户为只读权限
                self.disable_modify()
            else:
                # not validated
                #     这里可以加一条将三元组设置成不可编辑
                if token == 4:
                    # 只有创建权限的用户
                    self.get_view().direct_commit(self.is_coating)
                    self.enable_modify()
                else:
                    # valid或者admin或者manager，添加validate询问的窗口
                    self.get_view().question_for_validate(self.is_coating)
                    self.enable_modify()
        else:
            # 不存在这种元素
            print("不存在这种元素")
            if token <= 4:
                self.enable_modify()
            else:
                self.disable_modify()
        return chara, unity, mat

    def action_create_element(self, element_type_name, number, attribute_name, unity, value):
        """
        如果用户点击了，肯定是有权限创建的，所以权限检查不需要做

        其次，将create的粒度降低，如果当前没有position，就算attribute，unity和value被填充了，也不会创建对应的attribute
        必须先点击一次create将position创建好了，再点击一次create才可以insert attribute
        """
        if not element_type_name or not number:
            return

        # 获取type_id
        table_name = 'type_coating' if self.is_coating else 'type_detergent'
        element_type_id = self.get_model().model_get_simple_id(table_name=table_name, ele_ref=element_type_name)[0][0]
        element_exist = self.get_model().is_exist_element(element_type_name, number, self.is_coating)
        print("待创建的元素element_type_id=" + str(element_type_id))
        print("待创建的元素element_exist=" + str(element_exist))

        if not element_exist:
            # 先判断number是否存在，如果不存在，创建number随后直接返回
            self.get_model().model_create_new_element(element_type_id, number, self.is_coating)
            self.get_view().setup_tab_coating_and_detergent()
            print("新number" + number + "已创建")
        else:
            if not attribute_name:
                # 如果输入不合法，没有attribute_name直接返回
                return

            unity_id = self.get_model().model_is_unity_exist(unity)
            if not unity_id:
                # 如果不存在单位，先创建单位
                unity_id = self.get_model().model_create_new_unity(unity)[0][0]
                print("新单位" + unity + "已创建")
            else:
                unity_id = unity_id[0][0]
            # 更新unity列表
            lis = self.get_model().model_get_unity()
            self.get_view().setup_combobox_unity(items=self.tools_tuple_to_list(lis), strategy=self.is_coating)

            # 如果不存在attribute三元组，创建三元组
            attr_id = self.get_model().model_is_exist_attr(attribute_name, unity_id, value)
            if not attr_id:
                attr_id = self.get_model().model_create_new_attr(attribute_name, unity_id, value)[0][0]
                print("新attr" + attribute_name + str(value) + "已创建")
            else:
                attr_id = attr_id[0][0]
            print("attribute_id=" + str(attr_id))

            element_id = self.get_model().get_element_id(element_type_name, number, self.is_coating)[0][0]
            print("eid" + str(element_id))
            is_connected = self.get_model().is_connected_element_and_attribute(element_type_id, attr_id,
                                                                               self.is_coating)
            if not is_connected:
                # 确定是当前coating未绑定的新的attribute，将其绑定
                self.get_model().create_connexion(element_id, attr_id, self.is_coating)
                print("新关系" + str(element_type_id) + str(attr_id) + "已创建")

                # 刷新表格
                mat = self.get_model().model_get_element_attributes(element_type_name, number, self.is_coating)
                print(mat)
                self.get_view().refresh_table(mat=mat, strategy=self.is_coating)

    def action_delete_element_attribute(self, element_type_name, number, attribute_name, value, unity):
        # 拿权限
        table_name = 'type_coating' if self.is_coating else 'type_detergent'
        element_id = self.get_model().model_get_simple_id(table_name=table_name, ele_ref=element_type_name)[0][0]
        # 权限图中必定存在一条边描述该用户和该设备的关系，找出权限
        uid = self.get_role().get_uid()
        token = self.right_graph.get_token(uid, element_type_id=1 if self.is_coating else 2, element_id=element_id)

        is_validate = self.get_model().is_validate(element_type_name, number, self.is_coating)[0][0]
        if is_validate:
            return

        if token <= 4:
            self.get_model().delete_element_attr(element_type_name, number, attribute_name, value, unity,
                                                 self.is_coating)
            mat = self.get_model().model_get_element_attributes(element_type_name, number, self.is_coating)
            print(mat)
            self.get_view().refresh_table(mat=mat, strategy=self.is_coating)

    def action_validate_element(self, element_type_name, number):
        self.get_model().validate_element(element_type_name, number, self.is_coating)

    def action_get_names_hemolymphe(self):
        names = self.tools_tuple_to_list(self.get_model().model_get_insect_names())
        hemo = self.tools_tuple_to_list(self.get_model().model_get_hemo())
        return names, hemo

    def action_get_insect_table(self):
        """
        strategy is False 意味着是页面的初始化
        strategy is True 意味着是页面的更新
        除了展示所有的数据库中的数据，还需要展示每一个insect的state
        """
        mat = self.get_model().model_get_insect()
        if not mat:
            return None
        mat = self.tools_tuple_to_matrix(mat)
        for item in mat:
            item.append(self.insect_state.get_state(item[0]))
        return mat

    def action_add_insect(self, **kwargs):
        if self.get_model().model_is_exist_insect(kwargs['name']):
            # 如果存在这种昆虫
            self.insect_state.add_state(kwargs['name'], 'UPDATED')
            self.get_model().model_update_insect(**kwargs)
        else:
            self.insect_state.add_state(kwargs['name'], 'CREATED')
            self.get_model().model_insert_insect(**kwargs)


class ListOfTestMeansController(Controller):
    def __init__(self, my_program, db_object, role):
        super(ListOfTestMeansController, self).__init__(my_program=my_program,
                                                        my_view=view.ListOfTestMeansView(),
                                                        my_model=model.ListOfTestMeansModel(db_object=db_object),
                                                        my_role=role)
        # test_mean的树对象
        self.test_mean_tree = tree.Tree()
        # 负责记录test_mean的token <= 4为creator权限
        self.test_mean_token, self.test_mean_validate = 6, True
        self.modify_flag = None

    def action_close_window(self):
        self.get_program().run_menu()

    def action_fill_means(self):
        """这里要查权限"""
        uid = self.get_role().get_uid()
        if uid in self.right_graph.admin_set:
            ret = self.get_model().all_test_means()
        else:
            # 不是管理员
            ret = self.get_model().test_means_str_by_uid(uid=uid)
        self.test_mean_tree.initialize_by_mat(ret)

        # 查找第一层
        return tree.show_sub_node_info(self.test_mean_tree.root)

    def action_fill_combobox_test_mean(self, txt):
        """用means type查找means name"""
        root = self.test_mean_tree.search(txt)
        if root is None:
            return None
        return tree.show_sub_node_info(root)

    def action_fill_serial(self, mean_type, mean_name):
        """用means type和means name查找serial"""
        root1 = self.test_mean_tree.search(mean_type)
        root2 = tree.search_node(root1, mean_name)
        return tree.show_sub_node_info(root2)

    def action_get_attributes_and_params(self, mean_type: str, mean_name: str, mean_number: str) -> tuple:
        """
        在means三个选项都填上之后，获取attributes
        chara_list 左侧characteristic combobox
        attr_unity_list 左侧unity combobox
        params_combobox  右侧params的combobox
        params_list 右侧param列表
        params_unity 右侧param的unity combobox
        """
        attr = self.get_model().model_get_element_attributes(mean_type, (mean_name, mean_number), 2)
        if not attr:
            # 如果不存在attributes，将左侧attribute列表清空
            chara_list = None

        ele_id = self.get_model().get_element_id(mean_type, (mean_name, mean_number), strategy=2)[0][0]
        uid = self.get_role().get_uid()
        self.test_mean_token = self.right_graph.get_token(uid=uid, element_type_id=0, element_id=ele_id)
        # 获取元素validate
        self.test_mean_validate = self.get_model().is_validate(type_element=mean_type, number=(mean_name, mean_number),
                                                               strategy=2)[0][0]

        # 配置create按钮和validate窗口
        if self.test_mean_validate or self.test_mean_token >= 4:
            # 没有validate的权限
            self.get_view().means_validate_token = False
        else:
            # 有validate的权限
            self.get_view().means_validate_token = True

        if not self.test_mean_validate and self.test_mean_token <= 4:
            # 用户有修改的权限，使能create组件
            self.get_view().enable_modify(1)
        else:
            self.get_view().disable_modify(1)

        # 暂且将两个unity都设置为unity全集
        attr_unity_list = self.tools_tuple_to_list(self.get_model().model_get_unity())
        params_unity = attr_unity_list

        # 获取当前三元组所对应的所有attributes
        chara_list = self.get_model().model_get_element_char((mean_type, mean_name, mean_number), 2)
        chara_list = self.tools_tuple_to_list(chara_list)

        params_combobox = self.get_model().get_all_params()
        # 使用列表生成器，筛选params的names
        if not params_combobox:
            params_combobox = None
        else:
            params_combobox = [item[0] for item in params_combobox]
            print(params_combobox)

        params_table = self.get_model().get_params_by_element((mean_type, mean_name, mean_number),
                                                              strategy=2)
        if not params_table:
            params_table = None

        return chara_list, attr_unity_list, params_combobox, params_table, params_unity, attr

    def action_create_new_attr(self, means, attribute):
        """
        不需要考虑权限问题，如果没有权限，该信号不会被接受
        传入参数tup的格式为：(means_type, means_name, mean_number, attr, unity, value)
        """

        # 类型检查
        if not tc.AttributeChecker.type_check(attribute) or not tc.TestMeanChecker.type_check(means):
            return None

        # 检查unity是否存在
        unity_id = self.get_model().model_is_unity_exist(attribute[1])
        if not unity_id:
            unity_id = self.get_model().model_create_new_unity(attribute[1])
        unity_id = unity_id[0][0]

        print(unity_id)

        # 检查attribute是否存在
        attr_id = self.get_model().model_is_exist_attr(attribute[0], unity_id, attribute[2])
        if not attr_id:
            attr_id = self.get_model().model_create_new_attr(attribute_name=attribute[0], unity_id=unity_id,
                                                             value=attribute[2])
        attr_id = attr_id[0][0]

        print(attr_id)

        # 获取means id
        means_id = self.get_model().get_element_id(means[0], means[1:], strategy=2)[0][0]
        print(means_id)

        # 创建链接
        link_id = self.get_model().is_connected_element_and_attribute(element_id=means_id, attr_id=attr_id, strategy=2)
        if not link_id:
            self.get_model().create_connexion(attr_id=attr_id, element_id=means_id, strategy=2)

    def action_delete_attr(self, means_tup: tuple, attr_tup: tuple):
        """解绑attribute"""
        means_id = self.get_model().get_element_id(means_tup[0], (means_tup[1], means_tup[2]), strategy=2)
        if not means_id:
            return
        means_id = means_id[0][0]
        print("means_id: " + str(means_id))
        uid = self.get_role().get_uid()
        token = self.right_graph.get_token(uid=uid, element_type_id=0, element_id=means_id)
        if token >= 5:
            # 对于只读用户，没有权限
            return

        self.get_model().delete_element_attr(means_tup[0], (means_tup[1], means_tup[2]), attr_tup[0], attr_tup[1],
                                             attr_tup[2], strategy=2)

    def action_validate_mean(self, mean_tup):
        """validate mean"""
        self.get_model().validate_element(mean_tup[0], (mean_tup[1], mean_tup[2]), strategy=2)

    def action_param_link(self, means_tup: tuple, param_tup: tuple):
        """创建新的param"""
        mean_id = self.get_model().get_element_id(element_name=means_tup[0], number=means_tup[1:], strategy=2)[0][0]
        if not self.get_model().is_exist_param(param=param_tup):
            self.get_model().create_new_param(param=param_tup)
        param_id = self.get_model().is_exist_param(param_tup)[0][0]
        if not self.get_model().is_exist_param_link(element_id=mean_id, param_id=param_id, strategy=2):
            # 如果不存在该链接
            self.get_model().create_param_link(element_id=mean_id, param_id=param_id, strategy=2)

    def action_delete_param(self, means_tup: tuple, param_tup: tuple):
        """删除param"""
        if self.test_mean_token <= 4 and not self.test_mean_validate:
            ret = self.get_model().is_exist_element(type_element=means_tup[0], number=means_tup[1:], strategy=2)
            element_id = ret[0][0]
            ret = self.get_model().is_exist_param(param_tup)
            param_id = ret[0][0]

            self.get_model().delete_param_link(element_id=element_id, param_id=param_id, strategy=2)

    def ejector_table(self):
        ret = self.get_model().ejector_table()
        if not ret:
            return None
        return ret

    def camera_table(self):
        ret = self.get_model().camera_table()
        if not ret:
            return None
        return ret

    def ejector_type(self):
        ret = self.get_model().type_ejector()
        return self.tools_tuple_to_list(ret)

    def camera_type(self):
        ret = self.get_model().type_camera()
        return self.tools_tuple_to_list(ret)

    def ejector_num(self, e_type):
        ret = self.get_model().ejector_number(e_type)
        return self.tools_tuple_to_list(ret)

    def camera_num(self, c_type):
        ret = self.get_model().camera_number(c_type)
        return self.tools_tuple_to_list(ret)

    def add_ejector(self, **kwargs):
        # 参数表和表字段名一致
        ret = self.get_model().is_exist_ejector(kwargs['type_ejector'], kwargs['number'])
        if not ret:
            # 如果不存在，则insert，首先获取ejector的类型id
            # type_id = self.get_model().
            self.get_model().insert_ejector(**kwargs)
        else:
            self.get_model().update_ejector(**kwargs)

    def add_camera(self, **kwargs):
        ret = self.get_model().is_exist_camera(kwargs['type_camera'], kwargs['number'])
        if not ret:
            # 如果不存在，则insert，首先获取ejector的类型id
            # type_id = self.get_model().
            self.get_model().insert_camera(**kwargs)
        else:
            self.get_model().update_camera(**kwargs)

    def action_delete_all_param_link(self, means_tup: tuple):
        """在导入param数据之前，将该test_mean绑定的param清空"""
        ret = self.get_model().is_exist_element(type_element=means_tup[0], number=means_tup[1:], strategy=2)
        element_id = ret[0][0]
        self.get_model().delete_all_param_link(element_id=element_id, strategy=2)

    def param_file_import(self, means_tup: tuple, path: str):
        """将param数据导入数据库的方法"""
        df = None
        try:
            df = pd.read_csv(filepath_or_buffer=path, sep=',', header=None)
            df[0] = df[0].str.strip()
            df[1] = df[1].str.strip()
        except TypeError:
            pass
        for index, row in df.iterrows():
            self.action_param_link(means_tup=means_tup, param_tup=(row[0], row[1]))

    def get_sensor_type(self):
        uid = self.get_role().get_uid()
        # if (uid,)


if __name__ == '__main__':
    unittest_db = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
    unittest_db.connect()
    print(Controller.tools_tuple_to_list([]))
