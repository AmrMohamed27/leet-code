class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([char for char in s if char.isalnum()]).lower().strip()
        if len(s) == 0:
            return True
        l = 0
        r = len(s)-1
        while r > l:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
s = Solution()
a = "aa"
b = "race a car"
print(s.isPalindrome(a))
print(s.isPalindrome(b))