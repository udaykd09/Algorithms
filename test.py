import random
import threading
import time
from multiprocessing import Pool

class Solution:
    def gen(self, n=None):
        for i in xrange(n):
            yield i

    def test(self,a=0, l=None):
        l.append(a)
        return l

    def test_rand(self):
        for n in range(7):
            print random.randint(0,5)

    def test_events(self, e):
        while not e.isSet():
            time.sleep(1)
            print"Running, e {} {}".format(e, e.isSet())

def test_multiprocess(x):
    print x*x

def mergeArrays(array_1, array_2):
    final_array = []
    index_1 = 0
    index_2 = 0
    m = len(array_1)
    print array_1, array_2
    while index_1 < m and index_2 < m:
        print index_1, index_2
        if array_1[index_1] < array_2[index_2]:
            final_array.append(array_1[index_1])
            index_1 += 1
        elif array_1[index_1] > array_2[index_2]:
            final_array.append(array_2[index_2])
            index_2 += 1
        else:
            final_array.append(array_1[index_1])
            final_array.append(array_2[index_2])
            index_1 += 1
            index_2 += 1

    if index_1 < m:
        final_array += array_1[index_1:]
    elif index_2 < m:
        final_array += array_2[index_2:]

    return final_array

s = Solution()
#gen = s.gen(10)
#print gen.next(), gen.next()
#l = s.test(l=[10])
#print s.test_rand()
#s.e = threading.Event()
#s.t = threading.Thread(target=s.test_events, args=(s.e,))
#s.t.start()
#time.sleep(10)
#s.e.set()
#s.t.join()
#p = Pool(1)
#p.map(test_multiprocess, [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3])
print mergeArrays([1,2,3,9], [0,0,1,2])