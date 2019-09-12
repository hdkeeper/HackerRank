#!/bin/python3

import math
import os
import random
import re
import sys
from functools import cmp_to_key

class Contest(object):
    def __init__(self, luck, isImp):
        self.luck = luck
        self.isImp = isImp

    def __repr__(self):
        return '%d%s' % (self.luck, '!' if self.isImp != 0 else '')

    def comparator(a, b):
        res = b.isImp - a.isImp
        if res == 0:
            res = a.luck - b.luck
        return res


# Complete the luckBalance function below.
def luckBalance(k, contests):
    sortedContests = sorted(
        (Contest(l, t) for (l, t) in contests),
        key=cmp_to_key(Contest.comparator))

    # print(sortedContests)

    # Количество важных тестов в списке
    impCount = sum(1 for c in sortedContests if c.isImp != 0)

    # Количество тестов, которые нам надо выиграть
    winCount = max(impCount - k, 0)

    result = 0
    if winCount > 0:
        for i in range(0, winCount):
            result -= sortedContests[i].luck

    for i in range(winCount, len(sortedContests)):
        result += sortedContests[i].luck
    
    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
