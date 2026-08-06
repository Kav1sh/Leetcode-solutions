class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
       output = []
       running_sum = 0
       for i in nums:

        running_sum += i
        output.append(running_sum)
       return output