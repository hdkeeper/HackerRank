#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    out = [0] * (n + 2)
    for (a, b, k) in queries:
        out[a] += k
        out[b+1] -= k

    maxVal = None
    sumVal = 0
    for n in out:
        sumVal += n
        if maxVal is None or sumVal > maxVal:
            maxVal = sumVal

    return maxVal


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    fptr.write(str(result) + '\n')
    fptr.close()
