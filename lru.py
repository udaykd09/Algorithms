import collections


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = collections.OrderedDict
        self.capacity = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.dict:
            return -1
        v = self.dict.pop(key)
        self.dict[key] = v
        return v

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dict.popitem(last=False)
        self.dict[key] = value
