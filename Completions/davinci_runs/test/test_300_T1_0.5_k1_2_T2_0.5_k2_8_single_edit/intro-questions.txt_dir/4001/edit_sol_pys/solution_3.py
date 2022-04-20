
N = int(input())
divisors = list(map(int, input().split()))
x = divisors[0]
y = divisors[1]
for i in range(N):
    if divisors[i] % 2 == 0:
        x *= divisors[i + 1]
        x *= divisors[i]
        y *= divisors[i + 1]
    else:
        y *= divisors[i]
print(x, y)
