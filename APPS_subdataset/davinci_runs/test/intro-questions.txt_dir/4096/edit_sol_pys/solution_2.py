

def check(n, m, a, b):
    a = sorted(a, reverse=True)
    for i in range(1, n+1):
        if sum(a[:i]) >= m:
            return i
    return -1

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(check(n, m, a, b))
