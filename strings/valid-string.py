#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    # Считаем количество символов
    charCount = {}
    for ch in s:
        charCount[ch] = charCount.get(ch, 0) + 1

    # Считаем количество частот
    freqCount = {}
    for cnt in charCount.values():
        freqCount[cnt] = freqCount.get(cnt, 0) + 1

    print(charCount)
    print(freqCount)

    # Частоты всех букв равны
    if len(freqCount) == 1:
        return 'YES'

    # При таком разнобое частот привести строку не удастся
    if len(freqCount) > 2:
        return 'NO'

    # Можно ли привести строку, удалив один символ
    minFreq = min(freqCount.keys())
    if freqCount.get(minFreq + 1, 0) == 1:
        return 'YES'

    maxFreq = max(freqCount.keys())
    otherFreq = [fr for fr in freqCount.keys() if fr != maxFreq][0]
    if freqCount[otherFreq] == 1:
        return 'YES'

    return 'NO'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
