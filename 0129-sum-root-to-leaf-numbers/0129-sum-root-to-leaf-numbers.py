# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        result = 0
        stack = [(root,str(root.val))]

        while stack:
            node,path_int = stack.pop()

            if not node.left and not node.right:
                result += int(path_int)
            
            if node.left:
                stack.append((node.left,path_int + str(node.left.val)))
            if node.right:
                stack.append((node.right,path_int + str(node.right.val)))

        return result
