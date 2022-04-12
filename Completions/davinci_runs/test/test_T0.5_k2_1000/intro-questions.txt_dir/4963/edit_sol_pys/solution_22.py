n = int(input())
l = [0] * (n+1)
d = list(map(int, input().split()))

for i in range(n):
    l[d[i]] = i+1

print(' '.join(map(str, l)))
