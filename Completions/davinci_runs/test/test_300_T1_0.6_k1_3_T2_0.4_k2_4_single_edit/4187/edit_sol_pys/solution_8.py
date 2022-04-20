
n = int(input())
a = list(map(int, input().split()))
a = [a[-1]] + a + [a[0]]

best = 0
length = 0

for i in range(n + 1):
    if a[i] == 1:
        length += 1
    else:
        best = max(best, length)
        length = 0

print(best)
