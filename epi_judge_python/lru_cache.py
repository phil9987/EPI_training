from test_framework import generic_test
from test_framework.test_failure import TestFailure

class Book:
    def __init__(self, price, isbn):
        self.price = price
        self.isbn = isbn

class Node:
    def __init__(self, book, prev=None, next=None):
        self.data = book
        self.prev = prev
        self.next = next

class LruCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(None, next = Node(None))
        self.tail = self.head.next
        self.tail.prev = self.head
        self.lookup_ = {}

    def insert_at_front(self, node):
        tmp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = tmp
        tmp.prev = node
    
    def pop_lru_el(self):
        lru_el = self.tail.prev
        self.tail.prev.prev.next = self.tail
        self.tail.prev = lru_el.prev
        return lru_el
    
    def remove_node_from_list(self, node):
        prev = node.prev
        prev.next = node.next
        prev.next.prev = prev

    def bring_node_to_front(self, node):
        if not node.prev is self.head:
            self.remove_node_from_list(node)
            self.insert_at_front(node)


    def lookup(self, isbn):
        if isbn in self.lookup_:
            node = self.lookup_[isbn]
            self.bring_node_to_front(node)
            return node.data.price
        else:
            return -1

    def insert(self, isbn, price):
        node = Node(Book(price, isbn))
        if isbn in self.lookup_:
            # bring entry to front of list
            self.bring_node_to_front(self.lookup_[isbn])
        elif len(self.lookup_) < self.capacity:
            self.lookup_[isbn] = node
            self.insert_at_front(node)
        else:
            # capacity reached, we need to remove the LRU element
            lru_el = self.pop_lru_el()
            del self.lookup_[lru_el.data.isbn]
            del lru_el
            self.insert(isbn, price)

    def erase(self, isbn):
        if isbn in self.lookup_:
            node = self.lookup_[isbn]
            self.remove_node_from_list(node)
            del self.lookup_[isbn]
            del node
            return True
        else:
            return False


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
