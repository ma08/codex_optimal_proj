import sys
input = sys.stdin.readline


n = int(input())  # 入力
x = list(map(int, input().split()))  # 入力

x.sort()  # ソート

ans = 0  # 初期化
for i in range(1, n):
    if x[i] - x[i-1] > 1:
        ans += x[i] - x[i-1] - 1

print(ans)
