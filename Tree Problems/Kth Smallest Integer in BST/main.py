# Definition for a binary tree node.
from typing import Optional




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = 0
        def dfs(root):
            nonlocal count
            nonlocal res
            if not root:
                return
            dfs(root.left)
            count += 1
            if count == k:
                res = root.val
                return
            dfs(root.right)
        dfs(root)
        return res
s = Solution()
root5 = TreeNode(15)
root5.left = TreeNode(10)
root5.right = TreeNode(20)
root5.left.left = TreeNode(8)
root5.left.right = TreeNode(12)
root5.right.left = TreeNode(17)
root5.right.right = TreeNode(25)
print(s.kthSmallest(root5, 3))