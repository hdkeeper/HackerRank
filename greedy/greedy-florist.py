#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    minCost = 0
    c = sorted(c)
    tempCount = prevPurchases = 0

    if k >= len(c):
        minCost = sum(c)
    else:
        for i in reversed(range(0, len(c))):
            if tempCount == k:
                tempCount = 0
                prevPurchases += 1

            minCost += (prevPurchases + 1) * c[i]
            tempCount += 1

    return minCost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)
    fptr.write(str(minimumCost) + '\n')
    fptr.close()
