class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        diff = abs(len(a) - len(b))
        if len(a) > len(b):
            b = ("0" * diff) + b
        elif len(b) > len(a):
            a = ("0" * diff) + a
        res = ""
        carry = 0
        l = len(a)
        for i in range(l-1, -1, -1):
            x = a[i]
            y = b[i]
            if x == "0" and y == "0":
                if carry == 0:
                    res = "0" + res
                else:
                    res = "1" + res
                    carry = 0
            elif (x == "0" and y == "1") or (x == "1" and y == "0"):
                if carry == 0:
                    res = "1" + res
                else:
                    res = "0" + res
                    carry = 1
            else:
                if carry == 0:
                    res = "0" + res
                    carry = 1
                else:
                    res = "1" + res
                    carry = 1
        if carry == 1:
            res = "1" + res
        return res
s = Solution()
a = "1010"
b = "1011"
c = "11"
d = "1"
print(s.addBinary(a, b))
print(s.addBinary(c, d))