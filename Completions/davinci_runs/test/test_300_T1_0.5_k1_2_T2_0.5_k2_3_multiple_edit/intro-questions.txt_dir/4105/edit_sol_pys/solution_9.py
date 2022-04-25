
n, k = [int(x) for x in input().split()]

if n == 2:
    print("NO")
else:
    if k == 1:
        print("YES")
        for i in range(1, n):
            print(i, i + 1)
        print(n, 1)
    else:
        print("NO")
