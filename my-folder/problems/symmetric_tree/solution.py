# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        
        r_left = root.left
        r_right = root.right
        
        def comp(l, r):
            if l == None or r == None:
                return l == r
            
            if l.val != r.val:
                return False
            
            return comp(l.left, r.right) and comp(l.right, r.left)
        
        return comp(r_left, r_right)
        
            
