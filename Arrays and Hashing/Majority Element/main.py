class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # freq = {}
        # for n in nums:
        #     freq[n] = freq.get(n, 0) + 1
        #     if freq[n] > len(nums) / 2:
        #         return n
        count = 0
        majority = nums[0]
        for n in nums:
            if n == majority:
                count += 1
            elif count == 0:
                majority = n
                count += 1
            else:
                count -= 1
        return majority
s = Solution()
a = [3,2,3]
b = [2,2,1,1,1,2,2]
print(s.majorityElement(a))
print(s.majorityElement(b))