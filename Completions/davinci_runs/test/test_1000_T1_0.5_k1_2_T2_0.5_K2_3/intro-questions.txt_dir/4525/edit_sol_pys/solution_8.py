
n = int(input())

if n == 2:
    print("NO")
else:
    print("YES")
    for i in range(1, (n // 2) + 1):
        print(2 * i, end=" ")
    for i in range(1, (n // 2) + 1):
        print(2 * i - 1, end=" ")
    print()
