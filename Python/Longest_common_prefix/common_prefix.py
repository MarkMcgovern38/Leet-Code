class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        strs.sort()

        str1 = strs[0]
        str2 = strs[-1]
        common = []


        
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                common.append(str1[i])
            else: 
                break
            
        return "".join(common)
