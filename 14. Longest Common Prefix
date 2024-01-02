def helper(str1, str2):
    if len(str1) >= len(str2):
        n = len(str2)
        
    else:
        n = len(str1)
    common_pre = ""
    
    for i in range(0, n):
        if str1[i] == str2[i]:
            common_pre += str1[i]
        else:
            break

    return common_pre

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = strs[0]
        for word in strs:
            common = helper(common, word)

        return common
