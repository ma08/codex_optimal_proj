
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [0] * (n + 1)
for i in range(n):
    c[(a[i] + b[i]) % n] += 1    # c[i] is count of (a[i]+b[i])%n

c[0] = c[0] - 1
for i in range(n + 1):
    for j in range(c[i]):
        print(i, end=" ")
