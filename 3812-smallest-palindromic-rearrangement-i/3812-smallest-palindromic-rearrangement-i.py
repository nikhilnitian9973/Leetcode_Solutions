class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        one_half = s[:len(s)//2]
        one_half = sorted(one_half)

        if len(s) %2 == 0:
            out =  one_half + one_half[::-1]
        else:
            out =  one_half + [s[len(s)//2]] + one_half[::-1]
        return "".join(out)