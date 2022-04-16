# https://atcoder.jp/contests/abc146/tasks/abc146_a

n = int(input())
p = list(map(int, input().split()))

count = 0
for i in range(1, n - 1):
    if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
        count += 1
print(count)
