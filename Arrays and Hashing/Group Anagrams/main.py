from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute Force Solution
        # group = {}
        # res = []
        # for s in strs:
        #     t = "".join(sorted(s))
        #     if t in group.keys():
        #         group[t].append(s)
        #     else:
        #         group[t] = [s]
        # for key in group.keys():
        #     res.append(group[key])
        # return res
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()
s = Solution()
a = ["act","pots","tops","cat","stop","hat"]
b = ["x"]
print(s.groupAnagrams(a))
print(s.groupAnagrams(b))
