import sys
input = sys.stdin.readline


n = int(input())  # 入力
a = list(map(int, input().split()))  # 入力

a.sort(reverse=True)
ans = 0  # 出力
for i in range(n):
    ans += a[i] * (i + 1)


print(ans)
