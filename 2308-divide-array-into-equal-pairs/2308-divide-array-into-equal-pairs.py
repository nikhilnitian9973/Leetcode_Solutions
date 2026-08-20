class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash = [0]*501

        for i in nums:
            hash[i] +=1
        
        for i in hash:
            if i %2!=0:
                return False
            
        return True