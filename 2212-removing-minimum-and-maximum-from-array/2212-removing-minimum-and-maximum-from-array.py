class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = min(nums)
        mx = max(nums)
        n = len(nums)
        scenarios = []

        #removing from the front

        scenarios.append(1+max(nums.index(mn),nums.index(mx)))
        #removing from the last
        scenarios.append(n-min(nums.index(mn),nums.index(mx)))
        #removing from the front and last
        scenarios.append(1+min(nums.index(mn),nums.index(mx))+n-max(nums.index(mn),nums.index(mx)))
        return min(scenarios)
        