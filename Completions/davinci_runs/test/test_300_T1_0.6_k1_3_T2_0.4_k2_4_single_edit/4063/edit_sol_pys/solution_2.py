import sys

N = int(sys.stdin.readline().rstrip())  # 数字の数
d = list(map(int, sys.stdin.readline().rstrip().split()))  # 数字のリスト

# print(N)
# print(d)

count = 0

for i in range(1, N):
    if sum(d[:i]) == sum(d[i:]):
        count += 1

print(count)
