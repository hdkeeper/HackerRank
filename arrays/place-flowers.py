flowerbed = [1,0,0,0,1]
n = 2

def is_available(i):
    return not ( \
        flowerbed[i] == 1 or \
        (i > 0 and flowerbed[i-1] == 1) or \
        (i < len(flowerbed)-1 and flowerbed[i+1] == 1)
    )

for i in range(0, len(flowerbed)):
    if (is_available(i)):
        flowerbed[i] = 1
        n -= 1
        if (n == 0):
            print(True)

print(False)
