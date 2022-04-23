

A, B = map(int, input().split())

for price in range(1, B+1):
    if int(price * 0.08) == A and int(price * 0.1) == B:  # 小数点以下が切り捨てられるので、それを利用して計算する
        print(price)
        exit()

print(-1)
