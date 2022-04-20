

A, B = map(int, input().split())

for price in range(1, B+1):
    if int(price * 0.08) == A and int(price * 0.1) == B:  # 小数点以下切り捨て
        print(price)
        exit()

print(-1)
