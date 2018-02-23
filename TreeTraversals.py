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

    left_h, right_h = 0, 0
    def getHeight(root):
        if root == None:
            return -1
        if root.left:
            root.left_h = root.left.getHeight()
        if root.right:
            root.right_h = root.right.getHeight()

        return root.left_h + 1 if root.left_h > root.right_h else root.right_h + 1

    def pre_order(self):
        print self.value
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def level_order(self):
        current_level = [self]
        while current_level:
            next_level = list()
            for n in current_level:
                print n.value
                if n.left: next_level.append(n.left)
                if n.right: next_level.append(n.right)
            print
            current_level = next_level

    def level_order_spiral(self):
        stack1, stack2 = [], []
        stack1.append(self)
        while stack1 or stack2:

            while stack1:
                node = stack1.pop()
                print node.value
                if node.right:
                    stack2.append(node.right)
                if node.left:
                    stack2.append(node.left)
            print
            while stack2:
                node = stack2.pop()
                print node.value
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)
            print

    def level_order_q(self):
        queue = []
        queue.append(self)
        sentinel = Node(-1)
        queue.append(sentinel)
        while queue:
            node = queue.pop(0)
            if node == sentinel and len(queue) > 0:
                queue.append(sentinel)
                print
            else: print node.value
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def post_order(root):
        if not root:
            return
        root.left.post_order()
        root.right.post_order()
        print root.value

    def in_order(root):
        if not root:
            return
        root.left.in_order()
        print root.value
        root.right.in_order()

    def clone(root):
        if not root:
            return None
        newRoot = Node(root.value)
        if root.left:
            newRoot.left = root.left.clone()
        if root.right:
            newRoot.right = root.right.clone()
        return newRoot

def create_tree(arr):
    for k, n in enumerate(list(arr)):
        if k == 0:
            root = Node(n)
        else:
            root.insert(n)
    root.printme()
    return root

root = create_tree([0,1,3,2,4,5])
#print(root.getHeight())
#root.level_order()
#root.level_order_q()
#root.level_order_spiral()
#post_order(root)
#root.pre_order()
#in_order(root)
new = root.clone()
new.printme()