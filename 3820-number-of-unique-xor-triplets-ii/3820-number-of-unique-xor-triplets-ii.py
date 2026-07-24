class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_xor =  2048

        pair_xor = [False]* max_xor
        triple_xor = [False]*max_xor

        for i in range(len(nums)):
            for j in range(len(nums)):
                pair_xor[nums[i]^nums[j]] = True
        
        
        for i in range(max_xor):
            if not pair_xor[i]:
                continue
            for j in nums:
                triple_xor[i^j] = True
        return sum(triple_xor)