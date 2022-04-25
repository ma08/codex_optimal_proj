

# submitted, accepted
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

def get_platforms(n, m, d, c):
    platform = []
    for i in range(1, m+1):
        platform.extend([i] * c[i-1])
    return platform

def get_river(n, m, d, c):
    platform = get_platforms(n, m, d, c)
    river = [0] * n
    for i in range(n):
        for j in range(m):
            if len(platform) == 0:
                continue
            if platform[0] == j+1:
                river[i] = platform[0]
                platform = platform[1:]
    return river

print("YES")
print(*get_river(n, m, d, c))
