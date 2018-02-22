"""
Scope:
Insert K,V
Get value from key
Update recently used key to top
Remove least recently used K,V when out of capacity

Ways:
1. Hashtable with timestamp: Remove last timestamp but needs O(N) to do it
2. LinkedList: Good for most and least used cache but not for get
3. Hashtable with Double LL: Double LL easy for remove
"""


class LinkedListNode:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.nxt = None
        self.pre = None


class LRUCache:
    def __init__(self, capacity=5):
        self.cache = {}
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, k):
        if k in self.cache.keys():
            node = self.cache[k]
            if not node == self.head:
                self.remove(k)
                self.insert(k, node.v)
            return node.v
        else:
            return None

    def insert(self, k, v):
        node = LinkedListNode(k, v)
        if self.size == self.capacity:
            self.remove_tail()
        node.nxt = self.head
        if self.size != 0:
            self.head.pre = node
        self.head = node
        if self.size == 0:
            self.tail = node
        self.cache[k] = node
        self.size += 1

    def remove(self, k):
        node = self.cache[k]
        if node == self.head:
            self.head = node.nxt
            node.nxt.pre = None
        elif node == self.tail:
            self.tail = node.pre
            node.pre.nxt = None
        else:
            node.pre.nxt = node.nxt
            node.nxt.pre = node.pre
        self.cache.pop(k)
        self.size -= 1

    def remove_tail(self):
        node = self.tail
        self.tail = node.pre
        node.pre.nxt = None
        self.cache.pop(node.k)
        self.size -= 1

    def print_cache(self):
        node = self.head
        ans = []
        while node:
            ans.append((node.k, node.v))
            node = node.nxt
        print ans
        print self.head.k, self.tail.k, self.tail.pre.k

lruc = LRUCache()
for k, v in enumerate("abcdef"):
    lruc.insert(k+1, v)
lruc.print_cache()
print lruc.get(2)
lruc.print_cache()