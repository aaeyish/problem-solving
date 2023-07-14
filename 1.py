# https://leetcode.com/problems/roman-to-integer/
# O() time | O() space
class Solution:
    def romanToInt(self, s: str) -> int:
        symobols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII")  # 4
        s = s.replace("IX", "VIIII")  # 9
        s = s.replace("XL", "XXXX")  # 40
        s = s.replace("XC", "LXXXX")  # 90
        s = s.replace("CD", "CCCC")  # 400
        s = s.replace("CM", "DCCCC")  # 900
        for i in s:
            number += int(symobols[i])
        return number


print(Solution().romanToInt("III"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))
print(Solution().romanToInt("I"))
print(Solution().romanToInt("II"))
print(Solution().romanToInt("III"))
print(Solution().romanToInt("IV"))
print(Solution().romanToInt("V"))
print(Solution().romanToInt("VI"))
print(Solution().romanToInt("VII"))
print(Solution().romanToInt("VIII"))
print(Solution().romanToInt("IX"))
print(Solution().romanToInt("X"))
print(Solution().romanToInt("XI"))
print(Solution().romanToInt("XII"))
