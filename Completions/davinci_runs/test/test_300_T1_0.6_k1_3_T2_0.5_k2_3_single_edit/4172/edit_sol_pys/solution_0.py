
n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 1:
    print(0)
else:
    mi, mx = min(a), max(a)
    ans = abs(mi - mx)
    while k < n:
        ans -= 1
        k += 1
    print(ans)
