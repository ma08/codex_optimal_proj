

n, d, k = map(int, input().split())

if n - 1 <= k * (d - 1):
    print("YES")
    for i in range(2, n + 1):
        print(i, 1)
    for i in range(2, d):
        for j in range(1, k + 1):
            if i + j <= n:
                print(i, i + j)
else:
    print("NO")