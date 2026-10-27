class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        a = [["#"]*n for _ in range(m)]
        for i in range(n):
            a[0][i] = "."
        for i in range(m):
            a[i][-1] = "."
        for i in range(m):
            a[i] = "".join(a[i])
        return a
            