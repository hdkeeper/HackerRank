#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minTime function below.
def minTime(machines, goal):
    def doneOnDay(day):
        return sum((day // m) for m in machines)

    class Point(object):
        def __init__(self, day):
            self.day = day
            self.items = doneOnDay(day)

        def __repr__(self):
            return '(Day {}, items {})'.format(self.day, self.items)

    p1 = Point(0)
    p2 = Point(10)

    # Find upper limit
    while p2.items < goal:
        p2 = Point(p2.day * 2)

    # Binary search
    while True:
        p = Point((p1.day + p2.day) // 2)
        if p.items == goal:
            break
        elif goal < p.items:
            p2 = p
        else: # p.items < goal
            p1 = p

        # Prevent internal loop
        if abs(p1.day - p2.day) <= 1:
            p = p2
            break

        # print('{} - {}'.format(p1, p2))

    # Rewind back for the minimum day
    while True:
        p1 = Point(p.day - 1)
        if p1.items < p.items:
            break
        else:
            p = p1

    return p.day


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nGoal = input().split()
    n = int(nGoal[0])
    goal = int(nGoal[1])
    machines = list(map(int, input().rstrip().split()))
    ans = minTime(machines, goal)
    print(ans)
    fptr.write(str(ans) + '\n')
    fptr.close()
