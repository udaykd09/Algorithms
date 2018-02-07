class Solution:
    strr = []

    def reverse_word(self, f, l):
        print self.strr[f:l]
        for n in range(f, l/2):
            self.strr[n], self.strr[l-n] = self.strr[l-n], self.strr[n]

    def reverse_string_inplace(self):
        self.strr = self.strr[::-1]
        f = 0
        l = 0
        for n, s in enumerate(self.strr):
            if s == " ":
                l = n
                self.reverse_word(f, l)
                f = n + 1
        self.reverse_word(f, len(self.strr))

s = Solution()
s.strr = list("aq dasd fsdg")
s.reverse_string_inplace()
print s.strr