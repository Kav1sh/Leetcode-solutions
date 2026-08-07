class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        output = 0
        n = len(nums)
        expected_sum = n*(n+1)/2
        actual_sum = 0
        for x in nums:
            actual_sum+=x
        output = expected_sum-actual_sum
        return int(output)