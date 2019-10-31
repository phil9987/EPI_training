from test_framework import generic_test
from typing import List, Iterator
from heapq import heappush, heappushpop, heappop

def online_median_(sequence : Iterator[int]) -> List[int]:
    smaller_half = [] # max heap
    larger_half = [] # min heap
    res = []
    for el in sequence:
        heappush(smaller_half, -heappushpop(larger_half, el))
        if len(smaller_half) > len(larger_half):
            heappush(larger_half, -heappop(smaller_half))
        res.append(0.5* (-smaller_half[0] + larger_half[0]) if len(smaller_half) == len(larger_half) else larger_half[0])
    return res

def online_median(sequence : Iterator[int]) -> List[int]:
    smaller_half = [] # max heap
    larger_half = [] # min heap
    res = []
    heappush(smaller_half, -next(sequence))
    res.append(-smaller_half[0])
    current_median = res[-1]
    for el in sequence:
        if el > res[-1]:
            heappush(larger_half, el)
        else:
            heappush(smaller_half, -el)
        if len(larger_half) > len(smaller_half) + 1:
            heappush(smaller_half, -heappop(larger_half))
        elif len(smaller_half) > len(larger_half) + 1:
            heappush(larger_half, -heappop(smaller_half))
            
        if len(larger_half) == len(smaller_half):
            res.append(0.5*(-smaller_half[0] + larger_half[0]))
        elif len(larger_half) > len(smaller_half):
            res.append(larger_half[0])
        else:
            res.append(-smaller_half[0])
    return res
            


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    online_median_wrapper([5, 4, 3, 2, 1])
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
