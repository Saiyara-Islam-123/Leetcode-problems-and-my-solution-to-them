import numpy as np
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        adj = [] #rows are from and columns are to

        for i in range(n):
            row = []
            for j in range(n):
                if j != i:
                    row.append(0)
                else:
                    row.append(-1)
            adj.append(row)

        for t in trust:
            [a, b] = t
            adj[a-1][b-1] = 1

        adj = np.array(adj)
        for i in range(n):
            if 1 not in adj[i, :] and 0 not in adj[:, i]:
                return i+1
        return -1



if __name__ == '__main__':
    solution = Solution()
    trust = [[1,2]]
    n = 2
    print(solution.findJudge(n, trust))