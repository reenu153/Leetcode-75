# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[Optional[TreeNode]]
        """
        hmap={}
        res=[]
        def dfs(node):
            if node is None:
                return '#'
            
            path=','.join([str(node.val), dfs(node.left), dfs(node.right)])

            if path in hmap:
                hmap[path]+=1
                if hmap[path] == 2:
                    res.append(node)
            else:
                hmap[path]=1

            return path

        dfs(root)

        return res


        