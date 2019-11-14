#!/bin/python3

import math
import os
import random
import re
import sys
from copy import deepcopy
from pprint import pprint


class WordSlot:
    def __init__(self, row, col, dir, len=None):
        self.row = row
        self.col = col
        self.dir = dir
        self.len = len
        self.word = None

    def __repr__(self):
        if self.word is not None:
            return 'WordSlot[row={} col={} dir={} len={} word={}]'.format(self.row, self.col, self.dir, self.len, self.word)
        return 'WordSlot[row={} col={} dir={} len={}]'.format(self.row, self.col, self.dir, self.len)

    def __eq__(self, other):
        return (self.row == other.row) and (self.col == other.col) and (self.dir == other.dir)

    def inside(self, row, col):
        if self.dir == 'H': # Horiz
            return (row == self.row) and (self.col <= col) and (col < self.col+self.len)
        else: # Vert
            return (col == self.col) and (self.row <= row) and (row < self.row+self.len)


class State:
    def __init__(self):
        self.matrix = []
        self.wordSlots = []
        self.availWords = []

    def print(self):
        pprint(self.toList())
        pprint(self.wordSlots)
        pprint(self.availWords)

    @staticmethod
    def fromList(aList):
        s = State()
        s.matrix = [list(s) for s in aList]
        return s
    
    def toList(self):
        return [''.join(row) for row in self.matrix]

    def copy(self):
        s = State()
        s.matrix = deepcopy(self.matrix)
        s.wordSlots = deepcopy(self.wordSlots)
        s.availWords = deepcopy(self.availWords)
        return s

    def charAt(self, row, col):
        if row < 0 or row >= len(self.matrix):
            return '@'
        if col < 0 or col >= len(self.matrix[row]):
            return '@'
        return self.matrix[row][col]

    def canWordBePutIntoSlot(self, word, slot):
        if word not in self.availWords:
            return False
        if slot.word is not None:
            return False
        if len(word) != slot.len:
            return False
        
        # Проверяем соответствие букв
        for ofs in range(slot.len):
            row, col = slot.row, slot.col
            if slot.dir == 'H': # Horiz
                col += ofs
            else: # Vert
                row += ofs
            if self.matrix[row][col] == '-':
                continue
            if self.matrix[row][col] != word[ofs]:
                return False
        
        return True

    def putWordIntoSlot(self, word, slot):
        st = self.copy()
        slot = next(s for s in st.wordSlots if slot == s)
        slot.word = word
        st.availWords.remove(word)
        for ofs in range(slot.len):
            row, col = slot.row, slot.col
            if slot.dir == 'H': # Horiz
                col += ofs
            else: # Vert
                row += ofs
            st.matrix[row][col] = word[ofs]

        return st
        

def findWordSlots(st):
    slots = []
    for irow in range(len(st.matrix)):
        for icol in range(len(st.matrix[irow])):
            if st.charAt(irow, icol) != '-':
                continue

            # Проверить, не входит ли эта клетка в слот, определенный ранее
            alreadyInSlot = False
            for slot in slots:
                if slot.inside(irow, icol):
                    alreadyInSlot = True
                    break
            if alreadyInSlot:
                continue

            # Определить направление слова
            if st.charAt(irow, icol+1) == '-':
                dir = 'H'
            elif st.charAt(irow+1, icol) == '-':
                dir = 'V'

            # Найти начало слова
            startRow, startCol = irow, icol
            while True:
                if dir == 'H': # Horiz
                    if st.charAt(startRow, startCol-1) != '-':
                        break
                    else:
                        startCol -= 1
                else: # Vert
                    if st.charAt(startRow-1, startCol) != '-':
                        break
                    else:
                        startRow -= 1

            # Найти конец слова
            newSlot = WordSlot(startRow, startCol, dir)
            endRow, endCol = newSlot.row, newSlot.col
            while True:
                if dir == 'H': # Horiz
                    if st.charAt(endRow, endCol+1) != '-':
                        break
                    else:
                        endCol += 1
                else: # Vert
                    if st.charAt(endRow+1, endCol) != '-':
                        break
                    else:
                        endRow += 1

            if dir == 'H': # Horiz
                newSlot.len = endCol - newSlot.col + 1
            else: # Vert
                newSlot.len = endRow - newSlot.row + 1

            slots.append(newSlot)

    return slots


def findWordForSlot(curState):
    # curState.print()
    if len(curState.availWords) == 0:
        return curState

    # Находим первый незанятый слот
    slot = next(slot for slot in curState.wordSlots if slot.word is None)
    
    # Перебираем слова подходящей длины
    for word in (w for w in curState.availWords if len(w) == slot.len):
        if curState.canWordBePutIntoSlot(word, slot):
            # Вписать это слово и продолжить поиск
            nextState = findWordForSlot(curState.putWordIntoSlot(word, slot))
            if nextState is not None:
                return nextState

    # Подходящих слов нет
    return None


# Complete the crosswordPuzzle function below.
def solveCrosswordPuzzle(crossword, words):
    init = State.fromList(crossword)
    init.availWords = words.split(';')
    init.wordSlots = findWordSlots(init.copy())
    # init.print()
    solved = findWordForSlot(init)
    return solved.toList()


if __name__ == '__main__':
    crossword = []
    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()
    result = solveCrosswordPuzzle(crossword, words)
    print('\n'.join(result))
