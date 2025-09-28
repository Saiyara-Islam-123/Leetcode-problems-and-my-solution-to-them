
class Solution(object):


    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_of_outputs = []
        acc = ""
        for i in range(len(s)):

            if s[i] in acc:
                list_of_outputs.append(acc)
                acc = ""

            acc = acc + s[i]

        list_of_outputs.append(acc)
        print(list_of_outputs)
        return len(list_of_outputs)
