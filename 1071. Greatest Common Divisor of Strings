def divides(str1, s):
    if len(s) == 0:
        return False

    mult = int(len(str1) / len(s))

    if (len(str1) % len(s) == 0):
        acc = ""
        for i in range (0, mult):
            acc += s

    else:
        return False

    if str1 == acc:
        return True
    else:
        return False


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        if str1 == str2:
            return str1

        if len(str1) >= len(str2):
            bigger = str1
            smaller = str2
        else:
            bigger = str2
            smaller = str1

        list_of_common_divisors = []
        common_divisor = ""
        for i in range(len(bigger)):

            if divides(bigger, common_divisor) == False:
                common_divisor += bigger[i]

            else:
                list_of_common_divisors.append(common_divisor)
                common_divisor += bigger[i]
        
        ones_that_divide = []

        for i in range(len(list_of_common_divisors)):
            if divides(smaller, list_of_common_divisors[i]):
                ones_that_divide.append(list_of_common_divisors[i])

        largest = ""

        for i in range(len(ones_that_divide)):
            if len(ones_that_divide[i]) > len(largest):
                largest = ones_that_divide[i]

        return largest
