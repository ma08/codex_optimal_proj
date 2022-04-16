

s = input().strip().split()
t = input().strip().split()

for i in range(len(s)):
    if s[i] != t[2*i]:
        print(s[i], end='')
