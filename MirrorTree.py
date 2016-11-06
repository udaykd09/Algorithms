class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def printme(self):
        print(self.value)
        if self.left:
            self.left.printme()
        if self.right:
            self.right.printme()

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.insert(value)
            else:
                self.left = Node(value)

        else:
            if self.right:
                self.right = self.right.insert(value)
            else:
                self.right = Node(value)
        return self

    def swap(self):
        self.left, self.right = self.right, self.left

    def mirror(self):
        self.swap()
        if self.left:
            self.left.mirror()
        if self.right:
            self.right.mirror()
        return self

def create_tree(arr):
    for k, n in enumerate(list(arr)):
        if k == 0:
            root = Node(n)
        else:
            root.insert(n)
    root.printme()
    return root

root = create_tree([3,2,1,8,4,6])
root_mirror = root.mirror()
root_mirror.printme()