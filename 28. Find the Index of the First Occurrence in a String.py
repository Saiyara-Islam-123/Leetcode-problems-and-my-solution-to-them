class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(needle) > len(haystack):
            return -1

        acc = ""
        start = -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                acc = ""
                start = i
                for j in range(i, len(haystack)):
                    acc += haystack[j]

                    if acc == needle:
                        return start

        return -1