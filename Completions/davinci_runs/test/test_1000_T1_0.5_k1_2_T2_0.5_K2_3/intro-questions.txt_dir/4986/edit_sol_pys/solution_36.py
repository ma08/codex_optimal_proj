
s = input().strip()
t = input().strip()

for i in range(len(s)):
    if s[i] != t[i]:
        print(s[i], end='')
