class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        mini= 5000
        while low <= high:
            mid = (low+high)//2
            if nums[mid] < nums[high]:
                mini = min(mini,nums[mid])
                high = mid -1
            else:
                mini = min(mini,nums[low])
                low = mid +1
        return mini

        


        
