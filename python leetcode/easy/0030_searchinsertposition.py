class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for k in range(len(nums)):
            if nums[k]==target:
                return k
            elif target < nums[k]:
                return k
        else:
            return len(nums)