# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def inorder(self,root,ele):
        if root.left:
            self.inorder(root.left,ele)
        ele.append(root.val)
        if root.right:
            self.inorder(root.right,ele)

    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        ele=[]
        self.inorder(root,ele)

        return ele[k-1]