class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        min_odd = float('inf')
        min_even = float('inf')

        for i in nums1:
            if i %2 == 0:
                min_even = min(min_even,i)
            else:
                min_odd = min(min_odd,i)
        if min_odd == float('inf'):
            return True
        return min_odd < min_even