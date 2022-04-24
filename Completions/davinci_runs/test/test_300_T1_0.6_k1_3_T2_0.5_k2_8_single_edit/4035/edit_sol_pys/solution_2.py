
A, B = map(int, input().split())

for price in range(1, B+1):
    if int(price * 0.08) == A and int(price * 0.1) == B:  # 両方の条件を満たすときにpriceを出力して終了
        print(price)
        exit()

print(-1)
