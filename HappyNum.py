class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        arr = map(int, str(n).strip())
        print(arr)
        sum = 0
        new_arr = []
        while sum >= 0:
            for n in arr:
                sum += (n * n)
            print(sum, arr)
            arr = map(int, str(sum).strip())
            if sum == 1:
                return arr[0] == 1
            if sum in new_arr:
                return False
            new_arr.append(sum)
            sum = 0

mySol = Solution()
print(mySol.isHappy(2))