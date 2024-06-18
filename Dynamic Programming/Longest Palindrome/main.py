class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return len(s)
        letters = {}
        res = 0
        hasOdd = False
        for c in s:
            letters[c] = letters.get(c, 0) + 1
        for value in letters.values():
            if value % 2 == 0:
                res += value
            elif value % 2 == 1:
                hasOdd = True
                res += (value - 1)
        if hasOdd:
            res += 1
        return res
s = Solution()
a = "AaAaBBBCCCCC"
b = "a"
print(s.longestPalindrome(a))
print(s.longestPalindrome(b))