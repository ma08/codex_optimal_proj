

def check(n, h, l, r, a):
    good = 0
    for i in range(1, n):
        if (a[i] <= r and a[i] >= l):
            good += 1
        if (a[i] < r):
            a[i] += 1
        else:
            a[i] -= 1
    return good

n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))
print(check(n, h, l, r, a))