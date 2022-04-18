
n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(1, d+1, a[i]):
        x += 1

print(x)
