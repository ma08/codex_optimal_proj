
N = int(input())
divisors = list(map(int, input().split()))
x = divisors[0]
y = divisors[1]
for i in range(N):
    x *= divisors[i]
    y *= divisors[i]
    if x == y:
        break
print(x, y)
