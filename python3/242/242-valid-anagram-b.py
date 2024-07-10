# Programming language: Python 3
# Algorithm/technique:  hash table
# Time complexity:      O(n)
# Auxiliary space:      O(n)
# Optimal:              yes
# Notes:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for i, c in enumerate(s):
            if count.get(c) is not None:
                count[c] += 1
            else:
                count[c] = 1
            if count.get(t[i]) is not None:
                count[t[i]] -= 1
            else:
                count[t[i]] = -1

        return not any(count.values())
