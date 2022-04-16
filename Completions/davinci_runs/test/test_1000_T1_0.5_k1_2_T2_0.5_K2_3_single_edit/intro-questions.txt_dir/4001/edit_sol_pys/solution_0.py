
N = int(input())
divisors = list(map(int, input().split()))

divisors.sort()

x, y = 1, 1
for i in range(N):
    if divisors[i] == 1:
        continue
    if i + 1 < N and divisors[i] == divisors[i + 1]:
        x *= divisors[i]
        i += 1
    else:
        y *= divisors[i]
print(x, y)
