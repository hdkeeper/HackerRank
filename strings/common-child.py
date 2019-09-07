# Enter your code here. Read input from STDIN. Print output to STDOUT
import time

def commonChild(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
 
    return lengths[-1][-1]


start_time = time.time()

s1 = input()
s2 = input()
result = commonChild(s1, s2)
print(result)

# print('Elapsed time %f s' % (time.time() - start_time))
