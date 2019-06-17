class Solution:
    def myAtoi(self, str: str) -> int:
        sign = ""
        new_str = ""
        pointer = 0
        
        for i in range(len(str)):
            ele = str[i]
            if ele == " ":
                next
            else:
                if ele == "+" or ele == "-":
                    sign = ele if ele == "-" else ""
                    pointer = i + 1
                if ele >= "0" and ele <= "9":
                    pointer = i
                break
    
        for j in range(pointer, len(str), 1):
            ele = str[j]
            if ele >= "0" and ele <= "9":
                new_str += ele
            else:
                break

        if len(new_str) > 0:
            num = int(sign + new_str)
        else:
            num = 0
        return max(-2**31, min(2**31-1, num))
