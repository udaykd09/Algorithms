class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        T = [1] * len(s)
        for i in range(1, len(s)):
            T[i] = T[i - 1] - s[i - T[i - 1]:i].index(s[i]) if s[i] in s[i - T[i - 1]:i] else T[i - 1] + 1
        return max(T)

mySol = Solution()
print(mySol.lengthOfLongestSubstring("aaaaaa"))