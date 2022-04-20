

# 入力
X, N = map(int, input().split())
p = [int(i) for i in input().split()]

# 計算
for i in range(1, 101):
    if i not in p:
        if abs(X - i) < abs(X - ans):
            ans = i

# 出力
print(ans)