import sys

class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.Heap = []
        self.Heap.append(-sys.maxint)

    @staticmethod
    def left(pos):
        return pos*2

    @staticmethod
    def right(pos):
        return (pos*2) + 1

    @staticmethod
    def parent(pos):
        return pos//2

    def isLeaf(self, pos):
        h = self.Heap
        if len(h)-1 >= pos >= len(h)/2:
            return True
        return False

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def insert(self, value):
        h = self.Heap
        h.append(value)
        self.inv_heapify()

    def inv_heapify(self):
        h = self.Heap
        current = len(h)-1
        while h[current] < h[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def print_heap(self):
        h = self.Heap
        for n in range(1, (len(h)//2)):
            print "parent: %s, left: %s, right: %s"%(h[n], h[2*n], h[(2*n)+1])

    def remove(self):
        h = self.Heap
        x = h.pop(1)
        self.min_heapify(1)
        return x

    def min_heapify(self, pos):
        h = self.Heap
        if not self.isLeaf(pos):
            if h[pos] > h[self.left(pos)] or h[pos] > h[self.right(pos)]:
                if h[self.left(pos)] < h[self.right(pos)]:
                    self.swap(pos, self.left(pos))
                    self.min_heapify(self.left(pos))
                else:
                    self.swap(pos, self.right(pos))
                    self.min_heapify(self.right(pos))

myHeap = MinHeap(5)
myHeap.insert(5)
myHeap.insert(3)
myHeap.insert(2)
myHeap.insert(1)
#myHeap.remove()
myHeap.print_heap()