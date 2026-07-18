class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = min(nums)
        y = max(nums)

        while x:
            x,y = y%x,x
        return y