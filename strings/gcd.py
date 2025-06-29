str1 = 'ABCABC'
str2 = 'ABC'

gcd_len = min(len(str1), len(str2))
while gcd_len > 0:
    if len(str1) % gcd_len == 0 and len(str2) % gcd_len == 0:
        gcd = str1[0:gcd_len]
        n1 = len(str1) // gcd_len
        n2 = len(str2) // gcd_len
        if gcd * n1 == str1 and gcd * n2 == str2:
            print(gcd)

    gcd_len -= 1


