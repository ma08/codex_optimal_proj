

def is_valid(p, n):
    if n <= 2:
        return True
    if p[n-1] - p[n-2] <= 2:
        return is_valid(p, n-1)
    if p[n-1] - p[n-3] <= 4:
        return is_valid(p, n-2)
    return False

def permute(n, p):
    if n == 1:
        if is_valid(p, len(p)):
            return p
        return None
    for i in range(n):
        p[n-1], p[i] = p[i], p[n-1]
        result = permute(n-1, p)
        if result is not None:
            return result
        p[n-1], p[i] = p[i], p[n-1]
    return None

t = int(input())
for i in range(t):
    n = int(input())
    p = list(range(1, n+1))
    while True:
        p = permute(n, p)
    if p is None:
        print(-1)
    else:
        print(' '.join(map(str, p)))
