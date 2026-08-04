class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        for i in range(min(nums),max(nums)):
            if i not in nums:
                ans.append(i)
        ans.sort()
        return ans
        