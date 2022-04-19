

# submitted
n, m, d = map(int, input().split())  # n = length of river, m = number of platforms, d = max distance
c = list(map(int, input().split()))  # c = array of number of platforms of each type


def get_platforms(n, m, c):
    platforms = []
    for i in range(m):
        platforms.append([i + 1] * c[i])
    return platforms


def get_river(n, m, d, platforms):
    river = [0] * n
    for i in range(n):
        for j in range(m):
            if len(platforms[j]) == 0:
                continue
            if platforms[j][0] == i + 1:
                river[i] = j + 1
                platforms[j] = platforms[j][1:]
    return river


platforms = get_platforms(n, m, c)
river = get_river(n, m, d, platforms)
print("YES")
print(*river)
