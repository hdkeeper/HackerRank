#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    def makeFreq(s):
        res = {}
        for ch in s:
            res[ch] = res.get(ch, 0) + 1
        return res

    aFreq = makeFreq(a)
    bFreq = makeFreq(b)

    # Сократить на минимальное количество одинаковых букв
    for ch in aFreq.keys():
        if ch in bFreq:
            minCount = min(aFreq[ch], bFreq[ch])
            aFreq[ch] -= minCount
            bFreq[ch] -= minCount

    # Посчитать сумму оставшихся букв
    return sum(aFreq.values()) + sum(bFreq.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
