import math

x, k, d = map(int,input().split())

if k*d > abs(x):
    k = abs(x) // d # 切り捨て除算
    x -= k*d # 切り捨て除算した分だけxを減らす
    if abs(x) % d == 0:
        print(abs(x))
    else:
        print(abs(x) - d) # そのままだと0になるので1つ戻す
else:
    print(abs(x - k*d))
