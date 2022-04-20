
n, r = map(int, input().split())
a = list(map(int, input().split()))
def is_heated(i):
    for j in range(i - r + 1, i + r):
        if j >= 0 and j < n:
            if a[j] == 1:
                return True
    return False
def is_possible():
    for i in range(n):
        if not is_heated(i):
            return False
    return True
def solve():
    if not is_possible():
        return -1
    ans = 0
    for i in range(n):
        if a[i] == 0:
            ans += 1
            a[i] = 1
            if not is_possible():
                return -1
    return ans

print(solve())
