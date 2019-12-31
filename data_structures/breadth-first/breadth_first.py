from binary_tree import BinaryTree
from collections import deque

def breadth_first(binary_tree):
    if not binary_tree.root:
        return "This binary tree is empty."
    else:
        breadth_results = []
        breadth_queue = deque()
        breadth_queue.appendleft(binary_tree.root)
        while len(breadth_queue):
            current = breadth_queue.pop()
            breadth_results.append(current.value)
            if current.left_child:
                breadth_queue.appendleft(current.left_child)
            if current.right_child:
                breadth_queue.appendleft(current.right_child)
        return breadth_results
