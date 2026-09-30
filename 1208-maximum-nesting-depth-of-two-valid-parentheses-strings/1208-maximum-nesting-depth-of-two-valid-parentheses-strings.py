class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        ans = []
        depth = 0
        for i in range(len(seq)):
            if seq[i] == "(":
                depth +=1
                ans.append(depth%2)
            else:
                ans.append(depth%2)
                depth-=1
        return ans
