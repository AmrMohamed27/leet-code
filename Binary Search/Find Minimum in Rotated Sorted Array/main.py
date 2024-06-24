from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 2000
        l = 0
        r = len(nums) - 1
        while r > l:
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        res = min(res, nums[l])
        return res
s = Solution()
a = [3,4,5,6,1,2]
b = [4,5,0,1,2,3]
c = [4,5,6,7]
# results are 1,0,4
print(s.findMin(a))
print(s.findMin(b))
print(s.findMin(c))
