import re

s = "axc"
t = "ahbgdc"
sre = s[0]
for i in range(1, len(s)):
    sre += r'.*' + s[i]

print( re.search(sre, t) is not None )


