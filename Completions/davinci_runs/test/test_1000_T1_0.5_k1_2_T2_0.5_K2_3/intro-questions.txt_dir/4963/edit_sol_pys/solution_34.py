n = int(input())
l = [1] * n
d = list(map(int, input().split()))

for i in range(1, n):
    l[d[i-1]] = i

print(' '.join(map(str, l[1:])))
