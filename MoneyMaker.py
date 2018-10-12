# import numpy as np

def count_change(money, coins):
    if money<0:
        return 0
    if money == 0:
        return 1
    if money>0 and not coins:
        return 0
    return count_change(money-coins[-1],coins) + count_change(money,coins[:-1])

print(count_change(10, [5,2,3]))