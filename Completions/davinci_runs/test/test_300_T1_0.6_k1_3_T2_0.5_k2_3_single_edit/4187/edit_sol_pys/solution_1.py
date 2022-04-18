
n = int(input())
a = list(map(int, input().split()))

best = 0
length = 0

for i in range(n):
    if a[i] == 1:
        length += 1
    else:
        best = max(best, length)
        length = 0

print(best)
