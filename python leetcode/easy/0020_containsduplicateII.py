class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Brute Force Approach
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             if nums[i] == nums[j] and abs(i-j) <= k:
        #                 return True
        # return False

        last_seen = {}

        for i in range(len(nums)):
            if nums[i] in last_seen:
                if i - last_seen[nums[i]] <= k:
                    return True

            last_seen[nums[i]] = i

        return False