

N = int(input())  # N = 10

count = 0
for a in range(1, N+1):  # 1 <= a <= 10
    for b in range(1, N+1):  # 1 <= b <= 10
        c = N - a*b  # c = 10 - a*b
        if c > 0:  # cが正の整数の時
            count += 1

print(count)
