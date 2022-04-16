n = int(input())
l = [0] * n
d = list(map(int, input().split()))[1:]

for i, j in enumerate(d):
    l[j-1] = i+1

print(' '.join(map(str, l)))
