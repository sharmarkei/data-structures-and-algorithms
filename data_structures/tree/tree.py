class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def in_order(self):
        output = []

        def traverse(node):
            if node.left_child:
                traverse(node.left_child)
            output.append(node.value)
            if node.right_child:
                traverse(node.right_child)
        traverse(self.root)
        return output

    def pre_order(self):
        output = []

        def traverse(node):
            output.append(node.value)
            if node.left_child:
                traverse(node.left_child)
            if node.right_child:
                traverse(node.right_child)
        traverse(self.root)
        return output

    def post_order(self):
        output = []

        def traverse(node):
            if node.left_child:
                traverse(node.left_child)
            if node.right_child:
                traverse(node.right_child)
            output.append(node.value)
        traverse(self.root)
        return output


class BinarySearchTree(BinaryTree):

    def add(self, value):
        node = Node(value)
        self.add_node(node)

    def add_node(self, node, current=None):
        if self.root is None:
            self.root = node
        if current is None:
            current = self.root
        if current:
            if current.value > node.value:
                if current.left_child is None:
                    current.left_child = node
                else:
                    self.add_node(node, current.left_child)
            if current.value < node.value:
                if current.right_child is None:
                    current.right_child = node
                else:
                    self.add_node(node, current.right_child)

    def contains(self, value):
        current = self.root
        if self.root is None:
            return False
        while value != current.value:
            if value < current.value and current.left_child:
                current = current.left_child
            elif value > current.value and current.right_child:
                current = current.right_child
            else:
                return False
        return True
