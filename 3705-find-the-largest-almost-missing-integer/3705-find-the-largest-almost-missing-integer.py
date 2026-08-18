class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == len(nums):
            return max(nums)
        hash_dic = {}
        if k ==1:
            for i in range(len(nums)):
                hash_dic[nums[i]] = hash_dic.get(nums[i],0)+1
            max_val = -1
            for j in hash_dic:
                if hash_dic[j] == 1 and j>max_val:
                    max_val = j
            return max_val
        first = nums[0]
        last = nums[-1]
        for i in range(len(nums)):
            if first == nums[i]:

                hash_dic[first] = hash_dic.get(first,0)+1
            elif last == nums[i]:
                hash_dic[last] = hash_dic.get(last,0)+1
        
        if hash_dic[first] == 1 and hash_dic[last] == 1:
            
            return max(first,last)
        elif hash_dic[first] == 1:
            return first
        elif hash_dic[last] == 1:
            return last
        else:
            return -1