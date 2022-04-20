

n = int(input())
p = list(map(int, input().split()))

count = 0
for i in range(1, n - 1):
    if p[i] > p[i - 1] and p[i] < p[i + 1]:
        count += 1
    elif p[i] < p[i - 1] and p[i] > p[i + 1]:
        count += 1

print(count)