from test_framework import generic_test
from typing import List, Generator
from heapq import heappush, heappushpop, nsmallest


def sort_approximately_sorted_array(sequence : List[int], k : int) -> List[int]:
    minheap = []
    res = []
    while len(minheap) < k:
        heappush(minheap, next(sequence))
    for el in sequence:
        next_el = heappushpop(minheap, el)
        res.append(next_el)
    res += nsmallest(k, minheap)
    return res

def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    seq = [1, -11, 2, -2, -19, 4, -9, 1, 10, -12, 6, -19, 9, -5, 0, 5, -4, 13, 19, 19, 11]
    k = 17
    sort_approximately_sorted_array_wrapper(seq, k)
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
