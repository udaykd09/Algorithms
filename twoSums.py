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

mySol = Solution()
mySol.twoSum()