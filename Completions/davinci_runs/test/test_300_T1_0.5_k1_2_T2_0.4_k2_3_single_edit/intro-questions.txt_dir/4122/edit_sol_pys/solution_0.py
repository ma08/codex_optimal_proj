

# Solution1

H, n = map(int, input().split())  # H: ボスの体力, n: 攻撃回数
d = list(map(int, input().split()))  # d: 攻撃力

hp = H  # ボスの体力
minute = 0  # 攻撃した回数

for i in range(n):
    hp += d[i]
    minute += 1
    if hp <= 0:
        print(minute)
        break
else:
    print(-1)
