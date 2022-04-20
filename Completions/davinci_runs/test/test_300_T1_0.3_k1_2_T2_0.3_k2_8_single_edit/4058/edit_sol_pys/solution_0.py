
n, r = map(int, input().split())
a = list(map(int, input().split()))

def is_heated(i, a):
    for j in range(max(0, i - r + 1), min(n, i + r)):
        if a[j] == 1:
            return True
    return False 

def is_possible(a):
    for i in range(n):
        if not is_heated(i, a):
            return False
    return True

def solve(a):
    if not is_possible(a):
        return -1
    ans = 0
    for i in range(n):
        if a[i] == 0:
            ans += 1
            a[i] = 1
            if not is_possible(a):
                return -1
    return ans

print(solve())
