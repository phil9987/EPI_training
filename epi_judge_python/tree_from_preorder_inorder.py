from test_framework import generic_test
from binary_tree_node import BinaryTreeNode
from typing import List, Dict


def fill_tree(node: BinaryTreeNode, lookup: Dict[int, int], preorder: List[int], inorder: List[int], start: int, end: int) -> None:
    if preorder:
        head_idx = lookup[node.data]
        left_subtree_size = head_idx - start
        right_subtree_size = end - start - left_subtree_size
        #print("left size = {} right size = {}".format(left_subtree_size, right_subtree_size))
        #print("start = {} end = {} head={}".format(start, end, head_idx))
        #print(preorder)
        if left_subtree_size > 0:
            # insert as left child
            node.left = BinaryTreeNode(preorder[0])
            if left_subtree_size > 1:
                fill_tree(node.left, lookup, preorder[1:left_subtree_size], inorder, start, head_idx - 1)
        if right_subtree_size > 0:
            # insert as right child
            node.right = BinaryTreeNode(preorder[left_subtree_size])
            if right_subtree_size > 1:
                fill_tree(node.right, lookup, preorder[left_subtree_size+1:], inorder, head_idx+1, end)

def binary_tree_from_preorder_inorder(preorder, inorder):
    if not preorder:
        return None
    root = BinaryTreeNode(data=preorder[0])
    lookup = {}
    for i, el in enumerate(inorder):
        lookup[el] = i
    fill_tree(root, lookup, preorder[1:], inorder, 0, len(inorder)-1)
    return root


if __name__ == '__main__':
    inorder= ['F', 'B', 'A', 'E', 'H', 'C', 'D', 'I', 'G']
    preorder =  ['H','B', 'F', 'E', 'A', 'C', 'D', 'G', 'I']
    binary_tree_from_preorder_inorder(preorder, inorder)
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
