class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        t = s.split(" ")
        w = []
        for i in range(len(t)):
            if t[i] != "":
                w.append(t[i])
        w = w[::-1]
        x = ""

        for i in range(len(w)):
            x += w[i] + " "

        return x.strip(" ")
        
