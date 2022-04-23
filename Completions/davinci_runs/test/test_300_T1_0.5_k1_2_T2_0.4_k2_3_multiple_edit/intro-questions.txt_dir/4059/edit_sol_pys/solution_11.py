import sys
input = sys.stdin.readline


n = int(input())  # 問題の数
p = list(map(int, input().split()))  # 問題の難易度
q = list(map(int, input().split()))  # 正解した問題の難易度

ans = 0  # 正解数
for i in range(n):
    if p[i] == q[i]:  # 問題の難易度と正解した問題の難易度が一致していれば
        ans += 1

print(ans)
