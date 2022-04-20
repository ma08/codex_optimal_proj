

n, r = map(int, input().split())
a, b = [], []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

def is_possible(r, a, b):
    for i in range(n):
        if r < a[i]:
            return False
        r += b[i]
        if r < 0:
            return False
    return True

print("YES" if is_possible(r, a, b) else "NO")