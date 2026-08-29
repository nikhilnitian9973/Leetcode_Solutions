# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        stack = []
        curr = root
        prev_node_val = -2**31-1
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            last= stack.pop()
            curr_node_val = last.val
            if prev_node_val >= curr_node_val:
                return False
            prev_node_val = curr_node_val
            curr = last.right
        return True