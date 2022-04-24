

H, n = [int(x) for x in input().split()]  # 初期値、魔法の数
d = [int(x) for x in input().split()]    # 魔法の効果

for i in range(n):
    H += d[i]
    if H <= 0:
        print(i + 1)
        break
else:
    print(-1)
