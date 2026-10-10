class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        d  = [0]*100001

        total = 0
        maxi = 0
        k = k1+k2
        for a,b in zip(nums1,nums2):
            x=  abs(a-b)
            d[x]+=1
            maxi = max(maxi,x)
            total +=x
        if total <=k:
            return 0
        
        for i in range(maxi,0,-1):
            
            move = min(k,d[i])
            d[i] -=move
            d[i-1] += move
            k -=move
        sum = 0
        for i in range(maxi+1):
            sum += i*i*d[i]
        return sum