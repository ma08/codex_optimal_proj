
n = int(input())
a = [int(input()) for i in range(n)]
 
if 0 in a:
    print(0)
else:
    ans = 1
    for i in range(n):
        if ans > 10**18 // a[i]:
            ans = -1
            break
        ans *= a[i]
    print(ans)
