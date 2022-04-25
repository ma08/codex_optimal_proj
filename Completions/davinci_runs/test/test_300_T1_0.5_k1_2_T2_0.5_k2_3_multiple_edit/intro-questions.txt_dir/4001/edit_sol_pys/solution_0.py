N = int(input())
divisors = list(map(int, input().split()))

x = divisors[0]
y = divisors[1]
for i in range(N):
    if divisors[i] == 1:
        continue
    if i < N - 1:
        if divisors[i] == divisors[i + 1]:
            x *= divisors[i]
            i += 1
            continue
    else:
        y *= divisors[i]









print(x, y)
