
import string
# solution

n, k = map(int, input().split())
s = input()

for i in range(len(s)):
    if s[i] in string.ascii_lowercase:
        s = s.replace(s[i], chr(ord(s[i])+k))
print(s)
