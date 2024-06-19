from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res =[]
        nums.sort()
        for i,n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = n + nums[l] + nums[r]
                if sum == 0:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
        return res
s = Solution()
a = [-1,0,1,2,-1,-4]
b = [0,1,1]
c = [0,0,0]
print(s.threeSum(a))
print(s.threeSum(b))
print(s.threeSum(c))