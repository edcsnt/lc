# Programming language: Python 3
# Algorithm/technique:  set
# Time complexity:      O(n)
# Auxiliary space:      O(n)
# Optimal:              yes
# Notes:

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        visited = set()

        for num in nums:
            if num in visited:
                return True
            visited.add(num)

        return False
