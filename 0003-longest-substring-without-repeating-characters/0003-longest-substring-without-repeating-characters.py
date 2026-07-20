class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_dic = {}
        left = 0
        right = 0
        longest_len = 0
        
        while right < len(s):
            if s[right] in my_dic:
                left = max(left,my_dic[s[right]]+1)
            longest_len = max(longest_len,right-left+1)
            my_dic[s[right]] = right
            right +=1
            
        return longest_len

