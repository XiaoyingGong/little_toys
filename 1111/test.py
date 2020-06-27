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
def traversal(root, depth, left_nodes, left_flag):
    if root is None:
        return
    if depth >= 1:

        print("(", left_nodes[depth - 1], " ", root.data, ")")
    if root.lchild:
        left_nodes.append(root.data)

    traversal(root.lchild, depth+1, left_nodes, True)
    if root.rchild is None and len(left_nodes) != 0:
         left_nodes.pop()
    traversal(root.rchild, depth, left_nodes, False)

    return left_nodes


data = ['A', 'B', 'C', 'D', '#', 'E', '#', '#', '#', 'F', 'G', 'H', '#', '#', 'I', '#', 'J','#','#', 'K', 'L',
        '#', '#', '#']
root = create_tree(data)

traversal(root, 0, [], True)
