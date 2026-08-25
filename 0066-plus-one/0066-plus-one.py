class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        st = ""
        for (ele) in digits:
            st += str(ele)

        num = int(st) + 1
        lis = []
        for i in str(num):
            lis.append(int(i))
        return lis
        