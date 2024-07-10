# Programming language: Python 3
# Algorithm/technique:  nested iteration
# Time complexity:      O(n^2)
# Auxiliary space:      O(1)
# Optimal:              no
# Notes:

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)

        if n < 2:
            return False

        # enumerate does not allow the last item to be skipped without slicing,
        # which would require O(n) auxiliary space.
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True

        return False
