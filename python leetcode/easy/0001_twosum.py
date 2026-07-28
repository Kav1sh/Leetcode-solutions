class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i]+nums[j]==target and i!=j):
                    return [i,j]
                
# what i learnt. 
# to use indices rather than position values of a list , use range. 
# range(len(nums)) gives values like 0,1,2,3