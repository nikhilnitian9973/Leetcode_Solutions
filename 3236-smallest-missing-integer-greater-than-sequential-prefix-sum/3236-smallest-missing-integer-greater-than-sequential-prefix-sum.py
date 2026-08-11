class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        last_index = len(nums) - 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] +1:
                last_index = i-1
                break
        
        a =  sum(nums[:last_index+1])
        if a not in nums:
            return a
        else:
            nums.sort()
            count = 0
            for i in range(len(nums)):
                if a + count == nums[i]:
                    count +=1
            return count +a
        