'''
Some code was found online geeksforgeeks 
'''


class Node: 
    def __init__(self, data): 
        self.data = data  
        self.left = self.right = None
      
def max(root):

    if (root == None):
        return None

    result = root.data
    left_result = max(root.left)
    right_result = max(root.right)
    if (left_result > result):
        result = left_result
    if (right_result > result):
        result = right_result
    return result


if __name__ == '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    print(max(root))