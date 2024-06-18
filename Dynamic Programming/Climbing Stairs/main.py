class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Recursion solution gives Time Limit Exceeded on LeetCode
        # def recurr(x):
        #     if x == 1:
        #         return 1
        #     elif x == 2:
        #         return 2
        #     else:
        #         return recurr(x - 1) + recurr(x - 2)
        # return recurr(n)
        
        # if n<=2:
        #     return n
        # x= 1
        # y= 2
        # z= 0
        # for i in range(2,n):
        #     z=x+y
        #     x=y
        #     y=z

        # return z
        one = 1
        two = 1
        for i in range(n-1):
            x = one + two
            one, two = x, one
        return one
s = Solution()
n = 44
print(s.climbStairs(n))