
if k == 2:
    print("YES")
    for i in range(1, n+1):
        print(i, i+1)
    exit()
n, k = [int(x) for x in input().split()]

if n == 2:
    print("YES")
    for i in range(1, n+1):
        print(i, i+1)
    exit()
else:
    print("YES")
    for i in range(1, n):
        print(i, i+1)
    print(n, 1)
