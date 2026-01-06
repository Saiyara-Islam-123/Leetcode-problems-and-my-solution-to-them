def flip(x):
        if x == "T":
            return "F"
        
        if x == "F":
            return "T"
        
def copy(x):
     new = []
     for i in range(len(x)):
          new.append(x[i])

     return new
        
def consecutive_count(arr):
    max_count = 0
    count = 0
    prev_char = arr[0]    
    for i in range(len(arr)):
         curr_char = arr[i]
         if curr_char != prev_char:
              prev_char = curr_char
              
              count = 1
         else:
              count += 1

         if count > max_count:
            max_count = count

    return max_count

class Solution(object):
    
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        l = []
        for char in answerKey:
             l.append(char)

        answerKey = l

        d = {}
        without_flip = answerKey
        with_flip = copy(without_flip)
        with_flip[0] = flip(with_flip[0])

        if consecutive_count(without_flip) >= consecutive_count(with_flip):
                 d[0] = (without_flip, 0)

        else:
                 d[0] = (with_flip, 1)

        for i in range(1, len(answerKey)):
            without_flip, flip_count = d[i-1]
            with_flip = copy(without_flip)
            with_flip[i] = flip(with_flip[i])

            if consecutive_count(without_flip) >= consecutive_count(with_flip):
                 d[i] = (without_flip, flip_count)

            else:
                 d[i] = (with_flip, flip_count+1)

        result, flips = d[len(answerKey)-1]

        return consecutive_count(result)
    

sol = Solution()
print(sol.maxConsecutiveAnswers("TTFF", 2))