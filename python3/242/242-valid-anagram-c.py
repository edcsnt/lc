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

        return collections.Counter(s) == collections.Counter(t)
