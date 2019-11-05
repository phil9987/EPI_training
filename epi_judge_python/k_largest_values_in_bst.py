from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils
from collections import deque


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    def find_k_largest_helper(tree: BstNode):
        if tree and len(k_largest_elements) < k:
            find_k_largest_helper(tree.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)
                find_k_largest_helper(tree.left)
    k_largest_elements : List[int] = []
    find_k_largest_helper(tree)

    return k_largest_elements


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
