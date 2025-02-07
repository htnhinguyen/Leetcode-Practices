class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        strs.sort()
        i = 0
        j = 0
        start = strs[0]
        end = strs[-1]

        while i < len(start) and j < len(end):
            if start[i] == end[j]:
                res += start[i]
                i += 1
                j += 1
            else: break
        return res
        
