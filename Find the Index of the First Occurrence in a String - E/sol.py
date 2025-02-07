class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        firstLetter = needle[0]
        for l in range(len(haystack)):
            if haystack[l] == firstLetter:
                i = 1
                while i < len(needle) and l+i < len(haystack):
                    if haystack[l+i] != needle[i]:
                        break
                    i += 1
                if i == len(needle):
                    return l
        return -1
