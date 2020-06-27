# author: 龚潇颖(Xiaoying Gong)
# date： 2020/5/31 9:52  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
import copy
class LinkNode:
    def __init__(self, index, data, lchild, rchild):
        self.index = index
        self.data = data
        self.lchild = lchild
        self.rchild = rchild
        self.next = None

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

# 构造二叉树的静态链表
def create_link(data):
    head = LinkNode(0, data[0][0], data[1][0], data[2][0])
    head_r = head
    for i in range(1, len(data[0])):
        head.next = LinkNode(i, data[0][i], data[1][i], data[2][i])
        head = head.next
    return head_r

# 遍历静态链表找到相应位置的数据
def search_index(list_head, index):
    while list_head is not None:
        if list_head.index == index:
            return list_head
        list_head = list_head.next
    return None

# 构造二叉树
def create_tree(head):
    if head is None:
        return None
    else:
        root = TreeNode(head.data)
        root.lchild = create_tree(search_index(head, head.lchild))
        root.rchild = create_tree(search_index(head, head.rchild))
        return root
    return root

# 验证，先序遍历我们构造的tree
def pre_traversal(root, result):
    if root is None:
        return
    result.append(root.data)
    pre_traversal(root.lchild, result)
    pre_traversal(root.rchild, result)
    return result

data = [['-', '+', '/', '*', 'A', 'B', 'C'],
        [1, 4, 6, 5, -1, -1, -1],
        [2, 3, -1, -1, -1, -1, -1]]
head = create_link(data)
root = create_tree(head)

result = pre_traversal(root, [])
print(result)
