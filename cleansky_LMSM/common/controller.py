"""
测试机的显示器分辨率为1366*768
resolution of the test viewer: 1366*768
"""

from abc import ABC, abstractmethod
import pandas as pd

import cleansky_LMSM.common.model as model
import cleansky_LMSM.common.view as view
import cleansky_LMSM.enum_config.config as ccc

import cleansky_LMSM.data_structure.graph as mg
import cleansky_LMSM.data_structure.tree as tree
import cleansky_LMSM.checker.type_checker as type_checker

import time


class Controller(ABC):
    """Controller基类负责实现控制器所共有的接口"""
    right_graph = mg.ElementRightGraph()

    def __init__(self, my_program, my_view, my_model):
        self.__view = my_view
        self.__model = my_model
        self.__program = my_program
        self.__view.set_controller(self)
        self.__model.set_controller(self)

    @abstractmethod
    def window_closed(self):
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
        return self.get_program().role

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
        多元素返回结果，拼装成矩阵，列表类型, 这个函数有过度设计的嫌疑
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

    @staticmethod
    def check_float(number) -> bool:
        return type(number) in [float, int]


class LoginController(Controller):
    def __init__(self, my_program, db_object):
        super(LoginController, self).__init__(my_program=my_program,
                                              my_view=view.LoginView(),
                                              my_model=model.LoginModel(db_object=db_object))

    def window_closed(self):
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
    def __init__(self, my_program, db_object):
        super(MenuController, self).__init__(my_program=my_program,
                                             my_view=view.MenuView(),
                                             my_model=model.MenuModel(db_object=db_object))
        # 告诉action_close_windows这个触发函数，到底是否需要显示login页面
        self.ret_to_login = True

    def window_closed(self):
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

    def action_open_list_of_configuration(self):
        self.ret_to_login = False
        self.get_view().main_window_close()
        self.get_program().run_list_of_configuration()

    def action_open_test_execution(self):
        self.ret_to_login = False
        self.get_view().main_window_close()
        self.get_program().run_test_execution()

    def action_open_exploitation_of_test(self):
        self.ret_to_login = False
        self.get_view().main_window_close()
        self.get_program().run_exploitation_of_test()


class ManagementController(Controller):
    def __init__(self, my_program, db_object):
        super(ManagementController, self).__init__(my_program=my_program,
                                                   my_view=view.ManagementView(),
                                                   my_model=model.ManagementModel(db_object=db_object))

    def window_closed(self):
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

    def action_fill_user_list(self, organisation):
        lis = self.get_model().model_get_list_of_users_by_organisation(organisation)
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
        if uid == 1 or uid == 2:
            return []
        list_of_tup = Controller.right_graph.get_user_right(uid=uid)
        # tup --- (role_id, ele_type, ele_id)
        mat = []
        for item in list_of_tup:
            item = list(item)
            mat.append(self.get_model().tools_get_elements_info(item))
        return mat

    def action_fill_f_name_l_name(self, uname):
        f_name = self.get_model().model_get_fname(uname)
        if f_name:
            f_name = self.tools_tuple_to_list(f_name)

        l_name = self.get_model().model_get_lname(uname)
        if l_name:
            l_name = self.tools_tuple_to_list(l_name)

        return f_name, l_name

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
        lis = Controller.tools_tuple_to_list(self.get_model().model_get_rights())
        uid = self.get_role().get_uid()
        if uid not in self.right_graph.manager_set:
            lis.remove('administrator')
        return lis

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
            others_set = self.right_graph.get_certain_element_others_set((table_number, element_id))

            # 标记是否存在管理员
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
        return mat, lis

    def change_role(self, element_type, ref_tup, person_name, role_str, state: int):
        """对元素权限的修改"""
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

            if element_type == 7:
                # 如果元素是type_test_point，需要拼装创建者和状态信息
                test_point_type = ref_tup[0]
                ref_tup = [test_point_type,
                           self.get_role().get_name(),
                           ccc.TestPointState.CREATED.value]

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
    """策略设计模式"""
    def __init__(self, my_program, db_object):
        super(ItemsToBeTestedController, self).__init__(my_program=my_program,
                                                        my_view=view.ItemsToBeTestedView(),
                                                        my_model=model.ItemsToBeTestedModel(db_object=db_object))
        self.insect_state = InsectState()
        self.tab_state = ccc.TabState.COATING

        # 该成员变量用于使能editable与否
        self.flag_coating_enabled = True
        self.flag_detergent_enabled = True

    def window_closed(self):
        self.get_program().run_menu()

    def action_get_element_type(self):
        """
        根据当前登录用户的身份查找属于他的coating元素，并展示在combobox中
        """
        uid = self.get_role().get_uid()
        if uid in self.right_graph.admin_set or uid in self.right_graph.manager_set:
            # 如果是管理员，则显示全部元素
            return self.tools_tuple_to_list(self.get_model().model_get_element_ref(self.tab_state))
        if (uid,) not in self.right_graph.element_dict.keys():
            # 用户什么权限也没有，什么都不返回（在user_right中只有一行权限为6的记录，这时候用户是不会被添加到字典中的，只会存在在稀疏矩阵中）
            return []
        else:
            # 用户有对某一个设备的权限，其身份不为管理员，此时需要筛选出其对coating设备的记录
            lis = []
            for item in self.right_graph.element_dict[(uid,)]:
                # 策略模式
                column_number = 1 if self.tab_state is ccc.TabState.COATING else 2
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
                    ret.append(self.get_model().model_get_simple_ele(table_name=self.tab_state.value,
                                                                     ele_id=item)[0][0])
                return ret

    def action_get_element_position(self, element_type):
        """根据元素类型表格填充position表格"""
        table_number = 1 if self.tab_state is ccc.TabState.COATING else 2
        element_id = self.get_model().get_ele_id_by_ref(table_number, (element_type,))
        if not element_id:
            # 不存在这种coating type
            return []
        else:
            # 存在这种type
            element_id = element_id[0][0]
            uid = self.get_role().get_uid()
            element_type_id = 1 if self.tab_state is ccc.TabState.COATING else 2
            token = self.right_graph.get_token(uid, element_type_id, element_id)

            if token <= 4:
                self.get_view().question_for_validate(self.tab_state)
            else:
                self.get_view().direct_commit(self.tab_state)

            data = self.get_model().model_get_number(element_type, self.tab_state)
            if not data:
                return []
            else:
                return self.tools_tuple_to_list(data)

    def action_config_by_type_number(self, element_type, number_name):
        # coating_type没填，直接返回
        self.get_view().refresh_value(self.tab_state)
        if element_type == '':
            self.get_view().disable_modify()
            return None, None, None

        # 权限图中必定存在一条边描述该用户和该设备的关系，找出权限
        uid = self.get_role().get_uid()
        element_type_id = 1 if self.tab_state is ccc.TabState.COATING else 2
        token = self.right_graph.get_token(uid, element_type_id, element_type_id)

        if token == 6:
            self.get_view().disable_modify()
            return None, None, None

        # 填充list
        mat = self.get_model().model_get_element_attributes(element_type, number_name, self.tab_state)
        if not mat:
            mat = None

        # 用type coating查找
        chara = self.get_model().model_get_element_char(element_type, self.tab_state)
        if chara:
            chara = self.tools_tuple_to_list(chara)

        unity = self.tools_tuple_to_list(self.get_model().model_get_unity())

        # 判断number是否存在
        # 如果数据被validate了，擦去db transfer， search， create
        is_validate = self.get_model().is_validate(element_type, number_name, self.tab_state)
        if is_validate:
            # 存在这种元素
            is_validate = is_validate[0][0]
            if is_validate or token == 5:
                # validated 或者用户为只读权限
                self.get_view().disable_modify()
            else:
                # not validated
                #     这里可以加一条将三元组设置成不可编辑
                if token == 4:
                    # 只有创建权限的用户
                    self.get_view().direct_commit(self.tab_state)
                    self.get_view().enable_modify()
                else:
                    # valid或者admin或者manager，添加validate询问的窗口
                    self.get_view().question_for_validate(self.tab_state)
                    self.get_view().enable_modify()
        else:
            # 不存在这种元素
            if token <= 4:
                self.get_view().enable_modify()
            else:
                self.get_view().disable_modify()
        return chara, unity, mat

    def action_create_element(self, element_type_name, number, attribute_name, unity, value) -> tuple:
        """
        如果用户点击了，肯定是有权限创建的，所以权限检查不需要做
        其次，将create的粒度降低，如果当前没有position，就算attribute，unity和value被填充了，也不会创建对应的attribute
        必须先点击一次create将position创建好了，再点击一次create才可以insert attribute
        """
        # 获取type_id
        table_name = self.tab_state.value
        element_type_id = self.get_model().model_get_simple_id(table_name=table_name, ele_ref=element_type_name)[0][0]
        element_exist = self.get_model().is_exist_element(element_type_name, number, self.tab_state)

        if not element_exist:
            # 先判断number是否存在，如果不存在，创建number随后直接返回
            self.get_model().model_create_new_element(element_type_id, number, self.tab_state)
            self.get_view().setup_tab_coating_and_detergent()
            return element_type_name + ", " + number + " is created", 0
        else:
            if attribute_name == '':
                return "ERROR\nattribute_name is null", -1
            if unity == '':
                return "ERROR\nUnity is null", -1
            if value == '':
                return "ERROR\nValue is null", -1

            unity_id = self.get_model().model_is_unity_exist(unity)
            if not unity_id:
                # 如果不存在单位，先创建单位
                unity_id = self.get_model().model_create_new_unity(unity)[0][0]
            else:
                unity_id = unity_id[0][0]
            # 更新unity列表
            lis = self.get_model().model_get_unity()
            self.get_view().setup_combobox_unity(items=self.tools_tuple_to_list(lis), strategy=self.tab_state)

            # 如果不存在attribute三元组，创建三元组
            attr_id = self.get_model().model_is_exist_attr(attribute_name, unity_id, value)
            if not attr_id:
                attr_id = self.get_model().model_create_new_attr(attribute_name, unity_id, value)[0][0]
            else:
                attr_id = attr_id[0][0]

            element_id = self.get_model().get_element_id(element_type_name, number, self.tab_state)[0][0]
            is_connected = self.get_model().is_connected_element_and_attribute(element_type_id, attr_id,
                                                                               self.tab_state)
            if not is_connected:
                # 确定是当前coating未绑定的新的attribute，将其绑定
                self.get_model().create_connexion(element_id, attr_id, self.tab_state)
                # 刷新表格
                mat = self.get_model().model_get_element_attributes(element_type_name, number, self.tab_state)
                self.get_view().refresh_table(mat=mat, strategy=self.tab_state)
            return "", 0

    def action_delete_element_attribute(self, element_type_name, number, attribute_name, value, unity):
        # 拿权限
        table_name = self.tab_state.value
        element_id = self.get_model().model_get_simple_id(table_name=table_name, ele_ref=element_type_name)[0][0]
        # 权限图中必定存在一条边描述该用户和该设备的关系，找出权限
        uid = self.get_role().get_uid()
        token = self.right_graph.get_token(uid,
                                           element_type_id=1 if self.tab_state is ccc.TabState.COATING else 2,
                                           element_id=element_id)

        is_validate = self.get_model().is_validate(element_type_name, number, self.tab_state)[0][0]
        if is_validate:
            return

        if token <= 4:
            self.get_model().delete_element_attr(element_type_name, number, attribute_name, value, unity,
                                                 self.tab_state)
            mat = self.get_model().model_get_element_attributes(element_type_name, number, self.tab_state)
            self.get_view().refresh_table(mat=mat, strategy=self.tab_state)

    def action_validate_element(self, element_type_name, number) -> tuple:
        # 查权限
        uid = self.get_role().get_uid()
        if uid in self.right_graph.manager_set:
            token = True
        else:
            table_name = self.tab_state.value
            element_id = self.get_model().model_get_simple_id(table_name=table_name, ele_ref=element_type_name)[0][0]
            token = self.right_graph.get_token(uid,
                                               element_type_id=1 if self.tab_state is ccc.TabState.COATING else 2,
                                               element_id=element_id)
            if token < 4:
                token = True
            else:
                token = False
        if not token:
            return "ERROR\nYou dont have token to validate", -1
        # 检查是否存在这个元素
        ret = self.get_model().is_exist_element(type_element=element_type_name,
                                                number=number,
                                                strategy=self.tab_state)
        if not ret:
            return "Error\nElement not exist", -1
        is_validate = self.get_model().is_validate(type_element=element_type_name,
                                                   number=number)
        if is_validate:
            return "Your element is already validate", -1
        self.get_model().validate_element(element_type_name, number, self.tab_state)
        return "Validation success\n", 0

    def action_get_names_hm(self):
        names = self.tools_tuple_to_list(self.get_model().model_get_insect_names())
        hm = self.tools_tuple_to_list(self.get_model().model_get_hemo())
        return names, hm

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
    
    """下面是关于coating页面upload和download功能的增补"""
    def action_is_element_has_attribute(self, ele_tup: tuple) -> bool:
        mat = self.get_model().model_get_element_attributes(ele_tup[0], ele_tup[1], self.tab_state)
        if not mat:
            return False
        return True

    def action_clone_new_element(self, from_element: tuple, to_element_tup: tuple):
        info, state = self.get_model().clone_attributes_to_new_element(from_element, to_element_tup, self.tab_state)
        return info, state


class ListOfTestMeansController(Controller):
    def __init__(self, my_program, db_object):
        super(ListOfTestMeansController, self).__init__(my_program=my_program,
                                                        my_view=view.ListOfTestMeansView(),
                                                        my_model=model.ListOfTestMeansModel(db_object=db_object))
        # test_mean的树对象
        self.test_mean_tree = tree.Tree()
        # 负责记录test_mean的token <= 4为creator权限
        # It is reasonable to set the initial value to 6,
        # Because None type cannot perform numerical comparisons
        self.test_mean_token, self.test_mean_validate = 6, True
        self.modify_flag = None

        # token for tank
        self.tank_token = 6
        # flag for validate tank
        self.validate_tank = False
        # modify tank flag
        self.modify_flag_tank = False

        # class member variable responsible for recording sensor permissions
        self.sensor_type_token = None

    def window_closed(self):
        self.get_program().run_menu()

    """those interface are related to tab Aircraft/Wind Tunnel"""

    def action_fill_means(self):
        """这里要查权限"""
        uid = self.get_role().get_uid()
        if uid in self.right_graph.admin_set or uid in self.right_graph.manager_set:
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
            self.get_view().enable_modify_test_means(1)
        else:
            self.get_view().disable_modify_test_means(1)

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

        params_table = self.get_model().get_params_by_element((mean_type, mean_name, mean_number),
                                                              strategy=2)
        if not params_table:
            params_table = None

        return chara_list, attr_unity_list, params_combobox, params_table, params_unity, attr

    def action_create_means_attr(self, means, attribute):
        """
        不需要考虑权限问题，如果没有权限，该信号不会被接受
        传入参数tup的格式为：(means_type, means_name, mean_number, attr, unity, value)
        """
        # 类型检查
        if not type_checker.AttributeChecker.type_check(attribute):
            return None, ""

        if not type_checker.TestMeanChecker.type_check(means):
            return None, ""

        state, info = type_checker.AttributeTupleChecker.type_check((attribute[0], attribute[2], attribute[1]))
        if not state:
            return None, info

        # 检查unity是否存在
        unity_id = self.get_model().model_is_unity_exist(attribute[1])
        if not unity_id:
            unity_id = self.get_model().model_create_new_unity(attribute[1])
        unity_id = unity_id[0][0]

        # 检查attribute是否存在
        attr_id = self.get_model().model_is_exist_attr(attribute[0], unity_id, attribute[2])
        if not attr_id:
            attr_id = self.get_model().model_create_new_attr(attribute_name=attribute[0], unity_id=unity_id,
                                                             value=attribute[2])
        attr_id = attr_id[0][0]

        # 获取means id
        means_id = self.get_model().get_element_id(means[0], means[1:], strategy=2)[0][0]

        # 创建链接
        link_id = self.get_model().is_connected_element_and_attribute(element_id=means_id, attr_id=attr_id, strategy=2)
        if not link_id:
            self.get_model().create_connexion(attr_id=attr_id, element_id=means_id, strategy=2)

        return None, ""

    def action_delete_means_attr(self, means_tup: tuple, attr_tup: tuple):
        """解绑attribute"""
        means_id = self.get_model().get_element_id(means_tup[0], (means_tup[1], means_tup[2]), strategy=2)
        if not means_id:
            return
        means_id = means_id[0][0]
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

    def action_param_link(self, means_tup: tuple, param_tup: tuple) -> tuple:
        """创建新的param，param的主键是param.name"""
        mean_id = self.get_model().get_element_id(element_name=means_tup[0], number=means_tup[1:], strategy=2)[0][0]
        if not self.get_model().is_exist_param(param=param_tup):
            """以name为主键进行检查"""
            self.get_model().create_new_param(param=param_tup)
        else:
            """以(name, unity)为主键进行检查"""
            ret = self.get_model().is_param_unity_exist(p_tup=param_tup)
            if not ret:
                return "ERROR\nParam: " + str(param_tup) + "\nParam name exist but unity is not correct", -1
        param_id = self.get_model().is_exist_param(param_tup)[0][0]

        print("\n---")
        print(param_tup)
        print(param_id)

        """到此为止，获取到正确的param_id"""
        if not self.get_model().is_exist_param_link(element_id=mean_id, param_id=param_id, strategy=2):
            """如果不存在link，创建新的link即可返回"""
            print("创建新的link")
            self.get_model().create_param_link(element_id=mean_id, param_id=param_id, strategy=2)
        else:
            print("link已经被创建，continue")
        return "", 0

    def action_get_unity_of_param(self, param_str: str):
        ret = self.get_model().model_get_param_unity(param_str=param_str)
        if not ret:
            return ""
        else:
            return ret[0][0]

    def action_delete_param(self, means_tup: tuple, param_tup: tuple):
        """删除param"""
        if self.test_mean_token <= 4 and not self.test_mean_validate:
            ret = self.get_model().is_exist_element(type_element=means_tup[0], number=means_tup[1:], strategy=2)
            element_id = ret[0][0]
            ret = self.get_model().is_exist_param(param_tup)
            param_id = ret[0][0]

            self.get_model().delete_param_link(element_id=element_id, param_id=param_id, strategy=2)

    def action_delete_all_param_link(self, means_tup: tuple):
        """在导入param数据之前，将该test_mean绑定的param清空"""
        ret = self.get_model().is_exist_element(type_element=means_tup[0], number=means_tup[1:], strategy=2)
        element_id = ret[0][0]
        self.get_model().delete_all_param_link(element_id=element_id, strategy=2)

    def param_file_import(self, means_tup: tuple, path: str):
        """将param数据导入数据库的方法"""
        df = None
        try:
            df = pd.read_csv(filepath_or_buffer=path, sep=',', encoding='unicode_escape', header=0)
        except TypeError:
            pass
        print(df)
        for index, row in df.iterrows():
            if type(row[0]) is not str or type(row[1]) is not str:
                continue
            param_name = row[0].strip()
            unity = row[1].strip()
            info, state = self.action_param_link(means_tup=means_tup, param_tup=(param_name, unity))
            if state != 0:
                return info, state
        return "insert success", 0

    """those interfaces are related to tab ejector and camera"""
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

    """those interfaces are related to tab sensor"""

    def get_sensor_type(self) -> list:
        """sensor type is written in user_right, so this interface required token check"""
        uid = self.get_role().get_uid()
        ret = []

        # only manager have rights to see all the sensors
        if uid in self.right_graph.manager_set:
            return self.tools_tuple_to_list(self.get_model().sensor_type())

        # element_id of sensor = 4
        if (uid,) in self.right_graph.element_dict.keys():
            lis = self.right_graph.element_dict[(uid,)]
            for item in lis:
                if item[1] == 4 and item[0] < 6:
                    # read-only access and above
                    info = self.right_graph.get_element_info(self.get_model(), item)
                    if info is not None:
                        ret.append(info[1])
            return ret
        else:
            return []

    def get_sensor_ref(self, sensor_type: str) -> list:
        """query table ref_sensor for comboBox sensor ref"""
        sensor_type_id = self.get_model().model_get_simple_id(table_name='type_sensor', ele_ref=sensor_type)[0][0]
        self.sensor_type_token = self.right_graph.get_token(uid=self.get_role().get_uid(),
                                                            element_type_id=4,
                                                            element_id=sensor_type_id)
        sensor_ref = self.get_model().sensor_reference(sensor_type=sensor_type)
        return self.tools_tuple_to_list(sensor_ref)

    def filled_sensor_ref(self, sensor_type: str, sensor_ref: str) -> tuple:
        """Fill sensor param, sensor number and sensor table by (sensor type and sensor ref)"""
        # get sensor number
        sensor_num = self.tools_tuple_to_list(self.get_model().sensor_number(sensor_type=sensor_type,
                                                                             sensor_ref=sensor_ref))
        sensor_table = self.get_model().sensor_table(sensor_type=sensor_type,
                                                     sensor_ref=sensor_ref)
        if not sensor_table:
            sensor_table = None
        sensor_param_table = self.get_model().sensor_params_table(sensor_tuple=(sensor_type, sensor_ref))
        if not sensor_param_table:
            sensor_param_table = None
        return sensor_num, sensor_table, sensor_param_table

    def get_sensor_param_combo(self):
        pass

    def get_sensor_unity_combo(self):
        pass

    def action_add_sensor_ref(self, sensor_tuple: tuple):
        """Interface used to create (sensor_type, sensor_ref), there's no need to check the existence of the sensor
        type. According to requirements, users can only create sensor reference though this unique GUI"""
        if self.sensor_type_token >= 5:
            return
        ret = self.get_model().is_exist_sensor_ref(sensor_tup=sensor_tuple)
        if not ret:
            # get sensor_type id
            sensor_type_id = self.get_model().is_exist_sensor_type(sensor_type=sensor_tuple[0])[0][0]
            # create ref
            self.get_model().model_insert_ref_sensor(sensor_type_id=sensor_type_id,
                                                     sensor_ref=sensor_tuple[1])

    def add_sensor(self, sensor_tup: tuple, order_state: ccc.State):
        """sensor_tup : (sensor_type, sensor_ref, sensor_number)
        The order_state parameter is type - safe with an enumeration type, see sensor configuration file for details"""
        ret = self.get_model().is_exist_sensor(sensor_tup=sensor_tup)
        if not ret:
            # create sensor
            self.get_model().model_insert_sensor(sensor_tup=sensor_tup)

            # Maintain table sensor_location
            self.get_model().insert_sensor_location(sensor_tup=sensor_tup, order=order_state,
                                                    loc=ccc.Loc.IN_STORE, vali=True)
        else:
            # update sensor
            pass

    def delete_sensor(self, sensor_tup: tuple) -> tuple:
        # 检查该sensor是否在某个configuration上
        ret = self.get_model().model_is_sensor_in_config(sensor_tup=sensor_tup)
        if ret:
            return -1, "ERROR\nSENSOR: " + str(sensor_tup) + "is in enum_config, you cannot delete it"
        self.get_model().model_delete_sensor(sensor_type=sensor_tup[0],
                                             sensor_ref=sensor_tup[1],
                                             sensor_num=sensor_tup[2])
        self.get_model().insert_sensor_location(sensor_tup=sensor_tup, order=ccc.State.REMOVED,
                                                loc=ccc.Loc.IN_STORE, vali=False)
        return 0, "DELETE SUCCESS"

    def action_sensor_history(self, sensor_tup: tuple):
        if not self.get_model().is_exist_sensor(sensor_tup=sensor_tup):
            return -1

        mat = self.get_model().model_sensor_history(sensor_tup=sensor_tup)

        dic = {'year': [item[0] for item in mat],
               'month': [item[1] for item in mat],
               'day': [item[2] for item in mat],
               'hour': [item[3] for item in mat],
               'minute': [item[4] for item in mat],
               'timezone': [item[5] for item in mat],
               'type': [item[6] for item in mat],
               'ref': [item[7] for item in mat],
               'serial_number': [item[8] for item in mat],
               'order': [item[9] for item in mat],
               'location': [item[10] for item in mat],
               'validation': [item[11] for item in mat]
               }

        my_pd = pd.DataFrame.from_dict(dic, orient='columns')
        file_name = r'.\file_output\sensor_history_' + sensor_tup[0] + '_' + sensor_tup[1] + \
                    '_' + sensor_tup[2] + '_' + '.csv'
        my_pd.to_csv(path_or_buf=file_name, sep=';', index=False)
        return len(mat)

    def action_import_calibration(self, path: str):
        """Import correction error file, check the dataframe line by line, skip if it encounters a non-existent
        element((sensor_type, sensor_ref, sensor_number), (versus_name, versus_symbol), (param_name, param_symbol)).
        Must adhere to the enumeration types specified in the table_field file"""
        # if self.sensor_type_token > 4:
        #     return
        # df = None
        # try:
        #     df = pd.read_csv(filepath_or_buffer=path, sep=';', header=0)
        # except IOError:
        #     pass
        # # for index, row in df.iter_rows():
        # #     print(index)
        # #     self.action_param_link(means_tup=means_tup, param_tup=(row[0], row[1]))
        pass

    def action_param_link_sensor(self, sensor_: str, param_tup: tuple) -> tuple:
        sensor_ref_id = self.get_model().is_exist_sensor_ref(sensor_tup=sensor_)
        if not sensor_ref_id:
            return "ERROR NOT EXIST (SENSOR_TYPE, SENSOR_REF)", -1

        sensor_ref_id = sensor_ref_id[0][0]
        param_id = self.get_model().is_exist_param(param=param_tup)
        if not param_id:
            self.get_model().create_new_param((param_tup[0], param_tup[1], param_tup[2]))
        param_id = self.get_model().is_exist_param(param=param_tup)[0][0]
        self.get_model().create_param_link(element_id=sensor_ref_id, param_id=param_id, strategy=1)

    def action_delete_param_sensor(self, sensor_: tuple, param_tup: tuple):
        # 要判断权限
        sensor_ref_id = self.get_model().is_exist_sensor_ref(sensor_tup=sensor_)[0][0]
        param_id = self.get_model().is_exist_param(param=param_tup)[0][0]
        # sensor_type_id和param_id都是存在的
        self.get_model().delete_param_link(element_id=sensor_ref_id, param_id=param_id, strategy=1)

    def tank_pos_import(self, tank_tup: tuple, path: str) -> tuple:
        ret = self.get_model().is_exist_tank_number(tank_tup=tank_tup)
        if not ret:
            return "TANK NUMBER NOT EXISTS", 1

        if self.tank_token >= 5:
            return "TOKEN INVALID", 1

        try:
            df = pd.read_csv(filepath_or_buffer=path, sep=';', header=0)
        except FileNotFoundError:
            return "FILE NOT FOUND", 1

        # 成功插入的行数
        count = 0

        # 重复的行数
        d_number = 0

        t0 = time.time()
        for index, row in df.iterrows():
            # row = row[1:]
            tc_ret = type_checker.PosOnTankChecker.type_check(row)
            if tc_ret[0]:
                if self.get_model().insert_tank_position(tank_tup=tank_tup,
                                                         element_type=row[0],
                                                         element_pos=row[1],
                                                         coord=(row[2], row[3], row[4]),
                                                         met=((row[5], row[6], row[7]),
                                                              (row[8], row[9], row[10]),
                                                              (row[11], row[12], row[13]))):
                    count = count + 1
                else:
                    d_number = d_number + 1
            else:
                ERROR_NUMBER = tc_ret[1]
                return "ERROR: TYPE INCORRECT\nFAILURE ROW: \n" + str(row) + "\nERROR_NUMBER: " + ERROR_NUMBER, 1

        t1 = time.time()
        delta_time = t1 - t0

        return "INSERT SUCCESS\nTIME USED: " + str(delta_time) + "\nINSERTED ROW COUNT: " + \
               str(count) + "\nDUPLICATED ROW COUNT: " + str(d_number), 0

    def tank_ref(self):
        uid = self.get_role().get_uid()
        if uid in self.right_graph.manager_set:
            return self.tools_tuple_to_list(self.get_model().tank_type())
        ret = []
        if (uid,) in self.right_graph.element_dict.keys():
            ele_lis = self.right_graph.element_dict[(uid,)]
            for item in ele_lis:
                if item[0] <= 5 and item[1] == 3:
                    # 至少有阅读的权限
                    ele_ref = self.get_model().model_get_simple_ele(table_name='type_tank', ele_id=item[2])[0][0]
                    ret.append(ele_ref)
        return ret

    def tank_num(self, tank_ref: str) -> list:
        tank_type_id = self.get_model().is_exist_tank_type(tank_type=tank_ref)[0][0]
        self.tank_token = self.right_graph.get_token(uid=self.get_role().get_uid(),
                                                     element_type_id=3,
                                                     element_id=tank_type_id)
        res = self.get_model().tank_number(tank_type=tank_ref)
        return self.tools_tuple_to_list(res)

    def tank_add_num(self, tank_tup: tuple):
        if self.tank_token >= 5:
            return
        ret = self.get_model().is_exist_tank_number(tank_tup=tank_tup)
        if not ret:
            self.get_model().insert_tank_num(tank_tup=tank_tup)

    def tank_num_edited(self, tank_tup: tuple):
        tank_id = self.get_model().is_exist_tank_number(tank_tup=tank_tup)
        if not tank_id:
            if self.tank_token <= 4:
                self.get_view().enable_modify_tank()
                self.modify_flag_tank = True
            return None

        # check validate
        validate_state = self.get_model().tank_number_validate(tk_tup=tank_tup)[0][0]
        if validate_state or self.tank_token >= 5:
            self.get_view().disable_modify_tank()
            self.modify_flag_tank = False
        else:
            self.get_view().enable_modify_tank()
            self.modify_flag_tank = True

        matrix = self.get_model().tank_pos(tank_type=tank_tup[0], tank_number=tank_tup[1])
        return matrix

    def tank_pos_table(self, tank_tup: tuple) -> list:
        """fill tank position table"""
        ret = self.get_model().tank_pos(tank_type=tank_tup[0], tank_number=tank_tup[1])
        return ret

    def tank_add_pos_table(self, tank_tup: tuple, elem_type: str, element_pos: str, coord: tuple, met: tuple):
        if self.tank_token == 5:
            return
        ret = self.get_model().is_exist_tank_pos(tk_tup=tank_tup, lc=element_pos)
        if not ret:
            # create new pos
            self.get_model().insert_tank_position(tank_tup=tank_tup,
                                                  element_type=elem_type,
                                                  element_pos=element_pos,
                                                  coord=coord,
                                                  met=met)
        else:
            self.get_model().update_tank_pos(pk=ret[0][0],
                                             element_type=elem_type,
                                             element_pos=element_pos,
                                             coord=coord, met=met)

    def tank_del_pos_table(self, tank_tup: tuple, loc: str):
        if self.tank_token >= 5 or self.modify_flag_tank is False:
            return
        ret = self.get_model().is_exist_tank_pos(tk_tup=tank_tup, lc=loc)
        if not ret:
            return
        ret = ret[0][0]
        self.get_model().delete_tk_pos(ret)

    def tank_sensor_coating_type(self) -> list:
        """fill sensor/coating Type comboBox"""
        ret = self.tools_tuple_to_list(self.get_model().sensor_type())
        ret.append('Coating')
        return ret

    def vali_test(self, tk_tup: tuple) -> bool:
        tk_number = self.get_model().is_exist_tank_number(tank_tup=tk_tup)
        if not tk_number:
            return False

        if self.tank_token >= 4:
            return False

        is_vali = self.get_model().tank_number_validate(tk_tup=tk_tup)[0][0]
        if is_vali:
            return False
        return True

    def vali_tank(self, tank_tup: tuple):
        self.get_model().vali_tank(tank_tup)

    def action_get_all_param(self):
        ret = self.get_model().get_all_params()
        return self.tools_tuple_to_list(ret)

    def action_get_all_unity(self):
        ret = self.get_model().model_get_unity()
        return self.tools_tuple_to_list(ret)

    def action_extraire_tank_pos(self, tk_tup: tuple) -> tuple:
        ret = self.get_model().tank_pos(tk_tup[0], tk_tup[1])
        if not ret:
            return "ERROR\nDATA NOT EXISTS", -1
        mat = self.tools_tuple_to_matrix(ret)
        df = pd.DataFrame(mat)
        df.columns = [item.value for item in ccc.FieldTankPos]
        try:
            df.to_csv(path_or_buf=r'.\file_output\tank_config_' + str(tk_tup[0]) + "_"
                                  + str(tk_tup[1]) + '.csv', sep=';', index=False)
        except:
            return "IO ERROR", -1
        return "EXTRAIRE SUCCESS\nTank info: " + str(tk_tup) + "\nROW NUMBER: " + str(len(mat)), 0

    def action_get_tank_location_list(self, tank_tup: tuple, sc_type: str):
        ret = self.get_model().model_tank_pos_by_pos_type(tank_tup, sc_type)
        return self.tools_tuple_to_list(ret)

    def action_get_unity_of_character(self, chara: str):
        ret = self.get_model().model_get_element_attributes(param_str=chara)
        if not ret:
            return ""
        return ret[0][0]


class ListOfConfiguration(Controller):
    def __init__(self, my_program, db_object):
        super(ListOfConfiguration, self).__init__(my_program=my_program,
                                                  my_view=view.ListOfConfigurationView(),
                                                  my_model=model.ListOfConfigurationModel(db_object=db_object))
        self.tank_tree = None
        self.sensor_tree = tree.Tree()

    def window_closed(self):
        self.get_program().run_menu()

    def action_get_tank_type(self):
        ret = self.get_model().tank_type()
        return self.tools_tuple_to_list(ret)

    def action_get_tank_num(self, tank_type: str):
        ret = self.get_model().tank_number(tank_type=tank_type)
        return self.tools_tuple_to_list(ret)

    def action_get_tank_config(self, tank_tup: tuple):
        """用means type和means name查找serial"""
        # root1 = self.tank_tree.search(tank_tup[0])
        # root2 = tree.search_node(root1, tank_tup[1])
        ret = self.get_model().model_get_tk_config_by_tk_tup(tk_tup=tank_tup)
        if ret:
            return [item[0] for item in ret]
        else:
            return []

    def action_fill_config_date(self, tk_config: str) -> str:
        # root1 = self.tank_tree.search(tank_tup[0])
        # root2 = tree.search_node(root1, tank_tup[1])
        # root3 = tree.search_node(root2, tk_config)
        # dt_lis = tree.show_sub_node_info(root3)
        ret = self.get_model().model_get_tk_config_date(tk_config=tk_config)
        if ret:
            return str(ret[0][0])
        else:
            return '----/--/--'

    def action_get_location_nr(self, tank_tup: tuple):
        ret = self.get_model().model_get_tank_loc(tank_tup=tank_tup)
        return self.tools_tuple_to_list(ret)

    def action_get_all_sensor_coating(self):
        mat1 = self.get_model().model_get_sensor_ref_serial_tree()
        mat2 = self.get_model().model_get_coating_tree()

        mat = []
        if not mat1:
            mat = mat2
        elif not mat2:
            mat = mat1
        else:
            for item in mat1:
                mat.append(item)
            for item in mat2:
                mat.append(item)
        self.sensor_tree.initialize_by_mat(mat)

        first_ = tree.show_sub_node_info(self.sensor_tree.root)
        return first_

    def action_tank_config_table(self, tk_config_tup: tuple):
        mat = self.get_model().model_tk_config_table(tk_config_tup=tk_config_tup)
        if not mat:
            return None
        return mat

    def action_get_serial_number(self) -> list:
        ls1 = self.get_model().model_get_all_sensor_num()
        ls1 = self.tools_tuple_to_list(ls1)
        ls2 = self.get_model().model_get_all_coating_number()
        ls2 = self.tools_tuple_to_list(ls2)
        return ls1 + ls2

    def action_is_tank_config_validated(self, tank_config_tup: tuple) -> bool:
        ret = self.get_model().is_tank_config_validated(tank_config_tup=tank_config_tup)
        return ret[0][0]

    def action_delete_tk_config_row(self, tk_config_tup: tuple, loc_str: str) -> int:
        self.get_model().model_delete_tk_config_row(tk_config_tup, loc_str)
        return 0

    def action_check_is_refer(self, tk_config_str: str, loc: str) -> bool:
        scc_id = self.get_model().is_exist_sensor_coating_config_for_tank_config(tk_config_str=tk_config_str,
                                                                                 loc=loc)[0][0]
        ret = self.get_model().is_exist_sensor_coating_config_reffed(sensor_coating_config_id=scc_id)
        if not ret:
            return False
        return True

    def action_validate_tk_config(self, tk_config_tup: tuple):
        self.get_model().model_validate_tk_config(tk_config_tup=tk_config_tup)

    def action_is_exist_tk_config(self, txt):
        ret = self.get_model().is_exist_tank_config(txt)
        if not ret:
            return False
        else:
            return True

    def action_add_row_in_tk_config(self, tk_config_name: str, loc: str) -> tuple:
        ret = self.get_model().is_exist_tank_config(tk_config_name)
        if not ret:
            return -1, "ERROR\nNOT EXIST THIS TANK CONFIG"

        ret = self.get_model().is_exist_sensor_coating_config_for_tank_config(tk_config_str=tk_config_name, loc=loc)
        if ret:
            return -1, "ERROR\nIS EXISTS ALREADY"

        # 正式插入
        self.get_model().insert_sensor_coating_config_for_tk_config()

    def action_clone_tk_config(self, fro: str, to: str) -> tuple:
        # 创建新的config
        new_id, count = self.get_model().model_clone_tank_config(fro, to)
        return new_id, count

    def action_push_add_ref(self, tk_config_tup: tuple, ref_info: tuple) -> tuple:
        # 待更新的元素的信息eid: 元素id, type_id: sensor=0, coating=1
        eid, type_id = self.get_model().model_get_element_id((ref_info[1], ref_info[2]))
        new_element = eid, type_id

        # 你要知道现在这个位置上的是什么器件
        # (element_id, type_id)
        ret = self.get_model().model_find_ele_on_tank(tk_config_tup, ref_info)
        if not ret:
            # 说明该位置上没有器件，直接插入
            self.get_model().model_link_ele_and_tk_pos(tk_config_tup, ref_info, new_element)
        else:
            # 说明该位置上已经有器件了
            ret = ret[0]
            if new_element == ret:
                # 新旧器件是同一个器件，而且插入的位置也是同一个位置，说明可能存在状态update，直接update即可
                self.get_model().model_update_ele_state(ref_info, ret)
            else:
                # 新旧器件不是同一个器件，我们暂且允许在同一个pos上绑定多个器件，插入新行
                # self.get_model().model_link_ele_and_tk_pos(tk_config_tup, ref_info, new_element)
                return -1, "ERROR!\nSomething is already on this position!\n" + str(tk_config_tup)

        return 0, ""

    def action_get_serial_number_by_ref(self, ref: str) -> list:
        # 判断是sensor还是coating
        return self.get_model().model_get_serial_number_for_coating_and_sensor(ref)

    def action_get_ele_ref_by_loc(self, loc, tk_config_tup):
        ret, pot_type = self.get_model().model_get_ref_by_loc(loc=loc, tk_config_tup=tk_config_tup)
        return self.tools_tuple_to_list(ret), pot_type

    def action_create_new_config(self, tk_config_tp: tuple) -> tuple:
        ret = self.get_model().is_exist_tank_config(tank_config=tk_config_tp[2])
        if ret:
            return "ERROR\n" + tk_config_tp[2] + " is exist, you cannot create again!", -1
        self.get_model().model_create_tk_config(tk_config_tup=tk_config_tp)
        return "Congratulation\n" + str(tk_config_tp) + " a new reference is created!", 0


class TestExecutionController(Controller):
    def __init__(self, my_program, db_object):
        super(TestExecutionController, self).__init__(my_program=my_program,
                                                      my_view=view.TestExecutionView(),
                                                      my_model=model.TestExecutionModel
                                                      (db_object=db_object))
        # 构造器创建新树
        self.test_mean_tree = tree.Tree()

        ret = self.get_model().get_air()
        self.airfield_tree = tree.Tree()
        self.airfield_tree.initialize_by_mat(ret)

    def window_closed(self):
        self.get_program().run_menu()

    def action_fill_means(self):
        """这里要查权限"""
        uid = self.get_role().get_uid()
        if uid in self.right_graph.manager_set:
            ret = self.get_model().all_test_means()
        else:
            # 不是管理员
            ret = self.get_model().test_means_str_by_uid(uid=uid)

        self.test_mean_tree.initialize_by_mat(ret)
        # 查找第一层
        first_ = tree.show_sub_node_info(self.test_mean_tree.root)
        return first_

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

    def action_get_test_number(self, mean_tup: tuple) -> list:
        ret = self.get_model().model_get_test_number(mean_tup=mean_tup)
        if not ret:
            return ret
        ret = self.tools_tuple_to_list(ret)
        return ret

    def action_filled_test_number(self, test_tup: tuple) -> list:
        ret = self.get_model().model_get_test_type_state(test_tup=test_tup)
        if not ret:
            return []

        ret = self.tools_tuple_to_matrix(ret)

        # test_type = ret[0][0]
        # test_driver = ret[0][1]

        # 不知道取出来是什么类型
        ret[0][2] = str(ret[0][2])
        ret[0][3] = str(ret[0][3])
        ret[0][4] = str(ret[0][4])

        # tank_config = ret[0][5]
        # acq_config = ret[0][6]
        # came_config = ret[0][7]

        # json string type
        # cond_ini = ret[0][8]
        # need translate json type

        # pilo = ret[0][9]
        # co_pilo = ret[0][10]

        # air_field = ret[0][11]
        # air_run_away = ret[0][12]
        ret[0][13] = str(ret[0][13])
        #
        # arch = ret[0][14]
        ret[0][14] = str(ret[0][14])
        # validate
        ret[0][15] = str(ret[0][15])
        # ...
        return ret

    def get_test_type(self) -> list:
        ret = self.get_model().model_get_test_type()
        return self.tools_tuple_to_list(ret)

    def get_test_driver(self) -> list:
        ret = self.get_model().model_test_driver()
        return self.tools_tuple_to_list(ret)

    def get_pilot(self) -> list:
        ret = self.get_model().model_get_pilot()
        return self.tools_tuple_to_list(ret)

    def get_copilot(self) -> list:
        ret = self.get_model().model_get_copilot()
        return self.tools_tuple_to_list(ret)

    def get_tank_config(self) -> list:
        ret = self.get_model().model_tank_config()
        return self.tools_tuple_to_list(ret)

    def get_came_config(self) -> list:
        ret = self.get_model().model_camera_config()
        return self.tools_tuple_to_list(ret)

    def get_acq_config(self) -> list:
        ret = self.get_model().model_acq_config()
        return self.tools_tuple_to_list(ret)

    def get_airfield_tree(self) -> list:
        first_ = tree.show_sub_node_info(self.airfield_tree.root)
        return first_

    def action_fill_combobox_runway(self, txt: str) -> list:
        root = self.airfield_tree.search(txt)
        if root is None:
            return []
        return tree.show_sub_node_info(root)

    def action_fill_alt(self, airfield: str, runway: str):
        """用means type和means name查找serial"""
        root1 = self.airfield_tree.search(airfield)
        root2 = tree.search_node(root1, runway)
        return tree.show_sub_node_info(root2)

    def get_insect_comb(self) -> list:
        ret = self.get_model().model_get_insect_names()
        return self.tools_tuple_to_list(ret)

    def is_test_exist(self, test_tup: tuple) -> bool:
        ret = self.get_model().model_is_test_exist(test_tup=test_tup)
        if not ret:
            return False
        return True

    def action_import_data_file(self, path, strategy, test_tup: tuple, tank_config) -> str:
        df = None
        try:
            df = pd.read_csv(filepath_or_buffer=path, sep=',', header=0)
        except TypeError:
            pass

        info = None
        row_inserted = None
        duplicated_number = None
        spoiled_sensor_list = None
        t0, t1 = 0, -1

        if strategy is ccc.DataType.F_D:
            t0 = time.time()
            info, row_inserted, duplicated_number = self.insert_airplane_data(df, test_tup)
            t1 = time.time()
        elif strategy is ccc.DataType.S_D:
            t0 = time.time()
            info, row_inserted, duplicated_number, spoiled_sensor_list = self.insert_sensor_data(df,
                                                                                                 test_tup,
                                                                                                 tank_config)
            t1 = time.time()

        if info == "":
            if strategy is ccc.DataType.F_D:
                delta_t = t1 - t0
                info = "INSERT SUCCESS\nTIME USED: " + str(delta_t) + " s \nINSERTED: " + str(
                    row_inserted) + " rows\n" + "duplicated: " + str(duplicated_number) + " rows "
            elif strategy is ccc.DataType.S_D:
                delta_t = t1 - t0
                info = "INSERT SUCCESS\nTIME USED: " + str(delta_t) + \
                       " s \nINSERTED: " + str(row_inserted) + " rows\n" + \
                       "DUPLICATED: " + str(duplicated_number) + " rows\n" + \
                       "SENSOR OUT OF ORDER: " + str(spoiled_sensor_list)

        # 返回状态码
        return info

    @staticmethod
    def get_time_series(df, strategy=1) -> pd.Series:
        if strategy == 1:
            # 明确是第一列为时间序列
            for col in df:
                return df[col]

    def insert_airplane_data(self, df: pd.DataFrame, test_tup: tuple) -> tuple:
        """
        本函数实现了插入飞行器记录的数据的接口

        被插入表结构如下：
                                                      数据表 "public.data_vol"
             栏位      |          类型          | 校对规则 |  可空的  |                 预设
        ---------------+------------------------+----------+----------+--------------------------------------
         id            | integer                |          | not null | nextval('data_vol_id_seq'::regclass)
         id_test       | integer                |          |          |
         id_type_param | integer                |          |          |
         time          | time without time zone |          |          |
         value         | double precision       |          |          |
         validate      | boolean                |          |          |
        索引：
            "data_vol_pkey" PRIMARY KEY, btree (id)
        外部键(FK)限制：
            "data_vol_id_test_fkey" FOREIGN KEY (id_test) REFERENCES test(id)
            "data_vol_id_type_param_fkey" FOREIGN KEY (id_type_param) REFERENCES type_param(id)

        输入信息：
        1. 参数列表：
        df为读取到的数据表，已经由上游转换为Pandas的DataFrame，test_tup是用于定位test的四字段联合主键
        2. DataFrame数据规约：
        第一列为时间戳，第2到n列，每列对应一个单位。header设置为0的时候，导入的DataFrame将自动地使用column来记录单位的名字，
        在遍历DataFrame的过程中会使用strip方法对单位字符串进行修正

        返回信息：
        三元组(info, row_inserted, duplicated_number)：
        info用于显示和用户交互的字符串，row_inserted统计插入的行数，duplicated_number统计重复的行数
        """
        test_id = self.get_model().model_is_test_exist(test_tup=test_tup)
        test_id = test_id[0][0]
        time_series = self.get_time_series(df, strategy=1)
        count = 0
        duplicated_number = 0

        for col in df:
            if col == df.columns[0]:
                continue
            # 如果不是第一列，判断param是否已经在数据库中存在
            param_str = col.strip()
            # bool variable to verify whether this param is in our database
            b = self.get_model().model_is_param_correct(test_tup=test_tup, param_name=param_str)
            if not b:
                self.action_roll_back()
                return "ERROR : <<" + param_str + ">> not exists!", -1, -1

            # 合并两个Series
            my_df = pd.concat([time_series, df[col]], axis=1)

            # 合并dataframe并插入数据库
            for index, row in my_df.iterrows():
                t, val = row[0], row[1]
                if self.check_float(val):
                    if self.get_model().model_insert_data_vol(test_id=test_id, value_tup=(param_str, t, val)):
                        count = count + 1
                    else:
                        duplicated_number = duplicated_number + 1

        return "", count, duplicated_number

    @staticmethod
    def time_to_str(time_ite) -> str:
        return str(time_ite[0]) + ':' + str(time_ite[1]) + ':' + str(time_ite[2]) + '.' + str(time_ite[3])

    def insert_sensor_data(self, df, test_tup: tuple, tank_config: str) -> tuple:
        """
        参数返回：
        row_inserted: type-int meaning-statistic_inserted_row
        duplicated_row: type-int meaning-statistic_duplicated_row
        spoiled_sensor_list: type-list meaning-set_of_out_of_order_sensor
        """
        # DATA_START_INDEX用于记录第一行数据开始的列index
        DATA_START_INDEX = 5
        ROW_INSERT_MAX = None

        row_inserted, duplicated_row, spoiled_sensor_list = 0, 0, list()
        info = ""
        tank_config_id = self.get_model().is_exist_tank_config(tank_config=tank_config)[0][0]
        tank_id = self.get_model().model_get_tank_id_by_tank_config(tank_config)[0][0]

        """
        Index(['16/06/2022', '6:34:41:0', 'A/C'], dtype='object')
        """
        # 首先提前这个dataframe中的数据报头信息，进行信息核对
        test_info = list(df.columns[:3])
        # check configuration name is correct
        # 检查configuration的名字是否匹配
        if test_info[2] != tank_config:
            return "ERROR\nTank configuration not correct", row_inserted, duplicated_row, spoiled_sensor_list

        """
        1, 6, 35, 16, 878
        2, 6, 35, 17, 869
        3, 6, 35, 18, 857
        4, 6, 35, 19, 841
        """
        # time_df = df[df.columns[:4]][1:]
        # 这里从[1:]开始截断是因为时间也有用于存放单位的行，实际时间戳数据是从第三行开始的
        time_df = df[df.columns[4][1:]]

        test_id = self.get_model().model_is_test_exist(test_tup=test_tup)[0][0]

        """Index(['16/06/2022', '6:34:41:0', 'A/C', '  ', '0-0', '0-0.1', '0-0.2', '0-1',
        '0-1.1', '0-1.2', '0-2', '0-2.1', '0-2.2', '0-3', '0-3.1', '0-3.2',
        '0-4', '0-4.1', '0-4.2', '0-5', '0-5.1', '0-5.2', '0-6', '0-6.1',
        '0-6.2', '0-7', '0-7.1', '0-7.2', '0-8', '0-8.1', '0-8.2', '0-9',
        '0-9.1', '0-9.2', '0-10', '0-10.1', '0-10.2', '0-11', '0-11.1',
        '0-11.2'], dtype='object')"""
        loc_list = list(df.columns)
        for i in range(len(loc_list)):
            if loc_list[i].find('.') != -1:
                new_loc = loc_list[i]
                new_loc = new_loc[:loc_list[i].find('.')]
                loc_list[i] = new_loc

        """['16/06/2022', '6:34:41:0', 'A/C', '  ', '0-0', '0-0', '0-0', '0-1', '0-1', 
        '0-1', '0-2', '0-2', '0-2', '0-3', '0-3', '0-3', '0-4', '0-4', '0-4', '0-5', 
        '0-5', '0-5', '0-6', '0-6', '0-6', '0-7', '0-7', '0-7', '0-8', '0-8', '0-8', 
        '0-9', '0-9', '0-9', '0-10', '0-10', '0-10', '0-11', '0-11', '0-11']"""
        # 按照列来索引
        for col in df.columns[DATA_START_INDEX:]:
            # 检查是否存在position
            # check position is exist on this tank
            index = col.find('.')
            if index != -1:
                pos = col[:index]
            else:
                pos = col
            ret = self.get_model().is_exist_tank_pos_by_tank_id(tk_id=tank_id, lc=pos)
            if not ret:
                info = "ERROR\nPosition not exist!\nTank configuration: " + tank_config + "\nPosition name: " + pos
                self.action_roll_back()
                return info, row_inserted, duplicated_row, spoiled_sensor_list
            pos_id = ret[0][0]

            # 检查该position的类型是否是sensor，且该sensor是否存在
            ret = self.get_model().model_get_tank_pos_type_by_loc_and_tk_config(tk_config=tank_config, loc=pos)
            if not ret:
                info = "ERROR\nThere is no sensor on: \nPosition <<" + pos + ">>\nOn tank enum_config <<" + \
                       tank_config + ">>"
                self.action_roll_back()
                return info, row_inserted, duplicated_row, spoiled_sensor_list
            s_id = ret[0][0]

            # 检查数据的单位param是否和传感器reference，也就是ref_sensor绑定
            param = df[col][0]
            tp_id = self.get_model().model_is_param_linked_to_sensor(sensor_id=s_id, param=param)
            if not tp_id:
                info = "ERROR\nParameter: " + param + "not exist for sensor: id(" + str(s_id) + ")"
                self.action_roll_back()
                return info, row_inserted, duplicated_row, spoiled_sensor_list
            param_id = tp_id[0][0]

            # 检查sensor的状态是否是in order，如果不是in order，跳过，说明该传感器无法正常工作
            state = self.get_model().get_sensor_order_by_sensor_id(sensor_id=s_id)[0][0]
            if state != ccc.State.ORDER.value:
                spoiled_sensor_list.append(s_id)
                continue

            # 循环插入
            my_df = df[col][1:]
            my_df = pd.concat([time_df, my_df], axis=1)
            for index, row in my_df.iterrows():
                # time_stamp = str(row[0]) + ":" + str(row[1]) + ":" + str(row[2]) + "." + str(row[3])
                # 修改成第二版之后，直接取第一列的字符串即可，最大精度至秒，而不是微妙
                if ROW_INSERT_MAX is not None:
                    if row_inserted > ROW_INSERT_MAX:
                        return info, row_inserted, duplicated_row, spoiled_sensor_list

                time_stamp = str(row[0])
                v = row[4]
                if pd.isna(v):
                    # 空值处理，直接跳过
                    continue
                id_sensor_coating_config = self.get_model().is_exist_sensor_coating_config(pos_id=pos_id,
                                                                                           sensor_id=s_id,
                                                                                           tk_config_id=tank_config_id)
                # 检查数据项是否已经存在
                ret = self.get_model().is_exist_sensor_data_2(id_test=test_id,
                                                              id_sensor_coating_config=id_sensor_coating_config[0][0],
                                                              id_type_param=param_id,
                                                              time=time_stamp,
                                                              value=v)
                if ret:
                    duplicated_row = duplicated_row + 1
                else:
                    self.get_model().insert_sensor_data_2(id_test=test_id,
                                                          id_sensor_coating_config=id_sensor_coating_config[0][0],
                                                          id_type_param=param_id,
                                                          time=time_stamp,
                                                          value=v)
                    row_inserted = row_inserted + 1
                    print("INSERTED: " + str(row_inserted))

        return info, row_inserted, duplicated_row, spoiled_sensor_list

    def action_extraire_file(self, test_tup: tuple):
        test_str = ""
        for item in test_tup:
            test_str += ('_' + item)

        # sensor data
        mat = self.get_model().get_sensor_data(test_tup)
        if mat:
            dic = {'test_mean_type': [item[0] for item in mat],
                   'test_mean_name': [item[1] for item in mat],
                   'test_mean_number': [item[2] for item in mat],
                   'test_number': [item[3] for item in mat],
                   'sensor_type': [item[4] for item in mat],
                   'sensor_name': [item[5] for item in mat],
                   'sensor_number': [item[6] for item in mat],
                   'time': [str(item[7]) for item in mat],
                   'value': [str(item[8]) for item in mat],
                   'param_name': [item[9] for item in mat],
                   'unity_name': [item[10] for item in mat]
                   }
            my_pd = pd.DataFrame.from_dict(dic, orient='columns')
            try:
                my_pd.to_csv(path_or_buf=r'.\file_output\sensor_data' + test_str + '.csv', sep=';', index=False)
            except:
                pass

        # vol data
        mat = self.get_model().get_vol_data(test_tup)
        if mat:
            dic = {'test_mean_type': [item[0] for item in mat],
                   'test_mean_name': [item[1] for item in mat],
                   'test_mean_number': [item[2] for item in mat],
                   'test_number': [item[3] for item in mat],
                   'time': [str(item[4]) for item in mat],
                   'value': [item[5] for item in mat],
                   'param_name': [item[6] for item in mat],
                   'unity_name': [item[7] for item in mat]
                   }
            my_pd = pd.DataFrame.from_dict(dic, orient='columns')
            try:
                my_pd.to_csv(path_or_buf=r'.\file_output\vol_data' + test_str + '.csv', sep=';', index=False)
            except:
                pass

    def is_test_validated(self, test_tup: tuple) -> bool:
        ret = self.get_model().model_is_test_exist(test_tup=test_tup)
        if not ret:
            return False
        # 检查是否validated
        ret = self.get_model().model_is_test_validated(test_tup=test_tup)[0][0]
        return ret

    def validate_test(self, test_tup: tuple):
        self.get_model().model_validate_test(test_tup)

    def action_update_test(self, test_identification, test_configuration, test_initial_condition) -> bool:
        """能进到这个函数的时候，test一定是存在的"""
        self.get_model().model_update_test(test_identification=test_identification,
                                           test_configuration=test_configuration,
                                           initial_condition=test_initial_condition)
        return True

    def action_create_test(self, test_tup: tuple):
        """创建新的实验"""
        ret = self.is_test_exist(test_tup=test_tup)
        if ret:
            return "ERROR\nTest is exist: " + str(test_tup)

        self.get_model().model_insert_test(test_tup)
        return "SUCCESS\nTest created: " + str(test_tup)

    def fill_test_state_table_ac(self, test_tup: tuple):
        mat = self.get_model().ops_time_begin_time_end_data_vol(test_tup=test_tup)
        if not mat:
            # 一条记录也没有
            return None

        mat = self.tools_tuple_to_matrix(list_tuple=mat)

        not_validate_list = self.get_model().ops_is_data_vol_validate(test_tup=test_tup)
        not_validate_list = self.tools_tuple_to_list(not_validate_list)

        for item in mat:
            if item[0] in not_validate_list:
                item[1] = ccc.DataState.NOT_VALIDATE.value
            else:
                item[1] = ccc.DataState.VALIDATED.value
        return mat

    def fill_test_state_table_sensor_data(self, test_tup: tuple):
        mat = self.get_model().ops_sensor_data_state(test_tup=test_tup)
        if not mat:
            # 一条记录也没有
            return None
        return mat

    def action_get_coating_type_by_tank_config(self, txt):
        ret = self.get_model().model_get_coatings_by_tk_config(txt)
        return self.tools_tuple_to_matrix(ret)

    def is_manager(self) -> bool:
        uid = self.get_role().get_uid()
        if uid in self.right_graph.manager_set:
            return True
        return False


class ExploitationOfTestController(Controller):
    def __init__(self, my_program, db_object):
        super(ExploitationOfTestController, self).__init__(my_program=my_program,
                                                           my_view=view.ExploitationOfTestView(),
                                                           my_model=model.ExploitationOfTestModel(db_object=db_object))

    def window_closed(self):
        self.get_program().run_menu()

    def action_get_test_point_type(self):
        uid = self.get_role().get_uid()
        if uid in self.right_graph.manager_set or uid in self.right_graph.admin_set:
            ret = self.get_model().model_test_point_type()
            return self.tools_tuple_to_list(ret)

        ret_lis = []
        ele_lis = self.right_graph.get_user_right(uid=uid)
        # test point type id is 7
        for item in ele_lis:
            if item[0] <= 5 and item[1] == 7:
                ele_name = self.get_model().model_get_simple_ele(table_name='type_test_point',
                                                                 ele_id=item[2])
                ret_lis.append(ele_name[0][0])
        return sorted(ret_lis)

    def action_get_type_param(self) -> tuple:
        ret = self.get_model().get_all_params()
        # get unity
        unity_lis = self.get_model().model_get_unity()
        unity_lis = self.tools_tuple_to_list(unity_lis)
        return [item[0] for item in ret], unity_lis

    def action_filled_type_test_point(self, txt):
        mat = self.get_model().model_test_point_type_param_table(txt)
        mat = self.tools_tuple_to_matrix(mat)

        if not mat:
            return None
        return mat

    def action_create_new_param(self, t_tp: str, param_tup: tuple):
        ret = self.get_model().is_exist_param(param=param_tup)
        if not ret:
            self.get_model().create_new_param(param=param_tup)
        param_id = self.get_model().is_exist_param(param=param_tup)[0][0]

        tp_id = self.get_model().model_is_exist_tp_type(tp_type=t_tp)[0][0]
        ret = self.get_model().is_exist_param_link(element_id=tp_id, param_id=param_id, strategy=3)
        if not ret:
            self.get_model().create_param_link(element_id=tp_id, param_id=param_id, strategy=3)
            return "SUCCESS\nNEW LINK:\n" + t_tp + " + " + str(param_tup) + " created", 0
        else:
            return "ERROR\nLINK:" + t_tp + " + " + str(param_tup) + " is already created", 1

    def action_delete_param(self, t_tp: str, param_tup: tuple):
        param_id = self.get_model().is_exist_param(param=param_tup)[0][0]
        tp_id = self.get_model().model_is_exist_tp_type(tp_type=t_tp)[0][0]
        self.get_model().delete_param_link(element_id=tp_id, param_id=param_id, strategy=3)

    def action_get_type_state_and_user(self, type_tp: str) -> tuple:
        ret = self.get_model().model_get_info_of_type_test_point(type_tp=type_tp)
        if not ret:
            return 'None', 'None'
        return ret[0][0], ret[0][1]

    def action_is_type_test_point_validated(self, type_tp: str) -> bool:
        ret = self.get_model().model_is_tp_type_validated(tp_type=type_tp)[0][0]
        if ret is ccc.TestPointState.VALIDATED.value:
            return True
        return False

    def action_validate_type_tp(self, type_tp: str):
        self.get_model().model_validate_type_tp(type_tp=type_tp,
                                                user_name=self.get_role().get_name(),
                                                new_state=ccc.TestPointState.VALIDATED.value)

    def action_create_tp(self, tp_tup: tuple) -> tuple:
        uid = self.get_role().get_uid()
        token = ccc.Token.NONE
        if uid in self.right_graph.manager_set:
            token = ccc.Token.MANAGER
        else:
            ele_lis = self.right_graph.get_user_right(uid=uid)
            # test point type id is 7
            ele_id = self.get_model().model_is_exist_tp_type(tp_type=tp_tup[0])[0][0]
            for item in ele_lis:
                if item[2] == ele_id and item[1] == 7:
                    for role in ccc.Token:
                        if role.value == item[0]:
                            token = role

        if token.value > ccc.Token.WRITABLE.value:
            return "ERROR\nYOU CANNOT CREATE BECAUSE YOU HAVEN'T WRITTEN TOKEN", -1

        ret = self.get_model().model_is_exist_test_point(tp_tup=tp_tup)
        if ret:
            return "ERROR\n" + str(tp_tup) + " IS ALREADY EXISTS, SO YOU CANNOT CREATE AGAIN", 1
        self.get_model().model_insert_test_point(tp_tup=tp_tup,
                                                 confid=ccc.ConfiOfTestPoint.NONE.value,
                                                 user_id=self.get_role().get_uid())
        return "SUCCESS\n" + str(tp_tup) + " IS CREATED", 0

    """GUI1.1"""

    def action_filled_type_tp(self, txt):
        mat = self.get_model().model_test_point_mat(type_tp=txt)
        mat = self.tools_tuple_to_matrix(mat)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                mat[i][j] = str(mat[i][j])
        num_lis = self.get_model().model_tp_num(txt)
        num_lis = self.tools_tuple_to_list(num_lis)

        return num_lis, mat

    """Test identification"""

    def action_test_means_type(self):
        ret = self.get_model().model_get_test_mean_type_of_test()
        return self.tools_tuple_to_list(ret)

    def action_fill_combobox_test_mean_type(self, txt):
        ret = self.get_model().model_get_test_mean_name_of_test(txt)
        return self.tools_tuple_to_list(ret)

    def action_fill_serial(self, mean_type, mean_name):
        ret = self.get_model().model_get_test_mean_serial_of_test(test_mean_type=mean_type, test_mean_name=mean_name)
        return self.tools_tuple_to_list(ret)

    def action_get_test_number(self, mean_tup: tuple) -> list:
        ret = self.get_model().model_get_test_number_by_test_mean(test_mean_tup=mean_tup)
        return self.tools_tuple_to_list(ret)

    def action_is_exist_tp(self, tp_tup: tuple):
        ret = self.get_model().model_is_exist_test_point(tp_tup=tp_tup)
        if not ret:
            return False
        else:
            return True

    def action_test_point_is_filled(self, tp_tup: tuple):
        # 主键填值
        ret = self.get_model().model_test_point_filled(tp_tup=tp_tup)
        if not ret:
            return tuple([''] * 10)
        else:
            ls = []
            for i in range(len(ret[0])):
                ls.append(str(ret[0][i]))
            return ls

    def action_test_point_param(self, tp_tup: tuple):
        mat = self.get_model().model_test_point_param_table(tp_tup=tp_tup)
        if not mat:
            return None, None
        ls = [item[0] for item in mat]
        mat = self.tools_tuple_to_matrix(mat)
        for item in mat:
            # if test point value is NULL, we set as string 'None'
            if item[1] is None:
                item[1] = str(item[1])
        return ls, mat

    def action_test_point_cd(self, tp_tup: tuple):
        ret = self.get_model().model_get_test_point_cd_info(tp_tup=tp_tup)
        if not ret:
            return None
        return ret

    def action_update_tp_info(self, tp_tup: tuple, info: tuple) -> tuple:
        # 格式检查

        # update
        self.get_model().model_update_test_point_info(tp_tuple=tp_tup, info=info)
        return "Update success", 0

    def action_c_d_type(self, c_or_d: ccc.TabState):
        ret = self.get_model().model_get_element_type(c_or_d)
        return self.tools_tuple_to_list(ret)

    def action_c_d_num(self, e_type: str, c_or_d: ccc.TabState):
        ret = self.get_model().model_get_element_num(e_type, c_or_d)
        return self.tools_tuple_to_list(ret)

    def action_update_coating_detergent(self, tup: tuple, tp_tup: tuple):
        tp_id = self.get_model().model_is_exist_test_point(tp_tup=tp_tup)
        if not tp_id:
            return "ERROR\nP.E. NOT EXIST", -1
        tp_id = tp_id[0][0]
        self.get_model().model_c_d_update(tup=tup, tp_id=tp_id)
        return "UPDATE SUCCESS", 0

    def action_update_value(self, param_tup: tuple, tp_tup: tuple):
        ret = self.get_model().model_update_param_value(param_tup=param_tup, tp_tup=tp_tup)
        if not ret:
            return 'ERROR\n(PARAM, UNITY) NOT EXISTS', -1
        return "", 0

    def action_get_unity_by_param(self, param: str, tp_type):
        ret = self.get_model().model_get_unity_by_param(param, tp_type)
        return self.tools_tuple_to_list(ret)
