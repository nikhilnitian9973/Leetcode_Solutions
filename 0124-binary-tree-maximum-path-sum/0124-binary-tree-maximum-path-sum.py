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
        self.best = float('-inf')

        def fun(node):
            if not node:
                return 0

            left_gain = max(fun(node.left),0)
            right_gain = max(fun(node.right),0)
            
            path_through_node = node.val + left_gain + right_gain

            self.best = max(self.best,path_through_node)

            return node.val + max(left_gain, right_gain)
        
        fun(root)
        return self.best
