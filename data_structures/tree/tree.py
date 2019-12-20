"""
Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self, node=None, arr=[]):
        node = node or self.root

        arr.append(node.value)

        if node.left:
            self.pre_order(node.left, arr)
        if node.right:
            self.pre_order(node.right, arr)

        return arr
