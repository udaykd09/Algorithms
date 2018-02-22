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
p = Pool(1)
p.map(test_multiprocess, [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3])