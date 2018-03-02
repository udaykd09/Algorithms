from fractions import Fraction
from math import ceil
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # l=len(nums)
        # r=range(l)
        # t=[x for x in r if (target-nums[x]) in (nums[:x]+nums[x+1:])]
        # return t
        for i, n in enumerate(nums):
            newnums = nums[:i] + nums[i+1:]
            if (target - n) in newnums:
                i2 = newnums.index(target-n)+1
                return [i, i2] if i < i2 else [i2, i]


def twoSumPairs(l1, l2, f):
    s = set()
    ans = []
    for n in l1:
        s.add(f - n)
    print s
    for n in l2:
        if n in s:
            ans.append((n, f-n))
    return ans


#mySol = Solution()
#mySol.twoSum()
print twoSumPairs([1,2,2,5], [5,6,7,8], 9)