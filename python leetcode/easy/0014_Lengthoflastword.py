class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = s.split()[-1]
        return len(result)