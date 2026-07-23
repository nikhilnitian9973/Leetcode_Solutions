class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def bit_width(n):
            count = 0
            while (1<<count) <= n:
                count +=1
            return count
        n = len(nums)
        if n<=2:
            return n
        else:
            return 1<<bit_width(n)

