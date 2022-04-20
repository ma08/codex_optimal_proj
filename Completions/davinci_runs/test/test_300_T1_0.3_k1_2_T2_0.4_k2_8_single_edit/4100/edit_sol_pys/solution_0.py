

n, k, q = map(int, input().split())  # 複数数値入力
a = [int(input()) for _ in range(q)]  # 複数数値入力

players = [k] * n  # リストの要素をk個作る

for i in range(q):
    for j in range(n):
        if j + 1 != a[i]:
            players[j] -= 1

for i in range(n):
    if players[i] <= 0:
        print("No")
    else:
        print("Yes")
