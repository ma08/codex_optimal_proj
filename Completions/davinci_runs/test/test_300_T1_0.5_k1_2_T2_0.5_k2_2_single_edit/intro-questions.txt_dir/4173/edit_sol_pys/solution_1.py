
q = int(input())

for i in range(q):
    n, a, b = [int(x) for x in input().split()]

    print(min(n * a, n // 2 * b + n % 2 * a))
