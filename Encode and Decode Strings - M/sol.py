class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '-' + s
        return res

    def decode(self, s: str) -> List[str]:
        j = 0
        res = []
        while j < len(s):
            i = j
            while s[i] != '-':
                i += 1
            length = int(s[j:i])
            j = i + 1
            i = j + length
            res.append(s[j:i])
            j = i    
        return res

# 3-abc1-i2we


