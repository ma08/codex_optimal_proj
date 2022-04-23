n = int(input())
a = list(map(int, input().split()))

s = set(a)

for i in range(n):
    s.discard(a[i])

print(n-len(s))
