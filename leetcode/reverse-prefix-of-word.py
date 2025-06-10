class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        
        left = 0
        right = 0
        string = ""

        for i in range(len(word)):
            if word[right] == ch:
                string += word[right::-1]
                string += word[right+1:]
                return string
            else:
                right += 1
        
        
        return word