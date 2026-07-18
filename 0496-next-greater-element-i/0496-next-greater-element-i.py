class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        
        stack = []
        dic = {}
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<= nums2[i]:
                stack.pop()
            
            if nums2[i] in nums1:
                if stack:
                    dic[nums2[i]] = stack[-1]
                else:
                    dic[nums2[i]] = -1
            stack.append(nums2[i])
        
        
        for i in range(len(nums1)):
            nums1[i] = dic[nums1[i]]

        return nums1
