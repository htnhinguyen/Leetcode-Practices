class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        f = 0
        b = len(s)-1
        while f<b:
            if s[f].isalnum() == False: 
                f +=1
            elif s[b].isalnum() == False:
                b -= 1
            elif s[f] != s[b]:
                return False
            else: 
                f += 1
                b -= 1
        return True

      
