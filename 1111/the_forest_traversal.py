# author: 龚潇颖(Xiaoying Gong)
# date： 2020/3/11 17:09
# IDE：PyCharm
# des:
# input(s)：
# output(s)：
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

# 构造二叉树
def create_tree(data):
    if len(data) == 0:
        return
    data_pop = data.pop(0)
    if data_pop == '#':
        return None
    else:
        root = TreeNode(data_pop)
        root.lchild = create_tree(data)
        root.rchild = create_tree(data)
        return root
    return root

# 遍历二叉树
def traversal(root, depth, left_nodes):
    if root is None:
        return
    if depth >= 1:
        print("(", left_nodes[depth - 1], " ", root.data, ")")
    if root.lchild:
        left_nodes.append(root.data)
    traversal(root.lchild, depth+1, left_nodes)
    if root.rchild is None and len(left_nodes) != 0:
        left_nodes.pop()
    traversal(root.rchild, depth, left_nodes)
    return left_nodes


data_1 = ['A', 'B', 'C', 'D', '#', 'E', '#', '#', '#', 'F', 'G', 'H', '#', '#', 'I', '#', 'J','#','#', 'K', 'L',
        '#', '#', '#']
data_2 = ['M', 'N', 'O', '#', 'P', '#', '#', 'Q', '#']
root_1 = create_tree(data_1)
root_2 = create_tree(data_2)
traversal(root_1, 0, [])
traversal(root_2, 0, [])
