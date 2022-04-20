

n = int(input())
a = list(map(int, input().split()))
a.sort()

def solve(n, a):
    l = 0
    r = n-1
    res = n

    while l < r:
        if a[l] + a[r] == 0:
            res -= 1
            l += 1
            r -= 1
        else:
            if a[l] > a[r]:
                r -= 1
            else:
                l += 1
    return res

print(solve(n, a))
