class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        total = 0
        prev_value = 0

        for symbol in reversed(s):
            value = roman_values[symbol]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        
        return total
    
solution = Solution()
roman_numeral = "MCMXCIV"
result = solution.romanToInt(roman_numeral)
print(f"The Roman numeral {roman_numeral} is {result}")
