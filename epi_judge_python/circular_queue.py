from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity):
        self.queue = [0]*capacity
        self.capacity = capacity
        self.head = capacity - 1
        self.tail = capacity - 1
        self._size = 0
        return

    def _double_size(self):
        #print("doubling capacity {} (current_size={})".format(self.capacity, self.size))
        #print("old queue (head={} tail={}): ".format(self.head, self.tail))
        #print(','.join(map(str, self.queue)))
        old_capacity = self.capacity
        self.capacity = self.capacity * 2
        new_queue = [0] * self.capacity
        for i in range(self._size):
            new_queue[-1 - i] = self.queue[(self.capacity + self.tail - i) % old_capacity]
        self.head = self.capacity - self._size - 1
        self.tail = self.capacity - 1
        self.queue = new_queue
        #print("new queue (head={} tail={}): ".format(self.head, self.tail))
        #print(','.join(map(str, self.queue)))

    def enqueue(self, x):
        #print("enqueueing {}".format(x))
        self.queue[self.head] = x
        self._size += 1
        if self._size == self.capacity:
            self._double_size()
        else:
            self.head = (self.capacity + self.head - 1) % self.capacity


    def dequeue(self):
        if self._size > 0:
            res = self.queue[self.tail]
            self._size -= 1
            if self._size == 0:
                self.head = (self.capacity + self.head + 1) % self.capacity
                self.tail = self.head
            else:
                self.tail = (self.capacity + self.tail - 1) % self.capacity
            return res
        else:
            raise LookupError("size of queue is 0")

    def size(self):        
        return self._size


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
