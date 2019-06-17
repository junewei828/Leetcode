
class Solution:
    def reverse(self, x: int) -> int:
        
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            strg = str(x)
            if x >= 0 :
                reversed = strg[::-1]
            else:
                valid_nun = strg[1:]
                temp2 = valid_nun[::-1]
                reversed = "-" + temp2
    if int(reversed) >= 2**31-1 or int(reversed) <= -2**31: return 0
        return int(reversed)
