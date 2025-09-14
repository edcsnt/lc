# Copyright 2025 Eduardo Santos. All Rights Reserved.
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}
        for s in strs:
            count = 26 * [0]
            for c in s:
                count[ord(c) - ord('a')] += 1
            t = tuple(count)
            try:
                res[t].append(s)
            except KeyError:
                res[t] = [s]
        return list(res.values())
