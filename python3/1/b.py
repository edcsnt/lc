# Algorithm/technique: sorting, two-pointers
# Time complexity:     O(n lb n)
# Auxiliary space:     O(n)
# Optimal:             no

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        snums: list[enumerate] = sorted(enumerate(nums), key=lambda n: n[1])

        i: int = 0
        j: int = len(nums) - 1
        total: int
        res: list[int]
        while i < j:
            total = snums[i][1] + snums[j][1]
            if total == target:
                return [snums[i][0], snums[j][0]]
            elif total < target:
                i += 1
            else:
                j -= 1
