class Node:
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

    def pre_order(self):
        print self.value
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print root.value


def in_order(root):
    if not root:
        return
    in_order(root.left)
    print root.value
    in_order(root.right)

def create_tree(arr):
    for k, n in enumerate(list(arr)):
        if k == 0:
            root = Node(n)
        else:
            root.insert(n)
    root.printme()
    return root

root = create_tree([3,2,1,8,4,6])
#post_order(root)
root.pre_order()
#in_order(root)