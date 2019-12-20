from tree import BinaryTree, BinarySearchTree

def test_tree_instance():
    tree = BinaryTree()
    assert tree._root is None

def test_tree_one_member():
    tree = BinarySearchTree()
    tree.add('apples')
    assert tree._root.value == 'apples'

# TODO : test imbalanced
def test_three_members():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    assert tree._root.value == 10
    assert tree._root.left.value == 5
    assert tree._root.right.value == 15


def test_pre_order():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    expected = [10,5,15]
    actual = tree.pre_order()

    assert expected == actual

def test_in_order():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    expected = [5,10, 15]
    actual = tree.in_order()

    assert expected == actual