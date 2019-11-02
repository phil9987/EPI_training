from test_framework import generic_test
from typing import List


def merge_two_sorted_arrays(A : List[int], m : int, B : List[int], n : int):
    write_idx = len(A)-1
    ai = m-1
    bi = n-1
    while ai >= 0 and bi >= 0:
        if B[bi] > A[ai]:
            A[write_idx] = B[bi]
            bi -= 1
        else:
            A[write_idx] = A[ai]
            ai -= 1
        write_idx -= 1
    while bi >= 0:
        A[write_idx] = B[bi]
        write_idx -= 1
        bi -= 1

def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
