
n, k = [int(x) for x in input().split()]

if n == 2:
    print("YES\n1 2\n2 1")
else:
    print("YES\n1 2")
    for i in range(1, n):
        print(i, i+1, sep=" ")
    print(n, 1, sep=" ")
