#!/usr/bin/python3

def makeChange(coins, total):
    # Initialize dp array with total+1 as we can't have more coins than total+1
    dp = [total + 1] * (total + 1)
    
    # If total is 0, then answer is 0
    dp[0] = 0
    
    # For each coin, we update our dp array
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    # If dp[total] is still total+1, then we return -1 as no combination can sum to total
    return dp[total] if dp[total] != total + 1 else -1

