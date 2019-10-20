#!/bin/python3

import math
import os
import random
import re
import sys

opening = '[({'
closing = '])}'

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    for c in s:
        if c in opening:
            stack.append(opening.index(c))
        elif c in closing:
            if len(stack) == 0 or stack.pop() != closing.index(c):
                return 'NO'

    return 'YES' if len(stack) == 0 else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
