class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = []
        for i in s: 
            if i in '([{':
                brackets.append(i) 
            else: 
                if not brackets or \
                    (i == ')' and brackets[-1] != '(') or \
                    (i == '}' and brackets[-1] != '{') or \
                    (i == ']' and brackets[-1] != '['):
                    return False
                brackets.pop()
        return not brackets
