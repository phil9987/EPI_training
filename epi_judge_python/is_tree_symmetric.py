from test_framework import generic_test
from binary_tree_node import BinaryTreeNode


def is_symmetric(tree: BinaryTreeNode) -> bool:
    return not tree or are_symmetric(tree.left, tree.right)

def are_symmetric(node1 : BinaryTreeNode, node2 : BinaryTreeNode) -> bool:
    if not node1 and not node2:
        return True
    elif node1 and node2:
        return node1.data == node2.data and \
            are_symmetric(node1.left, node2.right) and \
            are_symmetric(node1.right, node2.left)
    else:
        # one subtree is empty and the other is not
        return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
