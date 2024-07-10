# Algorithm/technique: sorting
# Time complexity:     O(n lb n)
# Auxiliary space:     O(1)
# Optimal:             no

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return s.sort() == t.sort()
