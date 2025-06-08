class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        l=0
        r=0

        if s == s[::-1]:
            return 1
        else:
            return 2