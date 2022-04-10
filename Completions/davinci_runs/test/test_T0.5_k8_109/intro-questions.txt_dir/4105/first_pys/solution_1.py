

n, k = map(int, input().split())

if k == 1:
    print("NO")
    exit()

if n % 2 == 0:
    print("YES")
    for i in range(n):
        if i % 2 == 0:
            print(1, 2)
        else:
            print(2, 1)
else:
    if k < 3:
        print("NO")
        exit()
    print("YES")
    for i in range(n):
        if i % 2 == 0:
            print(1, 2)
        else:
            print(2, 3)
    print(3, 1)