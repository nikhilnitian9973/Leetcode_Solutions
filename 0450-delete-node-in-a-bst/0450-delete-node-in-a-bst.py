# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deletion(self,node):
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        else:
            right_node = self.reach_end_right(node.left)
            right_node.right = node.right
            return node.left

    def reach_end_right(self,node):
        while node.right:
            node = node.right
        return node
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        if root.val == key:
            return  self.deletion(root)
        
        curr = root
        while curr:
            if key < curr.val:
                if curr.left and curr.left.val == key:
                    curr.left = self.deletion(curr.left)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right and curr.right.val == key:
                    curr.right = self.deletion(curr.right)
                    break
                else:
                    curr = curr.right
        return root
                
            