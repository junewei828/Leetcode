
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = ""
        f = ""
        for i in range(len(s)):
            if s[i] not in f:
                f += s[i]
            else:
                if len(d) < len(f):
                    d = f
                f = f[f.index(s[i])+1::] + s[i]
    
    return max(len(d), len(f))


#Input: "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

#Input: "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
