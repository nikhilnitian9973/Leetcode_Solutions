class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0 #replace stack
        ans = 0
        i=0
        while i<len(s):
            if s[i] == "(":
                count +=1
                i+=1

            elif i+1<len(s) and s[i] == ")" and s[i+1] == ")":
                if count:

                    count -=1
                    
                else:
                    ans +=1
                i +=2
                continue   
            elif s[i] == ")":
                if count:
                    count -=1
                    ans +=1
                    
                else:
                    ans +=2
                i +=1
                continue
        if count:
            ans += 2*count
        return ans

