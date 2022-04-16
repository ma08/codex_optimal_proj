# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        left_unival = True
        right_unival = True
        
        if root.left:
            if root.val != root.left.val:
                return False
            left_unival = self.isUnivalTree(root.left)
        
        if root.right:
            if root.val != root.right.val:
                return False
            right_unival = self.isUnivalTree(root.right)
        
        return left_unival and right_unival
