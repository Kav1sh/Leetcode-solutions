class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return sorted(nums) != sorted(list(set(nums)))
        # return len(nums) != len(set(nums))


        #important lesson. set does not preserve input order as a list. it gives unpredictable order
        #  .sort() doesnt work in python, the function is sorted()