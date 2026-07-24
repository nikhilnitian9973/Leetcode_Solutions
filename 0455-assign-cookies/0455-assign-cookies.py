class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        child_pointer = 0
        cookie_pointer = 0
        count = 0
        while child_pointer <len(g) and cookie_pointer<len(s):
            if s[cookie_pointer] >= g[child_pointer] :
                count +=1
                child_pointer +=1
                cookie_pointer +=1
            else:
                cookie_pointer +=1
        return count