class Solution(object):
    def GCD(self,x,y):
        while x:
            x,y = y%x,x
        return y
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixGCD = []
        max_ele = nums[0]
        for i in range(len(nums)):
            if nums[i] > max_ele:
                max_ele = nums[i]
            prefixGCD.append(self.GCD(max_ele,nums[i]))
        

        prefixGCD.sort()

        left= 0
        right = len(prefixGCD)-1
        sum =  0
        while left <right:
            sum += self.GCD(prefixGCD[left],prefixGCD[right])
            left +=1
            right-=1
        
        return sum


        
    