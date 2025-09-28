#this one passes test cases but takes too long. Don't know if that's a W
def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        acc = ""
        longest = ""


        for i in range(len(s)): #for each letter
            for j in range(i, len(s)): #we iterate through the rest of the string

                acc += s[j] #increasing acc
                if acc == acc[::-1]: #if palindrome
                    if len(longest) < len(acc): #if we get a longer palindrome than the prev longest
                        longest = acc #update the longest


            acc = "" #resetting accumulator

        return longest

        

