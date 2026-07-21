class Solution:
    def isPalindrome(self, x: int) -> bool:
        # s = str(x)
        # if s[0:] == s[::-1]:
        #     return True
        # else:
        #     return False

        if x<0 or (str(x)[-1]=="0"):
            return False
        new_x = x
        reversed_x = 0
        while x>0:
            digit = x % 10
            x = x // 10
            reversed_x = (reversed_x * 10) + digit 
        return reversed_x == new_x