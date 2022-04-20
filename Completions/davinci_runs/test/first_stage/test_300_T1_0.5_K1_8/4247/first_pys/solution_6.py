

n = int(input())
p = list(map(int, input().split()))

count = 0
for i in range(1, n - 1):
    if p[i] != min(p[i - 1:i + 2]) and p[i] != max(p[i - 1:i + 2]):
        count += 1

print(count)