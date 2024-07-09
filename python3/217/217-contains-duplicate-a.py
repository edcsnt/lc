# Programming language: Python 3
# Algorithm/technique:  nested iteration
# Time complexity:      O(n^2)
# Space complexity:     O(1)
# Optimal:              no
# Notes:

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if num == nums[j]:
                    return True

        return False
