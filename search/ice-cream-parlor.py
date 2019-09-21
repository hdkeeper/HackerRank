#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    cost_map = {}
    for i in range(len(cost)):
        left_money = money - cost[i]
        if left_money in cost_map:
            res = sorted([ i+1, cost_map[left_money]+1 ])
            print(res[0], res[1])
            return

        if not cost[i] in cost_map:
            cost_map[cost[i]] = i


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())
        n = int(input())
        cost = list(map(int, input().rstrip().split()))
        whatFlavors(cost, money)
