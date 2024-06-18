from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # def hammingWeight(n: int) -> int:
        #     res = 0
        #     while n:
        #         n = n & (n - 1)
        #         res += 1
        #     return res
        # res = []
        # for i in range(n + 1):
        #     res.append(hammingWeight(i))
        # return res
        offset = 1
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            if i == offset * 2:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
s = Solution()
n = 4
print(s.countBits(n))