
q = int(input())

for i in range(q):
    n, a, b = [int(x) for x in input().split()]

    if (2 * a) < b:
        print(n * a)
    else:
        print(n // 2 * b + n % 2 * a)
