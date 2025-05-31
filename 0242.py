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
    def all_zeros(self, ls: list[int]) -> bool:
        for i in ls:
            if i != 0:
                return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        try:
            for (c, d) in zip(s, t, strict=True):
                count[c] = count.get(c, 0) + 1
                count[d] = count.get(d, 0) - 1
        except ValueError:
            return False
        return self.all_zeros(list(count.values()))
