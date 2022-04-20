
n = int(input())
divisors = list(map(int, input().split()))

x = 1
y = 1

while divisors:
    d = divisors.pop(0)
    if divisors and divisors[0] == d:
        divisors.pop(0)
        x *= d
    else:
        y *= d

print(x, y)
