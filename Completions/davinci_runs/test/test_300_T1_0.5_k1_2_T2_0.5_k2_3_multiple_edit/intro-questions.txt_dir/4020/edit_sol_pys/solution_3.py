
n = int(input())
s = list(map(int, input().split()))

s.sort()

for i in range(n):
    s[i] = str(s[i])

print(' '.join(s))
