class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zero_count=0
        # i=0
        # while i < len(nums):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         zero_count+=1
        #     else:
        #         i+=1
        # for x in range(zero_count):
        #     nums.append(0)
        ###optimal solution below 
        i,j = 0,0 
        for x in range(len(nums)):
            if nums[x] == 0:
                j+=1
            elif nums[x] !=0 :
                nums[x],nums[i] = nums[i],nums[x]
                i+=1