

n = int(input())
a = list(map(int, input().split()))
a.sort()


def power_of_two(n): # check if a number is power of 2
    if n == 0:
        return False
    else:
        return n & (n-1) == 0


def solve(n, a):
    l = 0 # left pointer
    r = n-1 # right pointer
    res = n # number of pairs

    while l < r:
        if power_of_two(a[l]+a[r]):
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
