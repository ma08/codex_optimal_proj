
import math


n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)


def power_of_two(x):
    return math.ceil(math.log2(x)) == math.floor(math.log2(x))


def solve(n, a):
    left = 0
    right = n-1
    res = n

    while left < right:
        if power_of_two(a[left]+a[right]):
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
