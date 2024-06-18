from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res
s = Solution()
a = [3,1,2]
print(s.missingNumber(a))