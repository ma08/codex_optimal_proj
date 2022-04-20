

n = int(input())
p = list(map(int, input().split()))

count = 0
for i in range(1, n - 1):
    if p[i - 1] > p[i] and p[i + 1] > p[i]:
        count += 1
    elif p[i - 1] < p[i] and p[i + 1] < p[i]:
        count += 1

print(count)