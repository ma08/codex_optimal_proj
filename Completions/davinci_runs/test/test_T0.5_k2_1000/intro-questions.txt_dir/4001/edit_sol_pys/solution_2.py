N = int(input())
divisors = list(map(int, input().split()))
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
