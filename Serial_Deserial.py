class Solution:
    mylist = []
    def serialize(self, arr):
        serial = ""
        for n, s in enumerate(list(arr)):
            self.mylist.append(len(s))
            serial += s
        return serial

    def deserialize(self, mystr):
        deserial = []
        for n, nn in enumerate(self.mylist):
            deserial.append(mystr[:nn])
            mystr = mystr[nn:]
        return deserial

mystr = Solution().serialize(["a","","bc,","d"])
arr = Solution().deserialize(mystr)
print(mystr)
print(arr)