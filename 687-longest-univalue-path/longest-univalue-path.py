# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_count=0
        def traverse(node,curr):
            if not node:
                return 0
            left,right=traverse(node.left,node.val),traverse(node.right,node.val)
            self.max_count=max(self.max_count,left+right)
            return 1+max(left,right) if node.val==curr else 0
        

        traverse(root,None)
        return self.max_count