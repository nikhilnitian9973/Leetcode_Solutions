class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_close_bracket = 0
        count_open_bracket = 0
        for i in range(len(s)):
            if s[i] == '(':
                count_open_bracket +=1
            else:
                if count_open_bracket == 0:
                    count_close_bracket +=1
                    continue
                if count_open_bracket>=1:
                    count_open_bracket -=1
                
        return count_close_bracket + count_open_bracket