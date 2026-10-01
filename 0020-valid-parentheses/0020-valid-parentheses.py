class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        check = True

        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if not stack:
                    return False
                elif (stack[-1] == "(" and i == ")") or (stack[-1] == "{" and i == "}") or (stack[-1] == "[" and i == "]"):
                    stack.pop()
                else:
                    check = False
        if stack:
            return False
        return check