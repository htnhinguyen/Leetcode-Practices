class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        j = 0
        i = 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j += 1
            i += 1
        if j < len(s): return False
        else: return True
