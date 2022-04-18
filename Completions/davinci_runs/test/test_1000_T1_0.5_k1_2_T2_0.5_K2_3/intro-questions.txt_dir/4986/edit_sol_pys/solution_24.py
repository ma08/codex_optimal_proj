

s = input()
t = input()

for i in range(len(s)):
    if s[i] != t[i*2]:
        print(s[i], end='')
