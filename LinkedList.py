class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def printll(self):
        root = self.head
        while root:
            print root.value
            root = root.next

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reverse_now(self, curr, prev):
        if not curr.next:
            self.head = curr
            curr.next = prev
            return
        next = curr.next
        curr.next = prev
        self.reverse_now(next, curr)

    def reverse_recursive(self):
        if not self.head:
            return
        self.reverse_now(self.head, None)

    def check_circular(self):
        root = self.head
        root2 = self.head
        while not root:
            root2 = root2.next
            if root.next:
                root = root.next.next
            else: return False
            if root2 is root:
                return True
        return False



ll = LinkedList()

ll.head = Node(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.printll()
"""
ll.reverse()
ll.printll()
ll.reverse_recursive()
ll.printll()
"""
print(ll.check_circular())