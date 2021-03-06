'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp =   [0] + ([float('inf') * amount])

        for i, val in enumerate(dp):
            for coin in coins:
                if coin <= i :
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        minCoins = dp[-1]
        if minCoin s== float('inf'):
            return -1
        return minCoins