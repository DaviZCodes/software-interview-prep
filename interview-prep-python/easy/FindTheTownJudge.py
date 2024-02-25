# this is a better soltuion since trust[i][0] might be confusing, default dicts are easier to handle with
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int) # we use default dict to avoid out of bounds error
        outgoing = defaultdict(int) # initialized at zero, must be integers

        for src, dst in trust: # each element is like [a, b]
            incoming[dst] += 1
            outgoing[src] += 1
        
        for i in range(1, n + 1):
            if incoming[i] == (n - 1) and outgoing[i] == 0: # everyone trusts the judge but themselves so (n - 1)
                return i
        
        return -1 # no town judge found
        
'''class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degree = [0] * (n + 1) # in_degree means someone trusts you
        out_degree = [0] * (n + 1) # out degree means you trust someone

        for i in range (len(trust)):
            # trust[0] is out_degree
            # trust[1] is in_degree
            out_degree[trust[i][0]] += 1
            in_degree[trust[i][1]] += 1
        
        for i in range(1, n + 1):
            if in_degree[i] == n - 1 and out_degree[i] == 0: # person is trusted by everyone (everyone minus themselves) and the person does not trust anyone
                return i
        
        return -1
'''
        
        
