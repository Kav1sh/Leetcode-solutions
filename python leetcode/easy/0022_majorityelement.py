class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        output = {}
        number = len(nums)
        for x in range(len(nums)):
            if nums[x] in output:
                output[nums[x]]+=1
            else:
                output[nums[x]]=1
        for y in output:
            if output[y] > number/2:
                return y
            else:
                continue 
#majority element