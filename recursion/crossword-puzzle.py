#!/bin/python3

import math
import os
import random
import re
import sys
from copy import deepcopy
from pprint import pprint
from collections import namedtuple


class WordSlot:
    def __init__(self, row, col, dir, len=None):
        self.row = row
        self.col = col
        self.dir = dir
        self.len = len
        self.word = None

    def __repr__(self):
        return 'WordSlot[row={} col={} dir={} len={}]'.format(
            self.row, self.col, self.dir, self.len)

    def __eq__(self, other):
        return (self.row == other.row) and (self.col == other.col) and (self.dir == other.dir)


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
        s.wordSlot = deepcopy(self.wordSlots)
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
        slot = next(s for s in st.wordSlots if s == slot)
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

    def findFirstEmptyPos():
        for irow in range(len(st.matrix)):
            for icol in range(len(st.matrix[irow])):
                if st.matrix[irow][icol] == '-':
                    return irow, icol
    
    def locateSlot(someRow, someCol):
        # Определить направление слова
        if st.charAt(someRow, someCol-1) == '-' or st.charAt(someRow, someCol+1) == '-':
            dir = 'H'
        elif st.charAt(someRow-1, someCol) == '-' or st.charAt(someRow+1, someCol) == '-':
            dir = 'V'

        # Найти границы слова
        startRow, startCol = someRow, someCol
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

        slot = WordSlot(startRow, startCol, dir)
        endRow, endCol = someRow, someCol
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
            slot.len = endCol - startCol + 1
        else: # Vert
            slot.len = endRow - startRow + 1

        slots.append(slot)

        # Заполнить все позиции слова, кроме пересечений
        cross = []
        for ofs in range(slot.len):
            curRow, curCol = slot.row, slot.col
            if slot.dir == 'H': # Horiz
                curCol += ofs
            else: # Vert
                curRow += ofs

            # Является ли пересечением
            emptyOnVert = (st.charAt(curRow-1, curCol) == '-' or st.charAt(curRow+1, curCol) == '-')
            emptyOnHoriz = (st.charAt(curRow, curCol-1) == '-' or st.charAt(curRow, curCol+1) == '-')
            if (slot.dir == 'H' and emptyOnVert) or (slot.dir == 'V' and emptyOnHoriz):
                cross.append((curRow, curCol))
            else:
                st.matrix[curRow][curCol] = '?'

        # Обработать слова на найденных пересечениях
        for (row, col) in cross:
            locateSlot(row, col)


    emptyRow, emptyCol = findFirstEmptyPos()
    locateSlot(emptyRow, emptyCol)
    return slots


def findWordForSlot(curState):
    curState.print()

    # Находим первый незанятый слот
    slot = next(slot for slot in curState.wordSlots if slot.word is None)
    # Перебираем слова подходящей длины
    for word in (w for w in curState.availWords if len(w) == slot.len):
        if curState.canWordBePutIntoSlot(word, slot):
            nextState = curState.putWordIntoSlot(word, slot)
            nextState.print()
            


# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words):
    # TODO
    st = State.fromList(crossword)
    st.availWords = words.split(';')
    st.wordSlots = findWordSlots(st.copy())
    findWordForSlot(st)

    # st.print()
    return st.toList()




if __name__ == '__main__':
    crossword = []
    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    print('\n'.join(result))
