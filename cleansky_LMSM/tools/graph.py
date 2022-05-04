class ElementRightGraph:
    def __init__(self, mat=None):
        # 管理员集合
        self.admin_set = set()
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

        if mat is not None:
            self.update_graph(mat)

    def update_graph(self, data):
        self.mat = data
        for vet in self.mat:
            if vet[1] == 6:
                self.user_set.add(vet[0])
                continue
            if vet[1] == 1:
                self.admin_set.add(vet[0])
            else:
                self.user_set.add(vet[0])
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

    def get_user_right(self, uid):
        """
        查找某个用户节点的所有的邻接element节点
        """
        return self.element_dict[(uid,)]

    def get_token(self, uid: int, element_type_id: int, element_id: int):
        """重要的接口，通过用户id和元素id获取token"""
        token = None
        if uid in self.admin_set:
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