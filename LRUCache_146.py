# double linked list 主要是为了降低更新（移动，删除，增加）lru时的复杂度。

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # use len() ?
        self.size = 0
        self.head = DLinkedListNode()
        self.tail = DLinkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            # update lry
            node = self.cache[key]
            self.movetotail(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            # update cache's value
            node = self.cache[key]
            node.value = value
            # update lru
            self.movetotail(node)
        else:
            node = DLinkedListNode(key, value)
            self.addtotail(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                # delete cache
                self.cache.pop(self.head.next.key)
                # delete lru
                self.deletehead()


    def addtotail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def movetotail(self, node):
        # delete node
        node.prev.next = node.next
        node.next.prev = node.prev
        # add to tail
        self.addtotail(node)

    def deletehead(self):
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head


class DLinkedListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
