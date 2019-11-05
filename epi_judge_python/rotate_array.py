import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def rotate_array(rotate_amount: int, A: List[int]) -> None:
    def reverse(begin: int, end: int) -> None:
        for offset in range(0, (end-begin + 1)//2):
            i = begin + offset
            j = end-offset
            A[i], A[j] = A[j], A[i]
    if not A or rotate_amount == 0:
        return
    rotate_amount = rotate_amount % len(A)
    reverse(0, len(A)-1)
    reverse(0, rotate_amount-1)
    reverse(rotate_amount, len(A)-1)
    return


@enable_executor_hook
def rotate_array_wrapper(executor, A, rotate_amount):
    a_copy = A[:]
    executor.run(functools.partial(rotate_array, rotate_amount, a_copy))
    return a_copy


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    rotate_array(3, arr)
    print(arr)
    exit(
        generic_test.generic_test_main('rotate_array.py', 'rotate_array.tsv',
                                       rotate_array_wrapper))
