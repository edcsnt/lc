# Algorithm/technique: hash table
# Time complexity:     O(n)
# Auxiliary space:     O(n)
# Optimal:             yes

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) < 2:
            return False

        visited: set[int] = set()

        num: int
        for num in nums:
            if num in visited:
                return True
            visited.add(num)

        return False
