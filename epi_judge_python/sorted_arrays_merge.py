from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
    front_elements_heap = []
    iterators = [iter(x) for x in sorted_arrays]
    for i, it in enumerate(iterators):
        first_el = next(it, None)
        if first_el is not None:
            heapq.heappush(front_elements_heap, (first_el, i))
    
    res = []
    while front_elements_heap:
        smallest_el, smallest_arr_idx = heapq.heappop(front_elements_heap)
        res.append(smallest_el)
        next_el = next(iterators[smallest_arr_idx], None)
        if next_el is not None:
            heapq.heappush(front_elements_heap, (next_el, smallest_arr_idx))
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
