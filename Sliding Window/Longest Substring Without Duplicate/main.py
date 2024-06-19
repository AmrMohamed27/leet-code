class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 0:
        #     return 0
        # totalMax = 1
        # l = 0
        # r = l+1
        # while l < r and r < len(s):
        #     if s[r] in "".join(s[l:r]):
        #         l += 1
        #         if l == r:
        #             r += 1
        #     else:
        #         totalMax = max(totalMax, r - l + 1)
        #         r += 1
        # return totalMax
        chars = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
        return res
s = Solution()
a = "dvdf"
b = "pwwkew"
print(s.lengthOfLongestSubstring(a))
print(s.lengthOfLongestSubstring(b))