# Algorithm/technique: hash table
# Time complexity:     O(n)
# Auxiliary space:     O(n)
# Optimal:             yes

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i: int
        num: int
        diff: int
        visited: dict[int, int] = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in visited:
                return [visited[diff], i]
            visited[num] = i
