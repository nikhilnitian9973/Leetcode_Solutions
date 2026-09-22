class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        if not arr:
            return []
        
        sorted_unique = sorted(set(arr))          # O(n log n)
        rank = {val: i + 1 for i, val in enumerate(sorted_unique)}  # O(n)
        
        return [rank[num] for num in arr]         # O(n)
