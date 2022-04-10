

n, k = map(int, input().split())
if k == 1:
    print("NO")
    exit()
if n == 2:
    print("YES")
    print(1, 2)
    print(2, 1)
    exit()
if n % 2 == 0:
    print("YES")
    for i in range(1, n + 1, 2):
        print(i, i + 1)
        print(i + 1, i)
else:
    print("YES")
    print(1, 2)
    print(2, 3)
    print(3, 1)
    for i in range(4, n + 1, 2):
        print(i, i + 1)
        print(i + 1, i)