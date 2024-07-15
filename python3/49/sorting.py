# Algorithm/technique: sorting
# Time complexity:     O(nk lb k)
# Auxiliary space:     O(nk)
# Optimal:             yes

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        s: str
        ss: str
        grps: dict[str, list[str]] = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in grps:
                grps[ss].append(s)
            else:
                grps[ss] = [s]

        return grps.values()
