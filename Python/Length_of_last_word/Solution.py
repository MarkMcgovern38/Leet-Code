class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        j= len(s) - 1
        total=0

        while j >=0 and s[j] == ' ':
            j -= 1

        while j >= 0 and s[j] != ' ':
            total += 1
            j -= 1
                    
        return total
