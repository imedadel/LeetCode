# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        vals = set()
        def findVals(node):
            if node:
                vals.add(node.val)
                findVals(node.right)
                findVals(node.left)
        findVals(root)
        return len(vals) == 1
