class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            strs.sort()
            prefix = ""
            for x, y in zip(strs[0], strs[-1]):
                if x == y:
                    prefix += x
                else:
                    break
            return prefix
