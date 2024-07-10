# Algorithm/technique: sorting
# Time complexity:     O(n lb n)
# Auxiliary space:     O(n)
# Optimal:             no

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l = 0
        r = len(nums) - 1
        snums = sorted(nums)

        while l < r:
            total = snums[l] + snums[r]
            if total == target:
                res = [nums.index(snums[l]), nums.index(snums[r])]
                if res[0] == res[1]:
                    res[1] = nums.index(snums[r], res[0] + 1)
                return res
            elif total < target:
                l += 1
            else:
                r -= 1
