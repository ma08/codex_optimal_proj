

A, B = map(int, input().split())

for price in range(1, B+1):
    if int(price * 0.08) == A and int(price * 0.1) == B:  # A = 0.08 * price, B = 0.1 * price
        print(price)
        exit()

print(-1)
