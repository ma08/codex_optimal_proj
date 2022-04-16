
n = int(input())
a = list(map(int, input().split()))
total = 0
for i in range(n):
    total += a[i]
print(total)
