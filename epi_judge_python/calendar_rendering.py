import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from typing import List
from heapq import heappush, heappop

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A : List[Event]):
    A.sort(key=lambda event : event.start)
    end_times : List[int] = [] # min heap
    max_concurrent = 0
    current_concurrent = 0
    for event in A:
        while end_times and end_times[0] < event.start:
            heappop(end_times)
            current_concurrent -= 1
        heappush(end_times, event.finish)
        current_concurrent += 1
        max_concurrent = max(current_concurrent, max_concurrent)
    return max_concurrent

@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
