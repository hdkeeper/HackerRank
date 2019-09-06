#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    avail = {}
    for word in magazine:
        if word in avail:
            avail[word] += 1
        else:
            avail[word] = 1

    for word in note:
        if word not in avail or avail[word] < 1:
            print('No')
            return

        avail[word] -= 1

    print('Yes')


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
