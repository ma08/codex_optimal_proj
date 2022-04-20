

n = int(input())

# 高さの最大値を求める
max_h = 0
for i in range(n):
    x,y,h = map(int,input().split())
    if h > max_h:
        max_h = h

# 高さの最大値を初期値として、高さが0になるまで探索
# 高さが0になった時点で、そのポイントが中心となる
for x in range(101):
    for y in range(101):
        H = max_h - abs(x) - abs(y)
        if H <= 0:
            print(x,y,max_h)
            exit()