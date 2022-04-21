


n, m, d = map(int, input().split())
c = list(map(int, input().split()))

def get_platforms(n, m, d, c):
    platforms = []
    for i in range(m):
        platforms.append([i+1]*c[i])

    return platforms

def get_river(n, m, d, c):
    p = 0
    platforms = get_platforms(n, m, d, c)
    river = [0] * n
    for i in range(n):
        if len(platforms[p]) == 0:
            p += 1
        river[i] = p+1
        platforms[p] = platforms[p][1:]
        p += 1
        p %= m
    return river

print("YES")
print(*get_river(n, m, d, c))
