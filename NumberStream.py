class Node(object):
    def __init__(self, value):
        self.value = value
        self.count = 1
        self.left = None
        self.right = None

    def printme(self):
        print(self.value, self.count)
        if self.left:
            self.left.printme()
        if self.right:
            self.right.printme()


def insert(root, value):
    if not root:
        root = Node(value)
    elif value == root.value:
        root.count += 1
    elif value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def createTree(arr):
    for k, n in enumerate(list(arr)):
        if k == 0:
            root = insert(None, n)
        else:
            insert(root, n)
    root.printme()

createTree([4, 2, 5, 5, 6, 1, 4])