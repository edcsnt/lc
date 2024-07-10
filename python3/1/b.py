# Algorithm/technique: sorting
# Time complexity:     O(n lb n)
# Auxiliary space:     O(n)
# Optimal:             no

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        snums: list[int] = sorted(nums)

        i: int = 0
        j: int = len(nums) - 1
        total: int
        res: list[int]
        while i < j:
            total = snums[i] + snums[j]
            if total == target:
                res = [nums.index(snums[i]), nums.index(snums[j])]
                if res[0] == res[1]:
                    res[1] = nums.index(snums[j], res[0] + 1)
                return res
            elif total < target:
                i += 1
            else:
                j -= 1
