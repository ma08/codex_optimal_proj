

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k > n:
    print("NO")
else:
    colors = [0] * n
    colors[0] = 1
    for i in range(1, n):
        if a[i] == a[i-1]:
            colors[i] = colors[i-1]
        else:
            colors[i] = colors[i-1] + 1
            if colors[i] > k:
                colors[i] = 1
    print("YES")
    print(*colors)