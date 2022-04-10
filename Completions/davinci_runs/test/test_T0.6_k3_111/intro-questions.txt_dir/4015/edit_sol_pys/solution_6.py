
def f(n,m):
    if n == m:
        return 0
    if n > m:
        return -1
    if n * 2 > m or n * 3 > m:
        return -1
    if n * 2 == m or n * 3 == m:
        return 1
    return 1 + min(f(n * 2, m), f(n * 3, m))

n, m = map(int, input().split())
print(f(n, m))
