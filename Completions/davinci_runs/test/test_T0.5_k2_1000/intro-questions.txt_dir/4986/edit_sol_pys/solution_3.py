
s = input().strip()
t = input().strip()

for i in range(len(s)):
    if s[i] != t[i*2] and s[i] != t[i*2+1]:
        print(s[i], end='')
print()
