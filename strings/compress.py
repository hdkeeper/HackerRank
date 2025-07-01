chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

res = []
last = None
for c in chars:
    if last is not None and c == last[0]:
        last[1] += 1
    else:
        last = [c, 1]
        res.append(last)

def flatten(e) -> str:
    s = e[0]
    if e[1] > 1:
        s += str(e[1])
    return s

res = ''.join(map(flatten, res))

print(res)
