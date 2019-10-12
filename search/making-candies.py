#!/bin/python3

import math
import os
import random
import re
import sys


def divideToCeil(x, y):
    return x // y + (0 if x % y == 0 else 1)


# Complete the minimumPasses function below.
def minimumPasses(m, w, p, n):
    if m * w >= n:
        return 1

    minPass = 1e12
    curPass = 0
    production = 0
    while True:
        remainPass = divideToCeil(n - production, m * w)
        minPass = min(minPass, curPass + remainPass)
        if remainPass == 1:
            break
            
        if production < p:
            extraPass = divideToCeil(p - production, m * w)
            curPass += extraPass
            production += extraPass * m * w
            if production >= n:
                minPass = min(minPass, extraPass)
                break

        production -= p
        if m <= w:
            m += 1
        else:
            w += 1

    return int(minPass)


if __name__ == '__main__':
    mwpn = input().split()
    m = int(mwpn[0])
    w = int(mwpn[1])
    p = int(mwpn[2])
    n = int(mwpn[3])

    result = minimumPasses(m, w, p, n)
    print(result)
