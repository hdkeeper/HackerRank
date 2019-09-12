#!/bin/python3

import os
import sys


class Node(object):
    def __init__(self, index, depth):
        self.index = index
        self.depth = depth
        self.left = None
        self.right = None

    def __repr__(self):
        return '<Node i={} d={} {} {}>'.format(
            self.index,
            self.depth,
            '+' if bool(self.left) else '-',
            '+' if bool(self.right) else '-')


def walk(cur: Node):
    log = []
    if cur.left:
        log.extend(walk(cur.left))
    log.append(cur.index)
    if cur.right:
        log.extend(walk(cur.right))
    return log


#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    #
    # Write your code here.
    #
    result = []

    # Build a tree first
    treeRoot = Node(1, 1)
    treeIndex = { 1: treeRoot }
    for i in range(0, len(indexes)):
        left, right = indexes[i]
        parent = treeIndex[i+1]
        if left > 0:
            treeIndex[left] = parent.left = Node(left, parent.depth + 1)
        if right > 0:
            treeIndex[right] = parent.right = Node(right, parent.depth + 1)
    
    for k in queries:
        # Swap the tree
        for cur in treeIndex.values():
            if cur.depth % k == 0:
                cur.left, cur.right = cur.right, cur.left
                # print(cur)

        result.append(walk(treeRoot))

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
