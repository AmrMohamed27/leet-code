from typing import List


class Solution:
    code = ":;"
    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return None
        res = ""
        for i,s in enumerate(strs):
            if i < len(strs) - 1:
                res = res + s + self.code
            else:
                res = res + s
        return res
    def decode(self, s: str) -> List[str]:
        if s is None:
            return []
        if len(s) == 0:
            return [""]
        res = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and j+1 < len(s) and s[j:j+2] != ":;":
                j += 1
            if j == len(s) - 1:
                j += 1
            res.append(s[i:j])
            i = j + 2
        return res

s = Solution()
a = [""]
print(s.encode(a))
print(s.decode(s.encode(a)))