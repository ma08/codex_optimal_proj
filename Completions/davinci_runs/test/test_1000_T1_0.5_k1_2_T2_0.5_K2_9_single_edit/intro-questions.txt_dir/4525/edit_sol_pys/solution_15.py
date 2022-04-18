

t = int(input())

for _ in range(t):
    n = int(input())
    if n == 2:
        print("NO")
    else:
        print("YES")
        for i in range(1, n + 1):
            if i % 2 == 0:
                print(i, end=" ")
        for i in range(1, n + 1):
            if i % 2 != 0:
                print(i, end=" ")
        print()
