class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        shortest_len = 0
        word1_shorter = False
        word2_shorter = False

        if len(word1) >= len(word2):
            shortest_len = len(word2)
            word2_shorter = True
        else:
            shortest_len = len(word1)
            word1_shorter = True

        acc = ""
        for i in range(shortest_len):

            acc = acc + word1[i]
            acc = acc + word2[i]

        
        if(word1_shorter):
            for j in range(i + 1, len(word2)):
                acc = acc + word2[j]

        else:
            for j in range(i + 1, len(word1)):
                acc = acc + word1[j]

        return acc
