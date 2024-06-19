from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r - l))
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return res
s = Solution()
a = [1,7,2,5,4,7,3,6]
b = [1,2,1]
print(s.maxArea(a))
print(s.maxArea(b))
