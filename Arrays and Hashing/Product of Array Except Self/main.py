from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # preProduct = [1] * len(nums)
        # postProduct = [1] * len(nums)
        # res = [1] * len(nums)
        # l = len(nums)
        # for i in range(l):
        #     if i == 0:
        #         continue
        #     else:
        #         preProduct[i] = preProduct[i - 1] * nums[i - 1]
        #         postProduct[l - 1 - i] = postProduct[l - i] * nums[l - i]
        # for i in range(l):
        #     res[i] = preProduct[i] * postProduct[i]
        # return res
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res
s = Solution()
a = [1,2,4,6]
b = [1,0]
print(s.productExceptSelf(a))
print(s.productExceptSelf(b))
