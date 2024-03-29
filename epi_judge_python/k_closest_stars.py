import functools
import math

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from heapq import heappush, heappushpop, nlargest


class Star:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs):
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)


def find_closest_k_stars(stars, k):
    k_closest = []
    heappush(k_closest, (stars[0].distance(), stars[0]))
    for s in stars[1:]:
        if s.distance() < -k_closest[0][0]:
            if len(k_closest) < k:
                heappush(k_closest, (-s.distance(), s))
            else:
                heappushpop(k_closest, (-s.distance(), s))
    return [s for (_, s) in nlargest(k, k_closest)]


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(
        functools.partial(find_closest_k_stars, iter(stars), k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("k_closest_stars.py",
                                       "k_closest_stars.tsv",
                                       find_closest_k_stars_wrapper, comp))
