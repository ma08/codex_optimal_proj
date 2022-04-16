

n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

k = int(input())

for i in range(n):
    if a[i][k] == 1:
        print(*a[i])
