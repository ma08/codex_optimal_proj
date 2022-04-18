

N, W = map(int, input().split())
#N, W = 5, 5
wv = list(map(int, input().split()))
#wv = [3, 1, 2, 1, 1]

count = 0  # 入れることができる商品の数
value = 0  # 重さの総和

while W > 0:
    if wv[count] <= W:
        W -= wv[count]
        count += 1
    else:
        break

print(count)
