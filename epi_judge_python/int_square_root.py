from test_framework import generic_test

def square_root(k):
    if k == 0:
        return 0
    start = 0
    end = k+1
    def f(i):
        return i*i > k

    while start < end:
        pivot = start + (end-start)//2
        #print("start={} end={} pivot={}".format(start, end, pivot))
        if not f(pivot):
            start = pivot + 1
        else:
            end = pivot
    return start -1

def square_root_(k):
    if k == 0:
        return 0
    if k <=3:
        return 1
    curr = 2
    while curr * curr < k:
        curr *= 2
    for i in range(curr//2, k):
        if i*i > k:
            return i-1

def square_root__(k):
    if k == 0:
        return 0
    if k <=3:
        return 1
    for i in range(2, k//2+2):
        if i*i > k:
            return i-1


if __name__ == '__main__':
    square_root(2147483647)
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
