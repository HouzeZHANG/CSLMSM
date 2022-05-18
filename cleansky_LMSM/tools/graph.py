class ElementRightGraph:
    """为设备管理权限专门定制的图数据结构"""
    def __init__(self, mat=None):
        # 管理员集合+包括manager
        self.admin_set = set()
        # manager集合
        self.manager_set = set()
        # 用户集合
        self.user_set = set()
        # 图的原始数据矩阵
        self.mat = []
        # 图的稀疏矩阵
        self.sparse_mat = []
        # 图的元素哈希表，通过用户id查找元素列表
        self.element_dict = dict()
        # 图的用户哈希表，通过元素查找用户列表
        self.person_dict = dict()
        # insect权限，只有manager才可以修改，其会影响诸多widget的显示
        self.insect = None

        if mat is not None:
            self.update_graph(mat)

    def update_graph(self, data):
        """
        当新用户被创建的时候，只在user_set中添加记录，不会更新sparse_mat，也不会更新element_dict和per_dict
        所以在调用element_dict以查询和用户绑定的元素的时候，需要先检查是否存在该键
        """
        self.mat, self.sparse_mat, self.element_dict, self.person_dict = data, [], dict(), dict()
        self.user_set, self.admin_set = set(), set()
        self.insect = None

        for vet in self.mat:
            if vet[1] == 6:
                self.user_set.add(vet[0])
                continue
            if vet[1] == 1:
                # 设置root和初始的manager为manager用户
                self.manager_set.add(vet[0])
                if vet[0] == 2:
                    # 如果是manager用户（不是root），读取其insect列
                    self.insect = vet[-2]
                continue

            # 既不是manager也不是nobody vat[2:]的意思是查找权限element
            for item in vet[2:]:
                if item is not None:
                    self.sparse_mat.append((vet[0], vet[1], vet[2:].index(item), item))
                    if vet[1] == 2:
                        self.admin_set.add(vet[0])
                    else:
                        self.user_set.add(vet[0])

                    if (vet[2:].index(item), item) in self.person_dict.keys():
                        self.person_dict[(vet[2:].index(item), item)].append((vet[0], vet[1]))
                    else:
                        self.person_dict[(vet[2:].index(item), item)] = [(vet[0], vet[1])]

                    if (vet[0],) in self.element_dict.keys():
                        self.element_dict[(vet[0],)].append((vet[1], vet[2:].index(item), item))
                    else:
                        self.element_dict[(vet[0],)] = [(vet[1], vet[2:].index(item), item)]

        self.print_sparse_mat()
        self.print_set()
        self.print_insect()
        self.print_element_dict()
        self.print_person_dict()

    def print_insect(self):
        print("\ninsect:"+str(self.insect))

    def print_set(self):
        print("\nmanager_set")
        print(self.manager_set)

        print("\nadmin_set")
        print(self.admin_set)

        print("\nuser_set")
        print(self.user_set)

    def get_user_right(self, uid):
        """
        查找某个用户节点的所有的邻接element节点
        """
        return self.element_dict[(uid,)]

    def get_token(self, uid: int, element_type_id: int, element_id: int):
        """重要的接口，通过用户id和元素id获取token，

        parameter element_type_id:

        test_mean: 0
        type_coating: 1
        type_detergent: 2
        type_tank: 3
        type_sensor: 4
        type_ejector: 5
        type_camera: 6
        type_test_point: 7
        type_intrinsic_value: 8
        test_team: 9
        insect: 10
        acq_system: 11
        """
        token = None
        if uid in self.manager_set:
            # 如果uid在管理员集合中，将token赋值为1
            token = 1
        else:
            ele_lis = self.element_dict[(uid,)]
            print(ele_lis)
            for item in ele_lis:
                if item[1] == element_type_id and item[2] == element_id:
                    token = item[0]
        return token

    def get_right_tables(self, tup):
        """输入： tup = (element_type_id, element_ref_id)
        查找某个元素节点的全部领接person节点
        这个接口的名字起的不好"""
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

    @staticmethod
    def get_element_info(model_object, element_list: list):
        """element_dict的接口，将element_dict的值转化为字符串"""
        return model_object.tools_get_elements_info(list(element_list))

    def get_certain_element_owner_set(self, tup):
        """传入的是元素tuple, 返回的是拥有这个元素的uid集合"""
        owner_set = set()
        if tup in self.person_dict.keys():
            for item in self.person_dict[tup]:
                owner_set.add(item[0])
        return owner_set

    def get_certain_element_others_set(self, tup):
        """传入元素元组，返回拥有者和其他人的集合"""
        owner_set = self.get_certain_element_owner_set(tup)
        other_set = self.user_set - owner_set
        return other_set

    def print_sparse_mat(self):
        print('\nsparse_mat : uid-role-type-eid\n')
        if not self.sparse_mat:
            return
        for item in self.sparse_mat:
            print(item)
        return

    def print_element_dict(self):
        print('\nele_dict = :{user_id--->(role_id, ele_type, ele_id)}\n')
        for k in self.element_dict.keys():
            print('key: ' + str(k))
            for item in self.element_dict[k]:
                print(item)

    def print_person_dict(self):
        print('\nper_dict = :{(ele_type, ele_id)--->(user_id, role)}\n')
        for k in self.person_dict.keys():
            print('key'+str(k))
            for item in self.person_dict[k]:
                print(item)
