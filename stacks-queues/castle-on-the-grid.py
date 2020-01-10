#!/bin/python3

import math
import os
import random
import re
import sys
from collections import namedtuple, deque

Point = namedtuple('Point', 'x y')

def getPointsFromPoint(N, arr, point):
    x = point.x
    y = point.y
    points = []

    while x > 0:
        x -= 1
        if arr[x][y] == 'X':
            break
        points.append(Point(x,y))
     
    x = point.x
    while x < N-1: 
        x += 1
        if arr[x][y] == 'X': 
            break
        points.append(Point(x,y)) 
     
    x = point.x 
    while y > 0:
        y -= 1
        if arr[x][y] == 'X':
            break
        points.append(Point(x,y))
     
    y = point.y
    while y < N-1:
        y += 1
        if arr[x][y] == 'X':
            break
        points.append(Point(x,y))
         
    return points


def solveCastleGrid(N, arr, start, end):
    q = deque([start])
    arr[start.x][start.y] = 0
     
    while q:
        current_point = q.pop()
        current_distance = arr[current_point.x][current_point.y]
         
        points = getPointsFromPoint(N, arr, current_point)
        for p in points:
            if arr[p.x][p.y] == '.':
                arr[p.x][p.y] = current_distance + 1
                q.appendleft(p)
                if p.x == end.x and p.y == end.y:
                    return current_distance + 1
    return -1


if __name__ == '__main__':
    n = int(input())
    grid = []
    for _ in range(n):
        grid_item = list(input())
        grid.append(grid_item)

    startXStartY = input().split()
    startX = int(startXStartY[0])
    startY = int(startXStartY[1])
    goalX = int(startXStartY[2])
    goalY = int(startXStartY[3])
    result = solveCastleGrid(n, grid, Point(startX, startY), Point(goalX, goalY))
    print(str(result))
