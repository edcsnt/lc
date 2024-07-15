# Algorithm/technique: nested iteration, sorting
# Time complexity:     O(n^2 k lb k)
# Auxiliary space:     O(n)
# Optimal:             no

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        i: int
        s: str
        n: int = len(strs)
        # Flattening strs would require O(nk) time, while initializing visited
        # requires only O(n).
        visited = n * [False]
        grp: list[str]
        j: int
        grps: list[list[str]] = []
        for i, s in enumerate(strs):
            if not visited[i]:
                grp = [s]
                visited[i] = True
                for j in range(i + 1, n):
                    if not visited[j]:
                        if sorted(s) == sorted(strs[j]):
                            grp.append(strs[j])
                            visited[j] = True

                grps.append(grp)

        return grps
