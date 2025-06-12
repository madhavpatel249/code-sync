class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        final = ""
        if (len(word1)>len(word2)):
            for i in range(len(word2)):
                final += word1[i]
                final += word2[i]
            final += word1[len(word2):len(word1)]
            return final
        else:
            for i in range(len(word1)):
                final += word1[i]
                final += word2[i]
            final += word2[len(word1):len(word2)]
            return final