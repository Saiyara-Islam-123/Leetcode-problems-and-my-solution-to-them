class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        #hash anagram key to words in strs

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in d:
                d[sorted_word] = []
            
            d[sorted_word].append(word)

        words = []
        for sorted_word in d:
            words.append(d[sorted_word])

        return words
    
sol = Solution()
print(sol.groupAnagrams(["cat", "tac", "kk"]))