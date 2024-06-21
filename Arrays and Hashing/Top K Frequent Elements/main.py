from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq ={}
        res = []
        for i, v in enumerate(nums):
            freq[v] = freq.get(v, 0) + 1
        while k > 0:
            maximum = max(freq, key=freq.get)
            res.append(maximum)
            freq.pop(maximum)
            k -= 1
        return res
s = Solution()
a = [1, 2,2, 3, 3, 3]
k1 = 2
b = [7,7]
k2 = 1
print(s.topKFrequent(a, k1))
print(s.topKFrequent(b, k2))