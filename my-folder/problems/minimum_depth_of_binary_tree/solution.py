# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        depth = 0
        
        if root == None:
            return depth
        
        def deeper(curr, d):
            d += 1
            if curr.left and curr.right:
                return min(deeper(curr.left, d), deeper(curr.right, d))
            elif curr.left:
                return deeper(curr.left, d)
            elif curr.right:
                return deeper(curr.right, d)
            else:
                return d
                
        return deeper(root, depth)
            