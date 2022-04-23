

A, B = map(int, input().split())

for price in range(1, B+1):
    if int(price * 0.08) == A and int(price * 0.1) == B: # この辺は0.1以下の小数が切り捨てられてしまうので、上手く動かない
        print(price)
        exit()

print(-1)
