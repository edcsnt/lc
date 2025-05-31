# Copyright (C) 2025 Eduardo Santos <eduardo.experimental@gmail.com>
#
# This file is part of edcsnt/lc.
#
# edcsnt/lc is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# edcsnt/lc is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# edcsnt/lc. If not, see <https://www.gnu.org/licenses/>.
#

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
