

N = int(input())
divisors = list(map(int, input().split()))
x = 1
y = 1
i = 0
while i < N:
    if divisors[i] == 1:
        continue
    if i + 1 < N and divisors[i] == divisors[i + 1]:
        x *= divisors[i]
        i += 1
    else:
        y *= divisors[i]
print(x, y)
