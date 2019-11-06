from typing import Iterator

from test_framework import generic_test
import heapq

def find_kth_largest_unknown_length(stream: Iterator[int], k: int) -> int:
    min_heap = []
    for el in stream:
        if len(min_heap) < k:
            heapq.heappush(min_heap, el)
        elif el > min_heap[0]:
            heapq.heappushpop(min_heap, el)
    if len(min_heap) == k:
        return min_heap[0]
    else:
        raise Exception("k larger than stream length, no kth largest element exists")


# Pythonic solution that uses library method but costs O(nlogk) time.
def find_kth_largest_unknown_length_pythonic(stream, k):
    return heapq.nlargest(k, stream)[-1]


def find_kth_largest_unknown_length_wrapper(stream, k):
    return find_kth_largest_unknown_length(iter(stream), k)


if __name__ == '__main__':
    find_kth_largest_unknown_length_wrapper([1,2,3,4,5], 3)
    exit(
        generic_test.generic_test_main(
            'kth_largest_element_in_long_array.py',
            'kth_largest_element_in_long_array.tsv',
            find_kth_largest_unknown_length_wrapper))
