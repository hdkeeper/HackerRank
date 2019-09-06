#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairCount = 0
    pool = {}
    for s in ar:
        if not s in pool:
            pool[s] = 0

        if pool[s] > 0:
            pool[s] -= 1
            pairCount += 1
        else:
            pool[s] += 1

    return pairCount



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
