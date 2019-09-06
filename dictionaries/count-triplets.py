#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    left = {}
    right = {}
    count = 0

    for i in range(0, len(arr)):
        left[arr[i]] = right[arr[i]] = 0

    for i in range(0, len(arr)):
        right[arr[i]] += 1

    for i in range(0, len(arr)):
        n2 = arr[i]
        right[n2] -= 1

        if n2 % r == 0:
            n1 = n2 / r
            n3 = n2 * r

            if n1 in left and n3 in right:
                count += left[n1] * right[n3]

        left[n2] += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
