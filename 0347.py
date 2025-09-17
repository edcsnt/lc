# Copyright 2025 Eduardo Santos. All rights reserved.
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        max_freq = 1
        res = []
        for n in nums:
            count[n] = count.get(n, 0) + 1
            if count[n] > max_freq:
                max_freq = count[n]
        freq = [[] for _ in range(max_freq + 1)]
        for n, c in count.items():
            freq[c].append(n)
        for c in range(max_freq, 0, -1):
            for n in freq[c]:
                res.append(n)
                if len(res) == k:
                    return res
