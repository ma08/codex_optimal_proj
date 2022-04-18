

# Solution

H, n = map(int, input().split())  # 入力はHとn
d = list(map(int, input().split()))  # 入力はn個の数字

hp = H
minute = 0

for i in range(n):
    hp += d[i]
    minute += 1
    if hp <= 0:
        print(minute)
        break
else:
    print(-1)
