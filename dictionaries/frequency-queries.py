#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    items = {}
    freqs = { 0: set() }
    result = []

    def updateFreqs(prevFreq, nextFreq, n):
        freqs[prevFreq].discard(n)
        if not nextFreq in freqs:
            freqs[nextFreq] = set()    
        freqs[nextFreq].add(n)

    for (op, n) in queries:
        if op == 1:
            # Insert
            if n in items:
                items[n] += 1
            else:
                items[n] = 1

            updateFreqs(items[n] - 1, items[n], n)

        elif op == 2:
            # Delete
            if n in items and items[n] > 0:
                items[n] -= 1
                updateFreqs(items[n] + 1, items[n], n)

        elif op == 3:
            # Check freq
            if n in freqs and len(freqs[n]) > 0:
                result.append(1)
            else:
                result.append(0)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
