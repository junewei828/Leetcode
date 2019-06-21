class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        if len(s) == 1:
            return roman[s]
        result = roman[s[-1]]
        for i in range(len(s)-1, 0, -1):
            if roman[s[i-1]] < roman[s[i]]:
                result -= roman[s[i-1]]
            else:
                result += roman[s[i-1]]
        return result
