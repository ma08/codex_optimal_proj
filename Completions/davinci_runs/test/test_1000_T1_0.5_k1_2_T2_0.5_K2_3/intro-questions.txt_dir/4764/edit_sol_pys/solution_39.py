
def volume(n, h, v):
    return 2 * (n - h) * (n - v) * n

n, h, v = map(int, input().split())

print(max(volume(n, h, v), volume(n, n - h, v), volume(n, h, n - v), volume(n, n - h, n - v)))
