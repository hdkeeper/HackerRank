#!/bin/python3

import math
import os
import random
import re
import sys


def countA(s):
    return len(re.findall('a', s))

# Complete the repeatedString function below.
def repeatedString(s, n):
    fullRepeatCount = n // len(s)
    tailLen = n % len(s)
    return countA(s) * fullRepeatCount + countA(s[:tailLen])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
