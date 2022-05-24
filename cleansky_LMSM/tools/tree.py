class Node(object):
    """节点类"""
    def __init__(self, value=None, node_list=None):
        self.sub_node_list = []
        if node_list is not None:
            self.sub_node_list = node_list

        self.val = value

    def __str__(self):
        return "\n[Node]: " + hex(id(self)) + "\nsub_node_list: " + str(self.sub_node_list) + "\nval: " + str(self.val)

    def __del__(self):
        self.sub_node_list = []
        self.val = None


def add_node(root, val):
    # 子节点列表为空表，则直接插入新节点，并返回改新创建的节点作为新的根节点
    if not root.sub_node_list:
        root.sub_node_list.append(Node(value=val))
        return root.sub_node_list[0]

    # 子节点列表不为空表，则遍历子节点列表，查找是否存在value相等的节点，如果有则返回该节点作为新的根
    for item in root.sub_node_list:
        if item.val == val:
            return item

    # 子节点列表中不存在等值节点，新建节点，插入子节点列表，返回该节点
    new_node = Node(value=val)
    root.sub_node_list.append(new_node)
    return new_node


def print_tree(root):
    print("\nMy Tree\n")

    if root is None:
        return

    print(root)

    if not root.sub_node_list:
        return

    for node in root.sub_node_list:
        print_tree(node)


def search_node(root, val):
    """层序查找一棵树中的特定节点"""
    if root is None:
        return None

    if root.val == val:
        # 根节点本身
        return root

    for node in root.sub_node_list:
        # 子节点，该层优先级更高
        if node.val == val:
            return node

    for node in root.sub_node_list:
        # 子节点递归
        ret = search_node(node, val)
        if ret is not None:
            return ret

    # 查不到
    return None


def show_sub_node_info(node):
    """获取某个节点的全部子节点的信息"""
    if node is None or not node.sub_node_list:
        return None

    info_lis = [item.val for item in node.sub_node_list]
    return info_lis


def post_order_del(root):
    if root is None:
        return

    for item in root.sub_node_list:
        post_order_del(item)

    del root


class Tree:
    def __init__(self, matrix=None, root=Node()):
        # 根节点
        self.root = root
        if matrix is not None:
            self.initialize_by_mat(matrix)

        if self.root is None:
            """异常"""
            pass

    def initialize_by_mat(self, matrix):
        """矩阵转化为树"""
        root = self.root
        for row in matrix:
            for col in row:
                root = add_node(root, col)
            root = self.root

    def search(self, val):
        """查找特定节点，假设每一层的元素都是unique的"""
        return search_node(self.root, val)

    def __del__(self):
        post_order_del(self.root)
