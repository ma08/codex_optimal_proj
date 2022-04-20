

# put your python code here
q = int(input())
for i in range(q):
    n, a, b = [int(x) for x in input().split()]
    if n % 2 == 0:
        print(min(n // 2 * a, n // 2 * b))
    else:
        print(min(n // 2 * b + a, n // 2 * a + b))