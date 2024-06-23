from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        totalMax = 0
        numSet = set(nums)
        for n in numSet:
            if (n - 1) not in numSet:
                currentMax = 1
                while (n + currentMax) in numSet:
                    currentMax += 1
                totalMax = max(totalMax, currentMax)
        return totalMax
s = Solution()
a = [2,20,4,10,3,4,5,1]
b = [0,3,2,5,4,6,1,1]
print(s.longestConsecutive(a))
print(s.longestConsecutive(b))