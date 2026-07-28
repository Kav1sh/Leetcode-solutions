class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        output = {}
        for x in magazine:
            if x in output:
                output[x]+=1
            else:
                output[x]=1
        for y in ransomNote:
            if y in output and output[y]>0:
                output[y]-=1
            else:
                return False
        return True   