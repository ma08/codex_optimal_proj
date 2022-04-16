
n, k = [int(x) for x in input().split()]

if n == 2 and k == 1:
    print("YES")
    print("1 2")
    print("2 1")
elif n == 2 and k == 2:
    print("YES")
    print("1 1")
    print("2 2")
elif n == 2:
    print("NO")
elif k == 1:
    print("YES")
    for i in range(1, n):
        print(i, i+1)
elif k == 2:
    print("YES")
    for i in range(1, n):
        print(i, i+1)
    print(n, 1)
    for i in range(1, n):
        print(i, i+1)
    print(n, 1)
    print(n, 1)
