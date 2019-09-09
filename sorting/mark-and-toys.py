#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    count = 0
    sortedPrices = sorted(prices)
    for p in sortedPrices:
        if p <= k:
            k -= p
            count += 1
    
    return count


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    print(str(result) + '\n')
