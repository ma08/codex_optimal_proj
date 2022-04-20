
n, k = [int(x) for x in input().split()]

if n == 2:
    print("NO")
else:
    print("YES")
    if k % 2 == 0:
        for i in range(1, n):
            print(i, i+1)
        print(n, 1)
    else:
        print("1 2")
        for i in range(3, n):
            print(i, i+1)
        print(n, 3)
