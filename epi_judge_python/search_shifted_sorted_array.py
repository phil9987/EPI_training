from test_framework import generic_test


def search_smallest(A):
    start = 0
    end = len(A) - 1
    def f(p,e):
        return A[p] <= A[e]
    while start < end:
        pivot = start + (end - start)//2
        #print("pivot = {}".format(pivot))
        if f(pivot, end):
            end = pivot
        else:
            start = pivot + 1
        #print("start={} end= {}".format(start, end))
    return start


if __name__ == '__main__':
    print(search_smallest([0,2,4,8]))
    print('.')
    print(search_smallest([100, 101, 102, 2, 5]))
    print('..')
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
