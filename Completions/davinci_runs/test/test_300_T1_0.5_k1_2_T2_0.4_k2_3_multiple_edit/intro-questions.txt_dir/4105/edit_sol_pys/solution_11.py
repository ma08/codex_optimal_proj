

n, m = [int(x) for x in input().split()]



if n == 2:
    print("Yes")
    print("1 2\n2 1")
else:
    if m > n:
        print("No")
    else:
        print("Yes")
        for i in range(1, n):
            print(i, i+1)
        print(n, 1)
