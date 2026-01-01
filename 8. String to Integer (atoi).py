import math
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.strip(" ")
        #check for sign + or -
        multiplier = 1
        start = 0
        if len(s) == 0:
            return 0
        if s[0] == "-":
            multiplier = -1
            start += 1
        elif s[0] == "+":
            multiplier = 1
            start += 1

        s= s[start:]
        start_2= 0
        for i in range(len(s)):
            if s[i] != 0:
                start_2=i
                break

        s = s[start_2:]
        digits = ""
        if len(s) == 0:
            return 0

        for i in range(len(s)):
            if s[i].isdigit():
                digits += s[i]
            else:
                if i == 0:
                    return 0
                break

        num = multiplier* int(digits)
        
        upper_lim = 2147483647
        lower_lim = -2147483648

        if num > upper_lim:
            return upper_lim
        
        elif num < lower_lim:
            return lower_lim

        return num
        
    

sol = Solution()
print(sol.myAtoi("  -g04h5  "))