

q = int(input())

for i in range(q):
    n, a, b = map(int, input().split())
    if n % 2 == 0:
        print(n // 2 * min(a, b))
    else:
        print(min(a, b) + (n - 1) // 2 * min(a, b))