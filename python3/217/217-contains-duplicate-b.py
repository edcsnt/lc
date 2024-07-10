# Programming language: Python 3
# Algorithm/technique:  sorting
# Time complexity:      O(n lb n)
# Auxiliary space:      O(1)
# Optimal:              no
# Notes:

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0:
                if num == nums[i - 1]:
                    return True

        return False
