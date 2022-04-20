

n = int(input())
a = list(map(int, input().split()))

def solve():
    l = 0
    r = 1
    s = a[l]
    count = 0
    while r < n:
        if s == 0:
            count += 1
            l = r
            r += 1
            s = a[l]
        elif s > 0:
            if a[r] < 0:
                r += 1
                s += a[r - 1]
            else:
                while s > 0:
                    s -= a[l]
                    l += 1
        else:
            if a[r] > 0:
                r += 1
                s += a[r - 1]
            else:
                while s < 0:
                    s -= a[l]
                    l += 1
    return count

print(solve())