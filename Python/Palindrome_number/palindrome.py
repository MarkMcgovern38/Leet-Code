class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        original_x = x   
        reversed_x = 0
        


        while x != 0:
            l = x % 10
            reversed_x = reversed_x * 10 + l
            x //= 10

        return reversed_x == original_x
    
solution = Solution()
