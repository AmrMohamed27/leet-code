# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root != None:
            temp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)
        return root
s = Solution()
a = TreeNode(1)
b = TreeNode(2)
a.left = b
print(s.invertTree(a))