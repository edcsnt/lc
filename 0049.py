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
