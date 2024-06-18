# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p) and (not q):
            return True
        if (not p) or (not q) or (p.val != q.val):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
#         q1 = deque([p])
#         q2 = deque([q])
#         while q1 and q2:
#             node1 = q1.popleft()
#             node2 = q2.popleft()
#             if not node1 and not node2:
#                 continue
#             if not node1 or not node2 or node1.val != node2.val:
#                 return False
#             q1.append(node1.left)
#             q1.append(node1.right)
#             q2.append(node2.left)
#             q2.append(node2.right)
#         return not q1 and not q2
s = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c
x = TreeNode(4)
y = TreeNode(7)
z = TreeNode(4)
zz = TreeNode(7)
x.left = y
z.right = zz
# print(s.isSameTree(a, a))
# print(s.isSameTree(a,b))
print(s.isSameTree(x, z))