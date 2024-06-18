from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])
            maxSum = max(maxSum, currentSum)
        return maxSum
s = Solution()
a = [-2,1,-3,4,-1,2,1,-5,4]
b = [1]
c = [5,4,-1,7,8]
print(s.maxSubArray(a))
print(s.maxSubArray(b))
print(s.maxSubArray(c))
