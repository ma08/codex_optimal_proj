

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

if len(set(a)) < k:
    print("NO")
else:
    ans = [0] * n
    for i in range(n):
        ans[a[i] - 1] = i % k + 1
    print("YES")
    for i in range(n):
        print(ans[i], end=" ")
