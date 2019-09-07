#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = n

    # Проверить на символы, идущие подряд
    for i in range(0, n-1):
        start_char = s[i]
        for j in range(i+1, n):
            if s[j] == start_char:
                count += 1
            else:
                break

    # Проверить на подстроки вида aaabaaa
    for i in range(1, n-1):
        middle_char = s[i]
        side_char = s[i-1]

        if middle_char == side_char or side_char != s[i+1]:
            continue

        '''
        abcdefghi
          ^
        i=2
        max(d) = 2

        abcdefghi
               ^
        i=7
        n=9
        max(d)=1
        n-i-1
        '''
        
        max_delta = min(i, n-i-1)
        for d in range(1, max_delta+1):
            if s[i-d] == side_char and s[i+d] == side_char:
                count += 1
            else:
                break

    return count


if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    n = 4
    s = 'aaaa'

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
