class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ans = 0
        i=0
        while i<len(s):
            if s[i] == "(":
                stack.append(s[i])
                i+=1
                
            elif i+1<len(s) and s[i] == ")" and s[i+1] == ")":
                if stack:

                    stack.pop()
                    
                else:
                    ans +=1
                i +=2
                continue   
            elif s[i] == ")":
                if stack:
                    
                    stack.pop()
                    ans +=1
                    
                else:
                    ans +=2
                i +=1
                continue
        if stack:
            ans += 2*len(stack)
        return ans

