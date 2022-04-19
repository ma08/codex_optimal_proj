
n = int(input())
divisors = [int(i) for i in input().split()] # list comprehension

divisors.sort()

x = 1 # x = divisors[0]
y = 1 # y = divisors[1]
for i in range(n):
    if i % 2 == 0:
        x *= divisors[i]
    else:
        y *= divisors[i]

print(x, y)
