from functools import cmp_to_key

def str_cmp(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return '%s %d' % (self.name, self.score)
        
    def comparator(a, b):
        res = b.score - a.score
        if res == 0:
            res = str_cmp(a.name, b.name)
        return res


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
