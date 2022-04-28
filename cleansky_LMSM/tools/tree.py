class Node(object):
    """节点类"""
    def __init__(self, value=None, node_list=None):
        if node_list is None:
            node_list = []
        self.val = value
        self.sub_node_list = node_list


class Tree:
    def __init__(self, root=None):
        self.root = root
        self.height = 0

    def update_tree_by_means(self, mat):
        pass
