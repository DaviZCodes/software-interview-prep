class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0

        for i in range(len(s)):
            if i + 1 < len(s) and symbol_values[s[i]] < symbol_values[s[i + 1]]:
                result -= symbol_values[s[i]]
            else:
                result += symbol_values[s[i]]
            
        return result
      
'''

Another solution:

class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        total = 0
        
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")

        for char in s:
            total += numerals[char]

        return total
'''
