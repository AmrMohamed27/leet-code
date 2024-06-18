# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def createBST():
    # Create nodes
    root = TreeNode(6)
    node2 = TreeNode(2)
    node8 = TreeNode(8)
    node0 = TreeNode(0)
    node4 = TreeNode(4)
    node7 = TreeNode(7)
    node9 = TreeNode(9)
    node3 = TreeNode(3)
    node5 = TreeNode(5)
    # Establish relationships
    root.left = node2
    root.right = node8
    node2.left = node0
    node2.right = node4
    node4.left = node3
    node4.right = node5
    node8.left = node7
    node8.right = node9
    return root

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
s = Solution()
root = createBST()
a = TreeNode(2)
b = TreeNode(8)
print(s.lowestCommonAncestor(root, a,b).val)

