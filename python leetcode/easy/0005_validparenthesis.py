class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        opening_pairs = ['(','[','{']
        for i in s:
            if i in opening_pairs:
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1] == pairs[i]:
                    stack.pop()
                    # return True
                else: 
                    return False
        return not stack 