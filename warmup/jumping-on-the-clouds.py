#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0
    count = 0
    last = len(c) - 1
    while i < last:
        if i+2 <= last and c[i+2] == 0:
            i += 2
            count += 1
        elif c[i+1] == 0:
            i += 1
            count += 1
        else:
            return 'FAIL'

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
