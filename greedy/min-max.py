#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    a = sorted(arr)
    minUnfair = None
    for i in range(0, len(a)-k+1):
        unfair = a[i+k-1] - a[i]
        if minUnfair is None:
            minUnfair = unfair
        else:
            minUnfair = min(minUnfair, unfair)

    return minUnfair



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
