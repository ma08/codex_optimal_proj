
n, k = map(int, input().split())

if n == 2:
    print("YES\n1 2\n2 1")
else:
    print("YES\n", end="")
    for i in range(1, n):
        print(i, i+1)
    print(n, 1)
