# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def size_sum(self,node):
        if node == None:
            return 0,0
        left_size,left_sum = self.size_sum(node.left)
        right_size,right_sum = self.size_sum(node.right)

        size = 1+ left_size + right_size
        sum = node.val + left_sum + right_sum
        return size, sum
        
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left_node = self.averageOfSubtree(root.left)
        right_node = self.averageOfSubtree(root.right)

        size,sum = self.size_sum(root)
        avg = sum//size
        if avg == root.val:
            return 1 + left_node + right_node
        else:
            return 0 + left_node + right_node
        