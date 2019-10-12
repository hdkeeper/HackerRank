# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s, n = input().split()
s = sorted(s)
n = int(n)
for p in permutations(s, n):
    print(''.join(p))
