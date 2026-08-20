# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        # if root == None:
        #     return []

        # result = []
        # stack = [(root,str(root.val))]


        # while stack:

        #     node,path = stack.pop()

        #     if node.left == None and node.right == None:

        #         result.append(path)
        #     if node.left:
        #         stack.append((node.left,path + "->" + str(node.left.val)))
        #     if node.right:
        #         stack.append((node.right,path + "->" + str(node.right.val)))
        # return result


        def bTP(root,path):
            if root == None:
                return
            
            path += str(root.val)


            if not root.left and not root.right:
                result.append(path)
                return
            bTP(root.left,path + "->")
            bTP(root.right,path+ "->")
        result = []
        bTP(root,"")
        return result
        