

n = int(input())
a = list(map(int, input().split()))

def solve(n, a):
    l = 0
    r = 0
    max_len = 0
    while r < n-1:
        if a[r+1] > a[r]:
            r += 1
        else:
            max_len = max(max_len, r-l+1)
            l = r
            r += 1
    max_len = max(max_len, r-l+1)
    return max_len

print(solve(n, a))