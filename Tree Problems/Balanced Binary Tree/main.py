# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if not root:
                return [True, 0]
            l, r = dfs(root.left), dfs(root.right)
            balanced = l[0] and r[0] and abs(l[1] - r[1]) <= 1
            return [balanced, 1 + max(l[1], r[1])]
        return dfs(root)[0]
def FirstTree():
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    node5 = TreeNode(6)
    node6 = TreeNode(8)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node3.left = node6
    return root
def SecondTree():
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(4)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node3.left = node5
    node3.right = node6
    return root
s = Solution()
root1 = FirstTree()
root2 = SecondTree()
print(s.isBalanced(root1))
print(s.isBalanced(root2))
# def printTree(root):
#     print(root.val)
#     if root.left:
#         printTree(root.left)
#     if root.right:
#         printTree(root.right)
# printTree(root1)