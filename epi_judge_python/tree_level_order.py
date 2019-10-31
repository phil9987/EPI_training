from test_framework import generic_test


def binary_tree_depth_order_rec(tree):
    res = []
    tree_to_list(tree, 0, res)
    return res

def binary_tree_depth_order(tree):
    res = []
    stack = [(tree, 0)]
    while stack:
        curr, depth = stack.pop()
        if not curr:
            continue
        if len(res) <= depth:
            res.append([])
        res[depth].append(curr.data)
        stack.append((curr.right, depth+1))
        stack.append((curr.left, depth+1))

    return res




def tree_to_list(root, current_level, res):
    if not root:
        return
    if len(res) <= current_level:
        res.append([root.data])
    else:
        res[current_level].append(root.data)
    tree_to_list(root.left, current_level + 1, res)
    tree_to_list(root.right, current_level + 1, res)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
