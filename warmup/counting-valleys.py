#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count = 0
    curHeight = 0
    for step in s:
        if step == 'D' and curHeight == 0:
            count += 1

        if step == 'U':
            curHeight += 1
        elif step == 'D':
            curHeight -= 1

    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
