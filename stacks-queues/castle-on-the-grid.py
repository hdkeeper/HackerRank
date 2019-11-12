#!/bin/python3

import math
import os
import random
import re
import sys
from collections import namedtuple

Point = namedtuple('Point', 'x y')

DIRECTIONS = [
    # (+x, +y)
    Point(0, -1),   # вверх
    Point(0, 1),    # вниз
    Point(-1, 0),   # влево
    Point(1, 0)     # вправо   
]

def printGrid(grid):
    for row in grid:
        print(''.join(row))

moves = []

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY, stepCount=0):
    def isOpen(x, y):
        return (y >= 0 and y < len(grid) and
            x >= 0 and x < len(grid[y]) and
            grid[y][x] == '.')

    def setGrid(x, y, ch):
        grid[y][x] = ch


    printGrid(grid)
    curX, curY = startX, startY
    setGrid(curX, curY, '+')

    # Выбрать направление для следующего хода
    for dir in DIRECTIONS:
        moveLen = 1
        nextX = curX + dir.x
        nextY = curY + dir.y

        # Проверить соседнюю клетку
        if isOpen(nextX, nextY):
            setGrid(nextX, nextY, '+')
            # Продлить ход на максимальное количество клеток
            while isOpen(nextX + dir.x, nextY + dir.y):
                moveLen += 1
                nextX += dir.x
                nextY += dir.y
                setGrid(nextX, nextY, '+')
                # Проверить, добрались ли мы до места
                if nextX == goalX and nextY == goalY:
                    return stepCount + 1

            # Записать ход
            moves.append(Point(nextX, nextY))
            print(nextX, nextY)

            printGrid(grid)
            subResult = minimumMoves(grid, nextX, nextY, goalX, goalY, stepCount+1)
            if subResult < 0:
                # Ничего не нашли, отмотать один ход
                moves.pop()
                # Убрать отметки последнего хода с грида
                while moveLen > 0:
                    setGrid(nextX, nextY, '.')
                    nextX -= dir.x
                    nextY -= dir.y
                    moveLen -= 1
            else:
                return subResult
            
    # Ходов больше нет
    return (-1)






if __name__ == '__main__':
    '''    
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
    result = minimumMoves(grid, startX, startY, goalX, goalY)
    print(str(result))
    '''

    # Debug mock
    grid = [
        list('.X.'),
        list('.X.'),
        list('...')
    ]
    startX, startY = 0, 0
    goalX, goalY = 0, 2
    result = minimumMoves(grid, startX, startY, goalX, goalY)
    print(str(result))
