

q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = -1
    if n == 1:
        ans = a[0]
    else:
        for i in range(1, k+1):
            if a[0] + i <= a[-1] - i:
                ans = a[0] + i
                break
    print(ans)
