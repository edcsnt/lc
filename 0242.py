# Copyright 2025 Eduardo Santos. All rights reserved.
class Solution:
    def all_zeros(self, ls: list[int]) -> bool:
        for i in ls:
            if i != 0:
                return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        try:
            for c, d in zip(s, t, strict=True):
                count[c] = count.get(c, 0) + 1
                count[d] = count.get(d, 0) - 1
        except ValueError:
            return False
        return self.all_zeros(list(count.values()))
