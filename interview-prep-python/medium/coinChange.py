class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dynamic programming to store # of coins for each amount
        dp = [amount + 1] * (amount + 1) # use amount + 1 for max val
        dp[0] = 0 # base case

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0: # positive value, we don't want negative
                    dp[i] = min(dp[i], 1 + dp[i - coin]) 
                    #min coins,
        
        # if result is not max val (amount + 1), we found answer, else return -1
        return dp[amount] if dp[amount] != (amount + 1) else -1
