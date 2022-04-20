

n, r = map(int, input().split())

projects = [list(map(int, input().split())) for i in range(n)]

def check(r):
    for a, b in projects:
        if r < a:
            return False
        r += b
        if r < 0:
            return False
    return True

print("YES" if check(r) else "NO")