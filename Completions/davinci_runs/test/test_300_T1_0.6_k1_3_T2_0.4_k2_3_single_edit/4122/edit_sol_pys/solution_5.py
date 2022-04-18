

# Write your code here
h, n = [int(x) for x in input().split()]  # h = 初期HP, n = 攻撃回数
d = [int(x) for x in input().split()]  # d = 攻撃力

hp = h  # 初期HPを保存
for i in range(n):
    hp -= d[i]
    if hp <= 0:
        print(i+1)
        break
else:
    print(-1)
