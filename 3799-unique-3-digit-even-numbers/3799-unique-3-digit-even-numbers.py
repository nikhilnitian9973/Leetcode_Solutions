class Solution(object):
    
        

    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        
        ans = set()
        

        for i in range(len(digits)):
            if digits[i] ==0:
                continue
            
            for j in range(len(digits)):
                if i == j:
                    continue
                for k in range(len(digits)):
                    if j ==k or i == k:
                        continue
                    if digits[k] %2 == 0:
                        ans.add((digits[i],digits[j],digits[k]))
        return len(ans)