

A, B = map(int, input().split())

for price in range(1, B+1):
    if int(price * 0.08) == A and int(price * 0.1) == B:  # 価格がA,Bになるものを探す
        print(price)
        exit()

print(-1)
