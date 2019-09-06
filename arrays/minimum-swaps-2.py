#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(a):
    a = list(map( lambda n: n-1, a ))
    
    # Карта для быстрого поиска
    lookup = [0] * len(a)
    for i in range(0, len(a)):
        lookup[a[i]] = i

    count = 0
    lastPos = len(a) - 1
    while lastPos > 0:
        if a[lastPos] != lastPos:
            # Найти позицию элемента со значением lastPos
            srcPos = lookup[lastPos]

            # Обменять с последним элементом
            a[srcPos], a[lastPos] = a[lastPos], a[srcPos]
            lookup[a[lastPos]] = lastPos
            lookup[a[srcPos]] = srcPos
            count += 1

        lastPos -= 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
