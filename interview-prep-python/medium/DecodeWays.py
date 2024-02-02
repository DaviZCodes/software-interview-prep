class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1} # base case is 1 way

        def dfs(i): # i is the index of the position on string
            if i in dp:
                return dp[i]
            if s[i] == "0": # if the character starts with 0 e.g. 06, it is invalid
                return 0
            
            # we want to recursively call the next index because the previous
            # one might be invalid
            res = dfs(i + 1) 

            if (i + 1) < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"): 
                '''
                if we do have one and second character in the string,
                if the first character is a 1, then we can definitely
                create a new decode like 12, 13 regardless of the
                second character. But if the first character is 2, then 
                the second character must be within 0-6 because the max
                character is 26, which is z.

                We add dfs(i + 2) because we want to skip over the 
                2 characters which we decoded.
                '''
                res += dfs(i + 2)

            dp[i] = res
            return res
        
        return dfs(0)

