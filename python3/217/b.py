# Algorithm/technique: sorting
# Time complexity:     O(n lb n)
# Auxiliary space:     O(1)
# Optimal:             no

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) < 2:
            return False

        nums.sort()

        i: int
        num: int
        for i, num in enumerate(nums):
            # nums[0] is needlessly compared to nums[-1] so as to avoid
            # checking if i > 0 at every iteration.
            if num == nums[i - 1]:
                return True

        return False
