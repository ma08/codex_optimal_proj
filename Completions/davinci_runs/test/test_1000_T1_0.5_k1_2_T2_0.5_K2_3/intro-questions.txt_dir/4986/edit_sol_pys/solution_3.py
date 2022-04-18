
s = input().strip().split()
t = input().strip().split()

for i in range(len(s)-1):
    if s[i] not in t:
        print(s[i], end=' ')
