
n, k = map(int, input().split())
a = list(map(int, input().split()))

if k >= n:
    print("YES")
    for i in range(n):
        print(i + 1, end=' ')
    print()
else:
    colors = [0] * (n + 1)
    count = 0
    for i in range(n):
        if colors[a[i]] == 0:
            colors[a[i]] = i + 1
            count += 1
    if count < k:
        print("NO")
    else:
        print("YES")
        for i in range(n):
            print(colors[a[i]] if colors[a[i]] != 0 else colors[a[i - 1]], end=' ')
        print()
