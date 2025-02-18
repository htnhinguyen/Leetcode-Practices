class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h = 0

        while h+n <= len(haystack):
            if haystack[h:h+n] == needle:
                return h
            h += 1

        return -1
