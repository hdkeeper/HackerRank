#!/bin/python3

import math
import os
import random
import re
import sys
from copy import deepcopy
from pprint import pprint


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({},{})'.format(self.x, self.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, n):
        return Vector(self.x * n, self.y * n)

    def asDir(self):
        if self.x == 1 and self.y == 0:
            return 'H'
        elif self.x == 0 and self.y == 1:
            return 'V'
        raise RuntimeError('Invalid dir')
    
    def copy(self):
        return Vector(self.x, self.y)

V = Vector


class WordSlot:
    def __init__(self, start, dir, len=None):
        self.start = start.copy()
        self.dir = dir.copy()
        self.len = len
        self.word = None

    def __repr__(self):
        if self.word is not None:
            return 'WordSlot[start={} dir={} len={} word={}]'.format(self.start, self.dir.asDir(), self.len, self.word)
        return 'WordSlot[start={} dir={} len={}]'.format(self.start, self.dir.asDir(), self.len)

    def __eq__(self, other):
        return (self.start == other.start) and (self.dir == other.dir)

    @property
    def finish(self):
        return self.start + (self.dir * (self.len-1))

    def inside(self, pos):
        if self.dir.asDir() == 'H':
            return (pos.y == self.start.y) and (self.start.x <= pos.x) and (pos.x <= self.finish.x)
        else:
            return (pos.x == self.start.x) and (self.start.y <= pos.y) and (pos.y <= self.finish.y)


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

    def charAt(self, pos):
        if pos.y < 0 or pos.y >= len(self.matrix):
            return '@'
        if pos.x < 0 or pos.x >= len(self.matrix[pos.y]):
            return '@'
        return self.matrix[pos.y][pos.x]

    def canWordBePutIntoSlot(self, word, slot):
        if word not in self.availWords:
            return False
        if slot.word is not None:
            return False
        if len(word) != slot.len:
            return False
        
        # Проверяем соответствие букв
        for ofs in range(slot.len):
            pos = slot.start + (slot.dir * ofs)
            if self.charAt(pos) == '-':
                continue
            if self.charAt(pos) != word[ofs]:
                return False
       
        return True

    def putWordIntoSlot(self, word, slot):
        st = self.copy()
        slot = next(s for s in st.wordSlots if slot == s)
        slot.word = word
        st.availWords.remove(word)
        for ofs in range(slot.len):
            pos = slot.start + (slot.dir * ofs)
            st.matrix[pos.y][pos.x] = word[ofs]

        return st
        

def findWordSlots(st):
    slots = []
    pos = V(0, 0)
    for pos.y in range(len(st.matrix)):
        for pos.x in range(len(st.matrix[pos.y])):
            if st.charAt(pos) != '-':
                continue

            # Проверить, не входит ли эта клетка в слот, определенный ранее
            alreadyInSlot = False
            for slot in slots:
                if slot.inside(pos):
                    alreadyInSlot = True
                    break
            if alreadyInSlot:
                continue

            # Определить направление слова
            if st.charAt(pos + V(1,0)) == '-':
                dir = V(1,0)
            elif st.charAt(pos + V(0,1)) == '-':
                dir = V(0,1)

            # Найти начало слова
            start = pos
            while True:
                if st.charAt(start - dir) != '-':
                    break
                else:
                    start -= dir

            # Найти конец слова
            newSlot = WordSlot(start, dir, 1)
            finish = start
            while True:
                if st.charAt(finish + dir) != '-':
                    break
                else:
                    finish += dir
                    newSlot.len += 1

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
