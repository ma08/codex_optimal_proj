
# SOLUTION
n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 1:
    print(0)
else:
    mi = min(a)
    mx = max(a)
    if mi == mx:
        print(0)
    else:
        ans = abs(mi - mx)
        while k < n:
            ans -= 1
            k += 1
        print(ans)
