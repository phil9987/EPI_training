from test_framework import generic_test
from list_node import ListNode


def reverse_sublist(L, start, finish):
    if start == finish:
        return L
    dummy_head = ListNode(0, L)
    pre_head = dummy_head
    for i in range(start-1):
        pre_head = pre_head.next
    tail = pre_head
    for _ in range(finish - start + 1):
        tail = tail.next
    post_tail = tail.next
    tail.next = None
    new_head, new_tail = reverse(pre_head.next)
    pre_head.next = new_head
    new_tail.next = post_tail
    return dummy_head.next


def reverse(L: ListNode) -> ListNode:
    last_node = L
    prev = None
    curr = L
    while curr:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_
    return prev, last_node


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
