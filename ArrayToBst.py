class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def createTree(arr, mmin, mmax):
    if mmin > mmax:
        return None
    mmid = (mmin + mmax)//2
    print mmid, arr[mmid]
    node = Node(arr[mmid])
    node.left = createTree(arr, mmin, mmid-1)
    node.right = createTree(arr, mmid+1, mmax)

    return node

node = createTree([0,1,3,4,5,6,7], 0, 6)
print(node)