
N = int(input())
divisors = list(map(int, input().split()))

if N == 1:
    print(divisors[0], divisors[0])
elif N == 2:
    print(divisors[0], divisors[1])
else:
    x = 1
    y = 1
    for i in range(N):
        if divisors[i] == 1:
            continue
        if divisors[i] == divisors[i + 1]:
            x *= divisors[i]
            i += 1
        else:
            y *= divisors[i]
    print(x, y)
