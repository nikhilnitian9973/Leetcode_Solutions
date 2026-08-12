class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi = 0
        left = 0
        right = 0
        my_dic = {}

        while right <len(nums):
            my_dic[nums[right]] = my_dic.get(nums[right],0) +1


            while my_dic[nums[right]] >k:
                my_dic[nums[left]] -= 1
                
                left +=1
                
            maxi = max(maxi,right-left+1)
            right +=1
        return maxi
            