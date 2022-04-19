
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

def get_platforms(n, m, d, c):
    platforms = [0] * m
    for i in range(m - 1, -1, -1):
        platforms[i] = [i+1]*c[i]
    return platforms[::-1]

def get_river(n, m, d, c):
    platforms = get_platforms(n, m, d, c)
    river = [0] * (n+1)
    for i in range(n, 0, -1):
        for j in range(m):
            if len(platforms[j]) == 0:
                continue
            if platforms[j][0] == i:
                river[i] = j
                platforms[j] = platforms[j][1:]
    return river

print("YES")
print(*get_river(n, m, d, c))
