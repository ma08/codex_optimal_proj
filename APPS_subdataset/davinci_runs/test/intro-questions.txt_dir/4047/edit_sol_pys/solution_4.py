
n = int(input())
x = list(map(int, input().split()))

x.sort()
c = 0
for i in range(1, n):
    c += abs(x[i] - x[i - 1])

print(c)
