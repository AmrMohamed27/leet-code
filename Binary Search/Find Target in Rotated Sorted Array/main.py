from typing import List


class Solution:
    # We find the pivot which the array rotated about using findMin function and then find the target accordingly
    def search(self, nums: List[int], target: int) -> int:
        def findMin(nums: List[int]) -> int:
            res = 2000
            index = -1
            l = 0
            r = len(nums) - 1
            while r > l:
                mid = (l + r) // 2
                res = min(res, nums[mid])
                if res == nums[mid]:
                    index = mid
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            res = min(res, nums[l])
            if res == nums[l]:
                index = l
            return index
        def binarySearch(nums: List[int], target: int)-> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                middle = (left + right)//2
                if nums[middle] < target:
                    left = middle + 1
                elif nums[middle] > target:
                    right = middle -1
                else:
                    return middle
            return -1

        pivot = findMin(nums)
        if pivot != 0:
            if target < nums[0]:
                answer = binarySearch(nums[pivot:], target)
                return pivot + answer if answer != -1 else -1
            else:
                answer = binarySearch(nums[:pivot], target)
                return answer
        else:
            return binarySearch(nums, target)
s = Solution()
a = [1,3]
# b = [4,5,0,1,2,3]
# c = [4,5,6,7]
print(s.search(a, 3))
# print(s.search(b, 2))
# print(s.search(c, 8))
