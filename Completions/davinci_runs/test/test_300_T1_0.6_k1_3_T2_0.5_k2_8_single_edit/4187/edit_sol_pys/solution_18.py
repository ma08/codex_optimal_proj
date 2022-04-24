
n = int(input())
a = list(map(int, input().split()))
a.append(a[0])
a.append(a[1])

best = 0
length = 0

for i in range(n + 2):
    if a[i] == 1 and a[i + 1] == 1:
        best = max(best, length)
        length += 1
    else:
        best = max(best, length)
        length = 0

print(best)
