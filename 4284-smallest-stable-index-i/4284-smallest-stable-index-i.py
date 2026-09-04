class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
       
        for i in range(len(nums)):
            if max(nums[:i+1]) - min(nums[i:len(nums)]) <= k:
                return i
        return -1