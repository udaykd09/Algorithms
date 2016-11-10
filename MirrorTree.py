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
        if not self:
            return self
        if self.left:
            self.left.mirror()
        if self.right:
            self.right.mirror()
        self.swap()
        return self

def create_tree(arr):
    for k, n in enumerate(list(arr)):
        if k == 0:
            root = Node(n)
        else:
            root.insert(n)
    root.printme()
    return root


def isMirror(root1, root2):
    # If both trees are empty, then they are mirror images
    if root1 is None and root2 is None:
        return True

    """ For two trees to be mirror images, the following three
        conditions must be true
        1 - Their root node's key must be same
        2 - left subtree of left tree and right subtree
          of right tree have to be mirror images
        3 - right subtree of left tree and left subtree
           of right tree have to be mirror images
    """
    if (root1 is not None and root2 is not None):
        if root1.key == root2.key:
            return (isMirror(root1.left, root2.right) and
                    isMirror(root1.right, root2.left))

    # If neither of above conditions is true then root1
    # and root2 are not mirror images
    return False


def isSymmetric(root):
    # Check if tree is mirror of itself
    return isMirror(root, root)


root = create_tree([3,2,1,8,9])
root_mirror = root.mirror()
root_mirror.printme()