from stackClass import Stack
# from queueClass import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.level = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.height = None

    def preorder(self, root_node: Node, preorder_list: Stack = Stack()):
        node = root_node
        if node:
            preorder_list.push(node.data)
            self.preorder(node.left_child, preorder_list)
            self.preorder(node.right_child, preorder_list)
            return preorder_list

    def inorder(self, root_node: Node, inorder_list: Stack = Stack()):
        node = root_node
        if node:
            self.inorder(node.left_child, inorder_list)
            inorder_list.push(node.data)
            self.inorder(node.right_child, inorder_list)
            return inorder_list

    def postorder(self, root_node: Node, postorder_list: Stack = Stack()):
        node = root_node
        if node:
            self.postorder(node.left_child, postorder_list)
            self.postorder(node.right_child, postorder_list)
            postorder_list.push(node.data)
            return postorder_list


if __name__ == '__main__':
    first_tree = BinaryTree()
    n1 = Node('A')
    n2 = Node('B')
    n3 = Node('C')
    n4 = Node('D')
    n5 = Node('E')
    n6 = Node('F')
    n7 = Node('G')
    n8 = Node('H')

    first_tree.root = n1
    n1.right_child = n3
    n1.left_child = n2
    n2.right_child = n5
    n2.left_child = n4
    n4.right_child = n8
    n4.left_child = n7
    n3.right_child = n6

    new_preorder_list = first_tree.preorder(first_tree.root)
    for i in new_preorder_list:
        print(i)

    new_inorder_list = first_tree.inorder(first_tree.root)
    for i in new_inorder_list:
        print(i)

    new_postorder_list = first_tree.postorder(first_tree.root)
    for i in new_postorder_list:
        print(i)
