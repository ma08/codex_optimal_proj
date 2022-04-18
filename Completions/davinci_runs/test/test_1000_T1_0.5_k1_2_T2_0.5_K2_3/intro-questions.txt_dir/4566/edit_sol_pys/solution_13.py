
n = int(input())
a = list(map(int, input().split()))

# 初期化
count = 0
before = 0

for i in range(n):
    if before > a[i]:
        count += before - a[i]
        a[i] = before
    before = a[i]

print(count)
