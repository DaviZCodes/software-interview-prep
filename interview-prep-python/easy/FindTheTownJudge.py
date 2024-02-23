class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degree = [0] * (n + 1) # in_degree means someone trusts you
        out_degree = [0] * (n + 1) # out degree means you trust someone

        for i in range (len(trust)):
            # trust[0] is out_degree
            # trust[1] is in_degree
            out_degree[trust[i][0]] += 1
            in_degree[trust[i][1]] += 1
        
        for i in range(1, n + 1):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i
        
        return -1
        
        
