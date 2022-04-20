# ABC 073 B


N = int(input())  # 1 <= N <= 100

total = 0
for i in range(N):
    l, r = map(int, input().split())  # 1 <= l <= r <= 10^4
    total += r - l + 1

print(total)
