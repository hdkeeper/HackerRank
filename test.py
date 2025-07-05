# Найди в строке и выведи в консоль первый не повторяющийся символ
s = 'abracadabrax'

def getFirst(s: str) -> str:
    cnt = {}
    for c in s:
        cnt[c] = cnt.get(c, 0) + 1

    for c in s:
        if cnt[c] == 1:
            return c
        
    return ''

print(getFirst(s))

