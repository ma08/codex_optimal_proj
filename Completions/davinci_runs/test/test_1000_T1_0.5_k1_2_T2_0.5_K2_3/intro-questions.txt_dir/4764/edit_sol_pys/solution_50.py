
n, h, v = map(int, input().split())

def volume(n, h, v):
    return 2 * (n - h) * (n - v) * h * v

print(max(volume(n, h, v), volume(n, n - h, v), volume(n, h, n - v), volume(n, n - h, n - v)))
