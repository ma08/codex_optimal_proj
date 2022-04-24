

H, n = [int(x) for x in input().split()]  # H: ヒーローの体力, n: 攻撃回数
d = [int(x) for x in input().split()]  # d[i]: i回目の攻撃でヒーローの体力が減少する値

for i in range(n):
    H += d[i]
    if H <= 0:
        print(i + 1)
        break
else:
    print(-1)
