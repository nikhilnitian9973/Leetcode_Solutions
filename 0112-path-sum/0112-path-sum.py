# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root == None:
            return False
        
        stack = [(root,root.val)]

        while stack:

            node, curr_sum = stack.pop()

            if node.left == None and node.right == None:
                
                if curr_sum == targetSum:
                    return True
                
            if node.left:
                stack.append((node.left,curr_sum+node.left.val))
            if node.right:
                stack.append((node.right,curr_sum+node.right.val))
            
        
        return False

        