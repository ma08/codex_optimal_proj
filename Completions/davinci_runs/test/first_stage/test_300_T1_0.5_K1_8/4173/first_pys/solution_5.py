

# SOLUTION

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    print(min(n * a, n // 2 * b + n % 2 * a))