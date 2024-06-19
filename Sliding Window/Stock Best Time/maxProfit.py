class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maximum = 0
        l = 0
        for r in range(l+1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                maximum = max(maximum, prices[r] - prices[l])
        return maximum
s = Solution()
a = [7,1,5,3,6,4]
b = [7,6,4,3,1]
print(s.maxProfit(a))
print(s.maxProfit(b))