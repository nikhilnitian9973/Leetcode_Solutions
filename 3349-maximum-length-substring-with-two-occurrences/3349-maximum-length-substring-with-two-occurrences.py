class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        count = {}
        max_len = 0

        while right < len(s):
            count[s[right]] = count.get(s[right],0)+1
            while count[s[right]] >2:
                count[s[left]] -= 1
                left +=1
            max_len = max(max_len,right-left+1)
            right +=1
        return max_len

                