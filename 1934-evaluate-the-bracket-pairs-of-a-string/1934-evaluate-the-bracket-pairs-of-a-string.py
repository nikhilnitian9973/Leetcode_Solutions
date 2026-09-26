class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        dic = {}
        for i in range(len(knowledge)):
            
            dic["(" + knowledge[i][0]+")"] = knowledge[i][1]
        new_str = ""
        i = 0
        while i<len(s):
        
            if s[i] == "(":
                j = i   
                while s[i] != ")":
                    i +=1
                new_str += dic.get(s[j:i+1],"?")
                i+=1
                continue
            if s[i] != "(":
                new_str += s[i]
                i +=1
                continue
        return new_str
                
            


