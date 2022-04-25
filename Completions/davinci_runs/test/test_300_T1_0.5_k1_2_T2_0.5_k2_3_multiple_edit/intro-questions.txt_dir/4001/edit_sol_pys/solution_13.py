N = int(input())
divisors = list(map(int, input().split()))
x, y = 1, 1
for i in range(N):
    if divisors[i] == 1:
        continue
    if divisors[i] == divisors[i + 1] and i != N - 1:
        x *= divisors[i]
    else:
        y *= divisors[i]









print(x, y)
