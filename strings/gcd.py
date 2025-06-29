str1 = 'ABABAB'
str2 = 'ABAB'

gcd_len = min(len(str1), len(str2))
while gcd_len > 0:
    gcd = str1[0:gcd_len]

