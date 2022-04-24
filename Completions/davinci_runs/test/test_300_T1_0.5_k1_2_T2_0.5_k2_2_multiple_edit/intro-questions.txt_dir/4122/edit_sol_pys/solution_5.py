# Solution

h, n = map(int, input().split()) # 入力を2つに分ける
d = list(map(int, input().split())) # 入力をリストにする

hp = h # 始まりのhp
minute = 0

for i in range(n):
    hp += d[i]
    minute += 1
    if hp <= 0: # hpが0以下になったら終了
        print(minute)
        break
else:
    print(-1)
