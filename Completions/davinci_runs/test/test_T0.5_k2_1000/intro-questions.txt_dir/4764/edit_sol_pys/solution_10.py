n, h, v = map(int, input().split())

def volume(n, h, v, x, y):
    return 2 * (n - x) * (n - y) * 4

print(max(volume(n, h, v), volume(n, n - h, v), volume(n, h, n - v), volume(n, n - h, n - v)))
