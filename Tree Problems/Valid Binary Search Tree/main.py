# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            if node is None:
                return True
            if not (left < node.val < right):
                return False
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        return dfs(root, -2000, 2000)
s = Solution()
# a = TreeNode(5)
# b = TreeNode(4)
# c = TreeNode(6)
# d = TreeNode(3)
# e = TreeNode(7)
# c.left = d
# c.right = e
# a.left = b
# a.right = c
a = TreeNode(2)
b = TreeNode(1)
c = TreeNode(3)
print(s.isValidBST(a))
