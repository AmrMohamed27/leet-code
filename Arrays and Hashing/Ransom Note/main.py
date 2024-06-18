class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letters = {}
        for c in magazine:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
        for c in ransomNote:
            if c not in letters:
                return False
            if letters[c] == 1:
                del letters[c]
            elif letters[c] >= 1:
                letters[c] -= 1
            else:
                return False
        return True
s = Solution()
a = "aa"
b = "aab"
print(s.canConstruct(a, b))