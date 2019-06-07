
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return s
        res = ""
        for i in range(len(s)):
            j = i + 1
            # While j is less than length of string
            # AND res is *not* longer than substring s[i:]
            while j <= len(s) and len(res) <= len(s[i:]):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(res):
                    res = s[i:j]
                j += 1
        
    return res

#Input: "babad"
#Output: "bab"
#Input: "cbbd"
#Output: "bb"
