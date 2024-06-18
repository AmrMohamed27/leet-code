class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        thisDict = {}
        for c in s:
            if c in thisDict.keys():
                thisDict[c] += 1
            else:
                thisDict[c] = 1
        for c in t:
            if c not in thisDict.keys():
                return False
            else:
                thisDict[c] -= 1
                if thisDict[c] == 0:
                    thisDict.pop(c)
        if len(thisDict) > 0:
            return False
        else:
            return True
s = Solution()
a = "anagram"
b = "nagaram"
c = "rat"
d = "car"
print(s.isAnagram(a, b))
print(s.isAnagram(c,d))