from test_framework import generic_test


def is_balanced_binary_tree(tree):
    return is_balanced_req(tree)[0]

def is_balanced_req(tree):
    if not tree:
        return (True, -1)
    left_res = is_balanced_req(tree.left)
    if not left_res[0]:
        return (False, 0)
    right_res = is_balanced_req(tree.right)
    if not right_res[0]:
        return (False, 0)
    if abs(left_res[1] - right_res[1]) <= 1:
        return (True, max(left_res[1], right_res[1]) + 1)
    else:
        return (False, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
