#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count = 0
    new_s = re.sub(r'(\w)\1', r'\1', s, count=1)

    while s != new_s:
        count += 1
        s = new_s
        new_s = re.sub(r'(\w)\1', r'\1', s, count=1)

    return count
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
