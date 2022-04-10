

def solve(n, k, a):
    a.sort()
    if k == 0:
        return a[0] - 1
    if a[0] == 1:
        return -1
    for i in range(n - 1):
        if a[i + 1] - a[i] > 1:
            return a[i] + 1
    return a[n - 1] + 1


k = int(input())
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
