# Algorithm/technique: hash table
# Time complexity:     O(nk)
# Auxiliary space:     O(nk)
# Optimal:             yes

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        s: str
        count: list[int]
        c: str
        # https://github.com/python/typing/issues/786.
        grp: tuple[
            int, int, int, int, int, int, int, int, int, int, int, int, int,
            int, int, int, int, int, int, int, int, int, int, int, int, int
        ]
        grps: dict[tuple[
            int, int, int, int, int, int, int, int, int, int, int, int, int,
            int, int, int, int, int, int, int, int, int, int, int, int, int
        ], list[str]] = {}
        for s in strs:
            count = 26 * [0]
            for c in s:
                count[ord(c) - ord('a')] += 1

            grp = tuple(count)
            if grps.get(grp) is not None:
                grps[grp].append(s)
            else:
                grps[grp] = [s]

        return grps.values()
