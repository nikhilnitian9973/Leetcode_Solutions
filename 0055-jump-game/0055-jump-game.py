class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxi_index = 0
        for i in range(len(nums)):
            if i > maxi_index:
                return False
            maxi_index = max(maxi_index,i+nums[i])
        return True