from collections import Counter

input()
shoeSizes = Counter(map(int, input().split()))

customerCount = int(input())
total = 0
for i in range(customerCount):
    size, price = list(map(int, input().split()))
    if shoeSizes[size] > 0:
        shoeSizes[size] -= 1
        total += price

print(total)
