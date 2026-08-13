# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def fun(root):
            if root == None:
                return 0

            left_height = fun(root.left)
            if left_height == -1:
                return -1
                
            right_height = fun(root.right)
            if right_height ==-1:
                return -1
            if abs(left_height - right_height) >1:
                return -1
        
            return 1 + max(left_height,right_height)
        
        return fun(root) != -1

        

    

