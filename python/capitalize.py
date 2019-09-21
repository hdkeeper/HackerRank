#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    ch = list(s)
    for i in range(0, len(ch)):
        if (i == 0) or (ch[i] != ' ' and ch[i-1] == ' '):
            ch[i] = ch[i].upper()

    return ''.join(ch)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
