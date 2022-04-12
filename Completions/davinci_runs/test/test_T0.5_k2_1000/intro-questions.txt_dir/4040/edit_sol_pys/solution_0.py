

#submitted
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

def get_platforms(n, m, d, c):
    platforms = []
    for i in range(m):
        platforms.append([i+1]*c[i])
    return platforms

def get_river(n, m, d, c):
    platforms = get_platforms(n, m, d, c)
    river = [0] * n
    for i in range(n):
        for j in range(m):
            if len(platforms[j]) == 0:
                continue
            if platforms[j][0] == i+1:
                river[i] = j+1
                platforms[j] = platforms[j][1:]
    return river

river = get_river(n, m, d, c)
if river:
    print("YES")
    print(*river)
else:
    print("NO")
