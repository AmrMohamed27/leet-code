from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
s = Solution()
nums = [1,2,3,1]
nums2 = [1,2,3,4]
print(s.containsDuplicate(nums))
print(s.containsDuplicate(nums2))