import math

class Solution(object):
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def recur(l, r):
            if l > r:
                return -1
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif l > r:
                return -1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            return recur(l, r)
        if len(nums) == 0:
            return -1
        l = 0
        r = len(nums) - 1
        return recur(l, r)
s = Solution()
a = [-1,0,3,5,9,12]
b = 9
print(s.search(a, b))