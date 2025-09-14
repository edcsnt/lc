# Copyright 2025 Eduardo Santos. All Rights Reserved.
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in visited:
                return [visited[diff], i]
            visited[n] = i
