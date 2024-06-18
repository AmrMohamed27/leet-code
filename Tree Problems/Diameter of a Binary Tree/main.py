# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        diameter = 0
        def helper(root):
            nonlocal diameter
            if root is None:
                return -1
            left = 1 + helper(root.left)
            right = 1 + helper(root.right)
            diameter = max(diameter, left + right)
            return max(left, right)
        helper(root)
        return diameter
s = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.right = c
a.left = b
b.left = d
b.right = e
print(s.diameterOfBinaryTree(a))