
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = {}
        max_len = 0
        index_of_sub = 0
        for i in range(len(s)):
            char = s[i]
            if char in sub:
                if len(sub) > max_len:
                    max_len = len(sub)
                prev_index = sub[char]
                #remove this prev instance as well as all prev elements
                new_sub = {}
                for c in sub:
                    if sub[c] > prev_index:
                        new_sub[c] = sub[c]
                sub = new_sub
            sub[char]=index_of_sub
            index_of_sub += 1
        if len(sub) > max_len:
            max_len = len(sub)
        return max_len

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("dvdf"))