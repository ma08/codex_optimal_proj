
n, k = map(int, input().split())

if n % 2 == 1:
    print("NO")
else:
    print("YES")
    for i in range(1, n // 2 + 1, 2):
        print(i, k - i + 1, i + 1, k - i)
