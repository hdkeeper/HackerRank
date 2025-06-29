word1 = 'abcdef'
word2 = '123'
result = ''

for i in range(0, max(len(word1), len(word2))):
    result += word1[i:i+1] + word2[i:i+1]

print(result)
