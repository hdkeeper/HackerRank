#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(a):
    def sumAt(r, c):
        return sum([
            a[r][c],
            a[r][c+1],
            a[r][c+2],
            a[r+1][c+1],
            a[r+2][c],
            a[r+2][c+1],
            a[r+2][c+2]
        ])

    maxVal = None
    for r in range(0, len(a)-2):
        for c in range(0, len(a[0])-2):
            s = sumAt(r, c)
            if maxVal is None or s > maxVal:
                maxVal = s
    return maxVal


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
