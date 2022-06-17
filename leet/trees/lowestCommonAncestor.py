# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#  Lowest Common Ancestor of a Binary Tree

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.lc = None
        # bubble up true if left or right are found
        def dfs(node):
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            found = node in [p, q]

            if left and right:
                self.lc = node 

            if (left or right) and found:
                self.lc = node 

            return left or right or found
        
        dfs(root)
        
        return self.lc 