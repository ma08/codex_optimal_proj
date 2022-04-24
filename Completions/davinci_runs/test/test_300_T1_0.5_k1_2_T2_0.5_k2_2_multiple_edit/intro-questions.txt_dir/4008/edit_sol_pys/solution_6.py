n = int(input())
a = [0]*n
b = [0]*n
for i in range(n):
    a[i], b[i] = map(int, input().split())
for i in range(n):
    print(a[i]+b[i])
