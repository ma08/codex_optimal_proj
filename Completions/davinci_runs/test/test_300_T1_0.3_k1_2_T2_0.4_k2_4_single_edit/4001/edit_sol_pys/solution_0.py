
n = int(input())
divisors = [int(i) for i in input().split()]

divisors.sort()

x = 1
y = 1
for i in range(n):
    if i % 2 == 0:
        x *= divisors[i]
    else:
        y *= divisors[i]

print(x, y)
