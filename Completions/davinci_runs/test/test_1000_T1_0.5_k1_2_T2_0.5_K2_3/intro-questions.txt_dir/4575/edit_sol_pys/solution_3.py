
n = int(input())
d, x = map(int, input().split())
a = [int(input()) for i in range(n)]

for i in range(n):
    x += (d - 1) // a[i] + 1

print(x)
