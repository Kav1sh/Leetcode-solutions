class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # (last_digit) = digits[-1] + 1
        # output = []
        # if last_digit <=9:
        #     digits[-1] = last_digit
        # else:
        #     digits[-2] = last_digit[-2]
        #     digits[-1] = last_digits[-1]


        
        number = int("".join(map(str, digits)))
        number += 1
        digits = list(map(int, str(number)))
        return digits