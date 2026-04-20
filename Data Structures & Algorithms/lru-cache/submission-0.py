class ListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None  

class LRUCache:        

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity

        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        prv = self.tail.prev
        nxt = self.tail

        node.prev = prv
        node.next = nxt

        prv.next = node
        nxt.prev = node

    def remove(self, node):
        nxt = node.next
        prv = node.prev 

        node.prev.next = nxt
        node.next.prev = prv

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = ListNode(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            self.cache.pop(lru.key)
        
