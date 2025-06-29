s = "leetcode"

all_vowels = set('aeiou')
def is_vowel(c):
    return c.lower() in all_vowels

backward_vowels = list(reversed(list(filter(is_vowel, s))))
res = ''
iv = 0
for i in range(0, len(s)):
    if is_vowel(s[i]):
        res += backward_vowels[iv]
        iv += 1
    else:
        res += s[i]

print(res)
