# Copyright 2025 Eduardo Santos. All Rights Reserved.
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        visited = set()
        for n in nums:
            if n in visited:
                return True
            visited.add(n)
        return False
