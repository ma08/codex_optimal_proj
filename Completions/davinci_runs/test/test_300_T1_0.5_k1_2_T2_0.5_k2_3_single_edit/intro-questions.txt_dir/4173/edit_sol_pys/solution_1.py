
# Solution
for _ in range(int(input())):
    n, a, b = map(int, input().split())
    x = n//2
    y = n % 2
    cost = x * min(a*2, b) + y * a
    print(cost)
