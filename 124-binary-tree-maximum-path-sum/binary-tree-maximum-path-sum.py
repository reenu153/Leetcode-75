# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum=float('-inf')
        def findMax(root):
            if not root:
                return 0
            left= max(0,findMax(root.left))
            right= max(0,findMax(root.right)) 
            print(self.max_sum, root.val+left+right)
            self.max_sum= max(self.max_sum, root.val+left+right)
            return max(left,right)+root.val
        
        findMax(root)
        return self.max_sum
