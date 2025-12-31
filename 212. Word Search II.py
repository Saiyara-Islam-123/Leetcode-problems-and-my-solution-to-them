import numpy as np
class Stack:
    def __init__(self):
        self.l = []

    def push(self, elm):
        self.l.append(elm)
    def pop(self):
        return self.l.pop()
    def is_empty(self):
        return len(self.l) == 0

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        board = np.array(board)
        f = words[0][0]
        

