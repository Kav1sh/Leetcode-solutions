class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for x in nums:
            if x in count:
                count[x]+=1
            else:
                count[x]=1
        for y in count:
            if count[y]==1:
                return y
            else:
                continue 