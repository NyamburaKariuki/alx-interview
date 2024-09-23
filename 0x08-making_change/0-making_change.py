#!/usr/bin/python3
"""Module for Making Change.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    """ Initialize a list with a large number, which will\
    represent an impossible total"""
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins are needed to make the total 0

    # Build up the solution for each total from 1 to the total
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    """If the total is still infinity, then it's not\ 
    possible to make the total with given coins"""
    return dp[total] if dp[total] != float('inf') else -1
