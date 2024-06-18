# Definition for a binary tree node.
from typing import Optional

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS:
        # def dfs(root):
        #     if root is None:
        #         return 0
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     return 1 + max(left, right)
        # return dfs(root)
        
        
        # BFS:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        depth = 0
        while queue:
            levelSize = len(queue)
            for i in range(levelSize):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth
s = Solution()
a = TreeNode(0)
b = TreeNode(1)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(4)
a.left = b
a.right = c
c.right = d
c.left = e
print(s.maxDepth(a))