class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for i in s:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        count_2 = {}
        for j in t:
            if j in count_2:
                count_2[j]+=1
            else:
                count_2[j]=1
        return (count) == (count_2)