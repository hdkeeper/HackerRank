import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    arr.sort()
    count = 0
    i = 0
    j = 1
    while j < len(arr):
        d = arr[j] - arr[i]
        if d == k:
            i += 1
            j += 1
            count += 1
        elif d > k:
            i += 1
        else:
            j += 1

    return count


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    print(str(result))
